# Task: Population Synthesis

## Goal

Generate synthetic populations (and other synthetic data) that resemble a real population dataset on key
marginals and simple joint distributions.

## Dataset (v1 – toy)

- Input: tabular CSV in `data/raw/population/`.
- Each row: one person.
- Example variables (tentative):
  - `age` (integer or binned),
  - `gender`,
  - `household_size`,
  - `income_bracket`,
  - `employment_status`,
  - `region` or `zone`.

## Minimal v1 requirements

- Use a small toy CSV (can be fabricated) with:
  - 200–1000 rows,
  - 4–8 columns as above.
- No strict schema enforcement yet; keep it simple.

## Output

- Synthetic dataset with the **same columns**.
- Saved per experiment under `outputs/population/<experiment_name>/`.

## Future refinements

- Add explicit schema metadata (types, allowed categories).
- Add constraints (e.g., age compatible with employment_status).
- Connect to real-world population sources when the skeleton is stable.
