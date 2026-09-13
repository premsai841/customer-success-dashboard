# Customer Success Dashboard

> A practical portfolio project showing how customer activity and service signals can be organized into a simple customer-health view for Customer Success follow-up.

## Career context

This project supports my Customer Success career focus. It reflects the type of work I want to understand better: customer health monitoring, risk identification, follow-up prioritization, reporting, and process improvement.

## Business problem

Customer Success teams need a repeatable way to identify accounts that may need attention. A health view can combine engagement, support activity, satisfaction, and renewal timing into one reviewable report.

## What the project demonstrates

- Customer-health thinking and risk segmentation
- Data validation and structured reporting
- Rule-based prioritization
- Identifying accounts that need follow-up
- Turning customer signals into an operational view

## Input signals

| Signal | Example interpretation |
|---|---|
| Product usage | Recent activity and adoption |
| Login frequency | Engagement consistency |
| Support tickets | Support demand and friction |
| CSAT | Customer satisfaction |
| Renewal proximity | Commercial urgency |

## Workflow

```text
Customer data
    ↓
Validate input
    ↓
Calculate health score
    ↓
Segment account risk
    ↓
Prioritize follow-up
    ↓
Generate customer-health report
```

## Project structure

```text
customer-success-dashboard/
├── data/
│   └── customers.csv
├── src/
│   └── health_score.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Run locally

```bash
pip install -r requirements.txt
python src/health_score.py
```

The script prints a customer-health summary and writes `data/customer_health_output.csv`.

## Technical learning

The implementation uses Python and Pandas as learning tools for processing structured data. I am not presenting this project as evidence of professional software-development experience.

## Scoring approach

The demo uses transparent business rules rather than a black-box model. Accounts receive points for positive engagement and lose points for support volume, lower satisfaction, and renewal proximity. The logic is intentionally easy for a Customer Success or Operations team to inspect and adjust.

## Scope

Synthetic sample data only. No real customer, CRM, or company data is included.

## Author

**Prem Sai Bachchala** — Customer Success / Customer Support / Operations portfolio.
