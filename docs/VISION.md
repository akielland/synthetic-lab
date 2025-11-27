# Synthetic Lab – Vision

This repo is a small, reusable lab for experimenting with synthetic data production methods.

## Main goals

- Build clean, reproducible pipelines for:
  - population synthesis (tabular, both with and without differential-privacy),
  - later: travel diary synthesis (sequences).
  - later: other not yet known synthetic data
- Treat **Python packages** as first choice for methods,
  then **GitHub repos**, then **own implementations** when needed.
- Make it easy to add new methods and new tasks without redesigning everything.

## Initial focus

1. Task: population synthesis from a tabular dataset.
2. One simple package-based method as baseline.
3. Standardized evaluation so methods are comparable.
4. Later: reuse the same infrastructure for travel diaries.

## Guiding principles

- Simple, explicit directory layout (`data/`, `outputs/`, `src/`, `configs/`).
- Clear interfaces for:
  - datasets,
  - synthesizers,
  - evaluation and runners.
- Docs kept short and accurate so an AI assistant can act as a real team member.
