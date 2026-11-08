# "Add to cart" button test

An online shop is testing two versions of the **Add to cart** button on its product pages.

- **Button A** is a redesign from the design team.
- **Button B** is the current button.

When a user first lands on a product page they are randomly assigned one of the two buttons. They see that same button on every visit. The team needs to decide whether the two buttons really differ in how many people click, and which one to roll out.

## What you know

- Over the last 30 days, about **10% of users** clicked the current button (B).
- New users arrive at roughly **800 per day**.
- Users can come back and visit again. Each user always sees the same button.
- Rolling out the redesign takes engineering time.
- The launch review is in **two weeks**, so the test can run for at most 14 days.

## Data

All files are in `data/`, one row per **visit**.

| File | What it contains |
|---|---|
| `experiment_days_1-5.csv` | Every visit during days 1 to 5 |
| `experiment_days_6-14_set1.csv` | Every visit during days 6 to 14 (version 1) |
| `experiment_days_6-14_set2.csv` | Every visit during days 6 to 14 (version 2) |

Your facilitator will tell you which days 6 to 14 file to use. Users who first appeared in days 1 to 5 and came back later appear in the days 6 to 14 files with the same `user_id` and button.

| Column | Meaning |
|---|---|
| `visit_id` | Unique ID of the visit |
| `user_id` | ID of the user making the visit. A returning user keeps the same ID |
| `timestamp` | When the visit happened. Day 1 starts at 2026-03-02 00:00:00 |
| `button` | `A` (redesign) or `B` (current) |
| `clicked` | 1 if the user clicked Add to cart on this visit, 0 otherwise |

## Choose a path

- **`guided/walkthrough.ipynb`**: a step-by-step notebook that takes you through planning, analysis, and a decision.
- **`self_directed/README.md`**: the task and nothing else. Figure out the approach yourself.
- **`plan_template.md`**: a blank page for writing down your plan. Either path can use it.

Install what the notebook needs with `pip install -r requirements.txt`. Spreadsheet tools work for the data too.

## Rule of the exercise

Write your plan down **before** you open any data file.
