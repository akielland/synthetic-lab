# Architecture

## Top-level layout

- `data/`
  - `raw/`: original or toy input data.
  - `processed/`: cleaned/encoded data ready for models.
- `outputs/`
  - Experiment outputs (synthetic data, metrics, logs).
- `src/synlab/`
  - `core/`: shared interfaces and base abstractions.
  - `data/`: dataset loaders and preprocessors.
  - `methods/`: wrappers around synthesis methods (packages, repos, custom).
  - `tasks/`: task-specific glue if needed.
  - `evaluation/`: metrics and comparison utilities.
  - `runners/`: scripts/entrypoints for experiments.
  - `utils/`: shared utilities (paths, helpers).
- `configs/`
  - Experiment configuration files by task.
- `notebooks/`
  - Exploratory analysis and result inspection.
- `docs/`
  - Vision, architecture, task descriptions, DataOps notes.
- `tests/`
  - Unit and integration tests.

## Methods vs tasks vs evaluation

- **Tasks** (e.g. `population`, `travel`) define:
  - what the data looks like,
  - which evaluation metrics are relevant.
- **Methods** are implementations of `BaseSynthesizer`:
  - `fit(data, metadata=None)`
  - `sample(n)`
- **Evaluation** compares real vs synthetic:
  - generic metrics,
  - task-specific reports.

These abstractions allow:
- multiple methods per task,
- multiple tasks sharing the same runners and infrastructure.
