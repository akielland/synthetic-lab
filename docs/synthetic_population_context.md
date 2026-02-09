# Synthetic Population Generator – Context for VS Code Agent

## Purpose
This document defines **exactly what the agent is expected to build**, how the system is structured, and what constraints must be respected. It is a *contract*, not a discussion. The agent should treat this as the authoritative specification.

The goal is to implement and compare **three synthetic population generators** using Norwegian register data and survey microdata, following the household-first strategy described in Rineer et al. (Nature Scientific Data, 2025, https://www.nature.com/articles/s41597-025-04380-7).

---

## Core Principles (Non‑negotiable)

1. **Registers define population mass**  
   - BSUs (geographic units) have fixed populations.
   - Person counts by gender × age group are hard constraints.

2. **Survey data provides patterns, not counts**  
   - Survey households/persons are templates.
   - Templates may be reused across BSUs.
   - Templates may receive weight zero in a BSU.

3. **Households are atomic units** (for household-based generators)
   - Persons are never sampled independently once households are used.
   - Household members are copied together.

4. **All constraint violations must be logged**  
   - Any geographic expansion or category relaxation must be recorded.

---

## Available Data

### Register data (hard)
- `N(bsu, gender_age_gr)`

### Register-derived proportions (soft → converted to BSU targets)
- `P(gender, age_gr, household_size, fam_type)`
- `P(employed | bsu, age_gr)`
- `P(employed | bsu, gender)`
- `P(income_index | bsu)`
- `P(car_type | bsu)`

### Survey data
- Person-level table with household variables duplicated per person:
  - `gender`, `age_gr`, `employed`, `income_index`, `car_type`
  - `household_size`, `fam_type`
  - child age variables (`ALDER_BARN_*`) – realism only
- Travel-behaviour table (used **after** population generation)

---

## Preprocessing (Run Once)

### Preprocessed artifacts (must be written to disk and reused)
- `processed/targets_bsu.parquet` (long-format targets, one row per BSU × constraint × category)
- `processed/survey_persons_harmonized.parquet`
- `processed/survey_households_templates.parquet`
- `processed/household_contributions.parquet` (sparse/long format contributions)
- `processed/category_maps.json` (explicit binning + codebook)

### Input/Output schemas (minimum required columns)
#### Register counts
- `bsu_id` (string)
- `gender` (category)
- `age_gr` (category)
- `count` (int)

#### BSU proportions (one table per distribution or a unified long table)
- `bsu_id` (string)
- `dist_name` (e.g., `hh_size_fam_type`, `income_index`, `car_type`, `employed_age`, ...)
- `category_key` (string; e.g., `size=4|type=3`)
- `p` (float in [0,1])

#### Survey persons (harmonized)
- `person_id` (string/int)
- `hh_id` (string/int; can be constructed)
- `gender`, `age_gr`, `employed`, `income_index`, `car_type` (categories)
- `hh_size`, `fam_type` (categories)
- optional realism vars (e.g., `ALDER_BARN_1..5`)

#### Household templates
- `hh_id`
- `hh_size`, `fam_type`, `car_type`
- `members` (list of person_ids) OR a separate link table `hh_members(hh_id, person_id)`

#### Household contributions (long sparse)
- `hh_id`
- `constraint_name` (e.g., `gender_age`, `hh_size_fam_type_persons`, `employed`, `income_index`, `car_type`)
- `category` (string key)
- `value` (int contribution)

---

## Calibration and sampling details (must be implemented)

### Calibration algorithm (household weights)
Use **iterative proportional fitting / raking on linear constraints** over households.
- Maintain household weights `w_h` (start at 1).
- For each constraint cell `j` with target `T_j`:
  - compute current total `S_j = Σ_h w_h * c_{h,j}`
  - multiply each household weight by an adjustment factor based on its contribution:
    - for binary/indicator constraints: `w_h ← w_h * (T_j / S_j)` for households in that cell
    - for count contributions (e.g., gender×age counts inside household): use generalized raking update:
      `w_h ← w_h * (T_j / S_j)^{c_{h,j}}`
- Iterate constraints in priority order until convergence.

If convergence is unstable or constraints are inconsistent, implement **tiered fitting**:
1) Fit hard constraints (gender×age) to tight tolerance.
2) Freeze/clip weights and fit household-structure constraints.
3) Fit soft constraints last (employment/income/car_type).

### Integerization / sampling
After calibration, produce an integer household sample:
- Default: **systematic PPS sampling** of households with probabilities ∝ `w_h` until person total matches `N(bsu)`.
- Enforce exact person total by:
  - sampling households until within ±(max household size), then adjust by resampling last households.

### Tolerances (acceptance thresholds)
- Hard: gender×age counts per BSU must match exactly **or** within `max(1, 0.1% of cell)` when exact is impossible due to household granularity.
- Household structure (persons in hh_size×fam_type): target relative error ≤ 2% per BSU (median), flag if >5%.
- Soft constraints (employment/income/car_type): target relative error ≤ 5% per BSU (median), flag if >10%.

### Logging format (mandatory)
Write one JSONL row per BSU per generator:
- `bsu_id`, `generator`, `seed`
- `expanded_level` (none/local/regional/national)
- `relaxations` (list)
- `fit_stats` (RMSE, max_abs_err, max_rel_err per constraint family)
- `ess` and weight concentration stats

---

## Geographic expansion and relaxation (programmatic rules)

### Candidate pool hierarchy
Define levels (customize to available metadata):
1) `local`: same municipality/region as BSU (or closest survey stratum)
2) `regional`: same county
3) `national`: all survey households

### When to expand
For each BSU after calibration attempt, compute **support ratio** for each required constraint cell:
- `support(cell) = #households with c_{h,cell} > 0`
- Require `support(cell) ≥ max(2, ceil(α * required_households_in_cell))` with default `α = 0.15`.
If any critical cell fails, expand one level and retry.

### Relaxation order (applied only after national expansion)
1) Merge `hh_size` bins (e.g., 5→4–6, 7+)
2) Merge `fam_type` bins (coarser family categories)
3) Merge `income_index` bins
4) Drop soft constraints one by one

Every expansion/relaxation must be logged.

---

## Execution model
- Generators run independently but **share preprocessed artifacts** from the Preprocessing stage.
- Each generator writes outputs to separate folders and produces comparable diagnostics.



### 1. Harmonize categories
- Align survey and register bins for all constrained variables.
- Store mappings explicitly.

### 2. Convert proportions → BSU target counts
For each BSU:
- `N(bsu) = sum_g,a N(bsu,g,a)`
- Compute target vectors:
  - `T_gender_age(bsu)` **(hard)**
  - `T_household_size_type_persons(bsu)`
  - `T_employed(bsu)`
  - `T_income(bsu)`
  - `T_car_type(bsu)`

### 3. Build survey pools

#### Pool A: Person pool
- Individual survey persons (used by person-only generator).

#### Pool B: Household-template pool
1. Identify or construct `hh_id`.
2. Collapse persons → households.
3. Store:
   - household attributes (`size`, `type`, `car_type`)
   - list of member persons
4. Precompute **contribution vectors** per household:
   - counts by gender_age_gr
   - counts by employment
   - counts by income_index
   - counts by car_type
   - counts contributing to `(household_size, fam_type)` person totals

---

## Generators to Implement

### Generator 1 (MAIN): Household‑first, person‑constrained
**Reference:** Rineer et al. (2025), adapted to Norwegian registers.

Per BSU:
1. Load BSU targets.
2. Select candidate household templates (start local).
3. Calibrate household weights `w_h` such that:
   - `Σ w_h * contribution_h ≈ targets`
   - Priority order:
     1. gender × age (hard)
     2. household_size × fam_type (strong)
     3. employed, income_index, car_type (soft)
4. Sample households using calibrated weights.
5. Expand households → persons.
6. Validate and log errors.

Fallback logic:
- If insufficient candidates:
  - expand survey geography (regional → national)
  - relax constraints in order:
    1. household_size bins
    2. fam_type bins
    3. income bins
    4. drop soft constraints

Outputs:
- `synthetic_households_main`
- `synthetic_persons_main`

---

### Generator 2 (CONTROL 1): Person‑only IPF
Purpose: baseline without household structure.

Per BSU:
1. Calibrate person weights to:
   - gender × age (hard)
   - optionally employed, income, car_type
2. Sample `N(bsu)` persons.

Output:
- `synthetic_persons_persononly`

---

### Generator 3 (CONTROL 2): Household‑first, structure‑only
Purpose: isolate effect of household structure without extra person constraints.

Per BSU:
1. Targets:
   - gender × age (hard)
   - household_size × fam_type persons (strong)
2. Calibrate and sample households.
3. Expand to persons.
4. Evaluate employment/income/car_type **diagnostically only**.

Outputs:
- `synthetic_households_structure_only`
- `synthetic_persons_structure_only`

---

## Diagnostics (Mandatory)

For each generator:
- Constraint fit per BSU and nationally
- Absolute and relative errors
- Effective sample size (ESS)
- Weight concentration
- Flags for expansion/relaxation

Compare generators on:
- person marginals
- household realism
- out‑of‑constraint joint distributions

---

## Travel Behaviour Assignment (Post‑processing)

1. Choose preferred synthetic population (likely Generator 1).
2. For each synthetic person, identify donor set in travel survey using:
   - gender, age_gr, employed, household_size/type, income_index, car_type
3. Sample travel behaviour conditionally.
4. Validate aggregated travel patterns.

---

## Implementation Notes for Agent

- Do **not** invent households or persons.
- Do **not** modify register totals.
- Treat survey households as reusable templates.
- Keep preprocessing, generators, and diagnostics modular.
- All random steps must be seed‑controlled.

This file is the authoritative guide. Deviations must be explicit and justified.

