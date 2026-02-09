# Synthetic Population Generator – Context for VS Code Agent

## Purpose
This document defines **exactly what the agent is expected to build**, how the system is structured, and what constraints must be respected. It is a *contract*, not a discussion. The agent should treat this as the authoritative specification.

The goal is to implement and compare **three synthetic population generators** using Norwegian register data and survey microdata, following the household-first strategy described in Rineer et al. (Nature Scientific Data, 2025).

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

