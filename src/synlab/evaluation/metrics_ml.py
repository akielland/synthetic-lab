from __future__ import annotations

from typing import Dict, Optional, List, Any

import numpy as np
import pandas as pd

from pandas.api.types import is_numeric_dtype

from .metrics_basic import _get_common_columns

# Optional dependency: scikit-learn
try:
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import Pipeline
    from sklearn.compose import ColumnTransformer
    from sklearn.preprocessing import OneHotEncoder, StandardScaler
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import (
        accuracy_score,
        f1_score,
        roc_auc_score,
        log_loss,
    )

    _HAVE_SKLEARN = True
except ImportError:  # pragma: no cover
    _HAVE_SKLEARN = False


def _check_sklearn():
    if not _HAVE_SKLEARN:
        raise RuntimeError(
            "scikit-learn is required for ML-based evaluation metrics. "
            "Install it with `pip install scikit-learn`."
        )


def _split_numeric_categorical(df: pd.DataFrame, feature_cols: List[str]) -> (List[str], List[str]):
    numeric_cols = [c for c in feature_cols if is_numeric_dtype(df[c])]
    categorical_cols = [c for c in feature_cols if c not in numeric_cols]
    return numeric_cols, categorical_cols


def _build_preprocessor(
    df: pd.DataFrame,
    feature_cols: List[str],
) -> ColumnTransformer:
    numeric_cols, categorical_cols = _split_numeric_categorical(df, feature_cols)

    transformers = []
    if numeric_cols:
        transformers.append(
            ("num", StandardScaler(), numeric_cols)
        )
    if categorical_cols:
        transformers.append(
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore", sparse=False),
                categorical_cols,
            )
        )

    if not transformers:
        # Degenerate case: no features at all
        transformers.append(("passthrough", "passthrough", feature_cols))

    preprocessor = ColumnTransformer(
        transformers=transformers,
        remainder="drop",
    )
    return preprocessor


# ----------------------------------------------------------------------
# 1) Discriminative two-sample test (real vs synthetic)
# ----------------------------------------------------------------------


def discriminative_score(
    real_df: pd.DataFrame,
    synth_df: pd.DataFrame,
    columns: Optional[List[str]] = None,
    test_size: float = 0.3,
    random_state: int = 0,
    classifier: str = "logreg",
) -> Dict[str, Any]:
    """
    Train a classifier to distinguish real vs synthetic rows
    (two-sample test using a discriminative model).

    Lower performance => synthetic data more similar to real.

    Parameters
    ----------
    real_df, synth_df : DataFrames
        Real and synthetic datasets.
    columns : list[str] or None
        Feature columns to use. If None, use intersection of columns.
    test_size : float
        Fraction of data used as test set.
    random_state : int
        Random seed for the split.
    classifier : {"logreg", "rf"}
        Logistic regression or random forest.

    Returns
    -------
    dict with keys:
        "auc", "accuracy", "f1", "log_loss",
        "n_train", "n_test", "classifier"
    """
    _check_sklearn()

    cols = _get_common_columns(real_df, synth_df, columns)

    # Label data: 1 = real, 0 = synthetic
    real_data = real_df[cols].copy()
    real_data["__is_real__"] = 1

    synth_data = synth_df[cols].copy()
    synth_data["__is_real__"] = 0

    combined = pd.concat([real_data, synth_data], axis=0, ignore_index=True)

    y = combined["__is_real__"].to_numpy()
    X = combined.drop(columns=["__is_real__"])

    feature_cols = list(X.columns)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    preprocessor = _build_preprocessor(X_train, feature_cols)

    if classifier == "logreg":
        clf = LogisticRegression(
            max_iter=1000,
            n_jobs=None,
        )
    elif classifier == "rf":
        clf = RandomForestClassifier(
            n_estimators=200,
            random_state=random_state,
            n_jobs=-1,
        )
    else:
        raise ValueError(f"Unsupported classifier: {classifier!r}")

    model = Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("clf", clf),
        ]
    )

    model.fit(X_train, y_train)

    y_prob = model.predict_proba(X_test)[:, 1]
    y_pred = (y_prob >= 0.5).astype(int)

    auc = roc_auc_score(y_test, y_prob)
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    ll = log_loss(y_test, y_prob)

    return {
        "auc": float(auc),
        "accuracy": float(acc),
        "f1": float(f1),
        "log_loss": float(ll),
        "n_train": int(len(y_train)),
        "n_test": int(len(y_test)),
        "classifier": classifier,
    }


# ----------------------------------------------------------------------
# 2) TSTR: Train on Synthetic, Test on Real (classification)
# ----------------------------------------------------------------------


def tstr_classification(
    real_df: pd.DataFrame,
    synth_df: pd.DataFrame,
    target_col: str,
    feature_columns: Optional[List[str]] = None,
    test_size: float = 0.3,
    random_state: int = 0,
    model_type: str = "logreg",
) -> Dict[str, Any]:
    """
    TSTR (Train on Synthetic, Test on Real) for classification tasks.

    Train a classifier on synthetic data and evaluate on real data.
    This measures whether synthetic data preserves signal relevant
    for predicting `target_col`.

    Parameters
    ----------
    real_df, synth_df : DataFrames
        Real and synthetic datasets.
    target_col : str
        Name of the target column (classification).
    feature_columns : list[str] or None
        Feature columns to use. If None, use common columns minus target.
    test_size : float
        Fraction of real data to reserve as test set. (Train uses synthetic only.)
    random_state : int
        Random seed.
    model_type : {"logreg", "rf"}
        Classifier type.

    Returns
    -------
    dict with keys:
        "accuracy", "f1_macro", "roc_auc_ovr",
        "n_train_synth", "n_test_real",
        "model_type", "n_classes"
    """
    _check_sklearn()

    if target_col not in real_df.columns or target_col not in synth_df.columns:
        raise ValueError(f"target_col {target_col!r} must exist in both real and synthetic DataFrames")

    # Determine feature columns
    if feature_columns is None:
        common_cols = _get_common_columns(real_df, synth_df)
        feature_columns = [c for c in common_cols if c != target_col]

    # Train on synthetic
    y_synth = synth_df[target_col].to_numpy()
    X_synth = synth_df[feature_columns].copy()

    # Test on held-out real
    y_real = real_df[target_col].to_numpy()
    X_real = real_df[feature_columns].copy()

    # split only the *real* data (for robustness you may want to keep a real train subset for other baselines)
    X_real_train, X_real_test, y_real_train, y_real_test = train_test_split(
        X_real, y_real, test_size=test_size, random_state=random_state, stratify=y_real
    )

    # For TSTR we train on *all* synthetic data
    preprocessor = _build_preprocessor(X_synth, feature_columns)

    if model_type == "logreg":
        clf = LogisticRegression(
            max_iter=1000,
            n_jobs=None,
        )
    elif model_type == "rf":
        clf = RandomForestClassifier(
            n_estimators=200,
            random_state=random_state,
            n_jobs=-1,
        )
    else:
        raise ValueError(f"Unsupported model_type: {model_type!r}")

    model = Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("clf", clf),
        ]
    )

    model.fit(X_synth, y_synth)

    y_prob = model.predict_proba(X_real_test)
    y_pred = np.argmax(y_prob, axis=1)

    acc = accuracy_score(y_real_test, y_pred)
    f1_macro = f1_score(y_real_test, y_pred, average="macro")

    # ROC-AUC (one-vs-rest) if multiclass
    try:
        roc_auc = roc_auc_score(
            y_real_test,
            y_prob,
            multi_class="ovr",
        )
    except Exception:
        roc_auc = np.nan

    n_classes = len(np.unique(y_synth))

    return {
        "accuracy": float(acc),
        "f1_macro": float(f1_macro),
        "roc_auc_ovr": float(roc_auc) if not np.isnan(roc_auc) else np.nan,
        "n_train_synth": int(len(y_synth)),
        "n_test_real": int(len(y_real_test)),
        "model_type": model_type,
        "n_classes": int(n_classes),
    }


# ----------------------------------------------------------------------
# 3) Baseline: Train/Test on Real (TRTR) – for comparison
# ----------------------------------------------------------------------


def real_baseline_classification(
    real_df: pd.DataFrame,
    target_col: str,
    feature_columns: Optional[List[str]] = None,
    test_size: float = 0.3,
    random_state: int = 0,
    model_type: str = "logreg",
) -> Dict[str, Any]:
    """
    Baseline: train and test on real data only (standard supervised split).

    This is useful to compare against TSTR to see how much performance
    is lost when training on synthetic instead of real.

    Returns
    -------
    dict with keys:
        "accuracy", "f1_macro", "roc_auc_ovr",
        "n_train_real", "n_test_real", "model_type", "n_classes"
    """
    _check_sklearn()

    if target_col not in real_df.columns:
        raise ValueError(f"target_col {target_col!r} must exist in real_df")

    if feature_columns is None:
        feature_columns = [c for c in real_df.columns if c != target_col]

    y = real_df[target_col].to_numpy()
    X = real_df[feature_columns].copy()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    preprocessor = _build_preprocessor(X_train, feature_columns)

    if model_type == "logreg":
        clf = LogisticRegression(
            max_iter=1000,
            n_jobs=None,
        )
    elif model_type == "rf":
        clf = RandomForestClassifier(
            n_estimators=200,
            random_state=random_state,
            n_jobs=-1,
        )
    else:
        raise ValueError(f"Unsupported model_type: {model_type!r}")

    model = Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("clf", clf),
        ]
    )

    model.fit(X_train, y_train)

    y_prob = model.predict_proba(X_test)
    y_pred = np.argmax(y_prob, axis=1)

    acc = accuracy_score(y_test, y_pred)
    f1_macro = f1_score(y_test, y_pred, average="macro")

    try:
        roc_auc = roc_auc_score(
            y_test,
            y_prob,
            multi_class="ovr",
        )
    except Exception:
        roc_auc = np.nan

    n_classes = len(np.unique(y))

    return {
        "accuracy": float(acc),
        "f1_macro": float(f1_macro),
        "roc_auc_ovr": float(roc_auc) if not np.isnan(roc_auc) else np.nan,
        "n_train_real": int(len(y_train)),
        "n_test_real": int(len(y_test)),
        "model_type": model_type,
        "n_classes": int(n_classes),
    }
