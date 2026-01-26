"""
Example: How to use GeoSTADConfig for different experiments.

This demonstrates the benefit of centralized configuration.
"""

from synlab.data import GeoSTADConfig, load_geostad, prepare_for_synthesis

# ============================================================
# Experiment 1: Default configuration
# ============================================================
print("Experiment 1: Default settings")
config_default = GeoSTADConfig()
df1, _ = load_geostad(config_default)
df1_features = prepare_for_synthesis(df1, config_default)
print(f"  Records: {len(df1_features):,}")
print(f"  Features: {df1_features.columns.tolist()}")
print()

# ============================================================
# Experiment 2: Only spatial features
# ============================================================
print("Experiment 2: Spatial features only")
config_spatial = GeoSTADConfig(feature_columns=["X_2025", "Y_2025", "grk2025"])
df2, _ = load_geostad(config_spatial)
df2_features = prepare_for_synthesis(df2, config_spatial)
print(f"  Records: {len(df2_features):,}")
print(f"  Features: {df2_features.columns.tolist()}")
print()

# ============================================================
# Experiment 3: Include non-geocoded businesses
# ============================================================
print("Experiment 3: All businesses (including non-geocoded)")
config_all = GeoSTADConfig(
    filter_geocoded=False,  # Keep businesses without coordinates
    feature_columns=["SN2025", "orgf2025", "grk2025"],  # No X/Y
)
df3, _ = load_geostad(config_all)
df3_features = prepare_for_synthesis(df3, config_all)
print(f"  Records: {len(df3_features):,}")
print(f"  Features: {df3_features.columns.tolist()}")
print()

print("=" * 60)
print("See how easy it is to experiment with different configs?")
print("Change settings in ONE place → affects loading AND features!")
print("=" * 60)
