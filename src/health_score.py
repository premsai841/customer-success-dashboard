from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "customers.csv"
OUTPUT_FILE = BASE_DIR / "data" / "customer_health_output.csv"


def calculate_health(row: pd.Series) -> tuple[int, str]:
    score = 50

    score += min(row["monthly_active_users"] * 0.5, 20)
    score += min(row["logins_30d"] * 1.0, 15)
    score += max(min((row["csat"] - 3.0) * 8, 15), -15)
    score -= min(row["support_tickets_30d"] * 2, 16)

    if row["days_to_renewal"] <= 30:
        score -= 10
    elif row["days_to_renewal"] <= 60:
        score -= 5

    score = int(round(max(0, min(100, score))))

    if score >= 70:
        status = "Healthy"
    elif score >= 50:
        status = "Watch"
    else:
        status = "At Risk"

    return score, status


def main() -> None:
    df = pd.read_csv(DATA_FILE)

    required = {
        "customer_id",
        "customer_name",
        "monthly_active_users",
        "logins_30d",
        "support_tickets_30d",
        "csat",
        "days_to_renewal",
    }
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    df[["health_score", "health_status"]] = df.apply(
        lambda row: pd.Series(calculate_health(row)), axis=1
    )
    df["follow_up_priority"] = df["health_score"].apply(
        lambda score: "High" if score < 50 else "Medium" if score < 70 else "Low"
    )

    df = df.sort_values(["follow_up_priority", "health_score", "days_to_renewal"], ascending=[True, True, True])
    df.to_csv(OUTPUT_FILE, index=False)

    print("Customer Health Summary")
    print("=" * 24)
    print(df[["customer_name", "health_score", "health_status", "follow_up_priority"]].to_string(index=False))
    print(f"\nSaved report to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
