# Customer Success Dashboard

> A practical customer-health dashboard for monitoring account engagement, support activity, renewal risk, and success signals.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-data%20analysis-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)

## Purpose

Customer Success teams need a repeatable way to turn account activity into an actionable health view. This project demonstrates a lightweight workflow for calculating customer health scores from engagement, support, adoption, and renewal signals.

## What it demonstrates

- Data cleaning and validation with pandas
- Rule-based customer health scoring
- Risk segmentation: Healthy / Watch / At Risk
- Identification of accounts needing follow-up
- Reproducible CSV-to-report workflow

## Input signals

| Signal | Example interpretation |
|---|---|
| Product usage | Recent activity and adoption |
| Login frequency | Engagement consistency |
| Support tickets | Support demand and friction |
| CSAT | Customer satisfaction |
| Renewal proximity | Commercial urgency |

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

## Scoring model

The demo uses transparent business rules rather than a black-box model. Each account receives points for positive engagement and loses points for support volume, low satisfaction, and renewal proximity.

This makes the logic easy for a Customer Success or Operations team to inspect and adjust.

## Example use cases

- Weekly customer-health review
- CSM follow-up prioritization
- Renewal-risk monitoring
- Support-to-success handoff
- Customer portfolio reporting

## Scope

This is a portfolio project using synthetic sample data. It is not connected to a live CRM or customer database.

## Author

**Prem Sai Bachchala** — Customer Success / Operations focused portfolio project.
