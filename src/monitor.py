from pathlib import Path
import pandas as pd

def check_data_drift_and_observability():
    print("🔍 Starting data drift and observability module...")
    scored_path = Path("data/processed/user_risk_scores_v1.parquet")
    if not scored_path.exists():
        raise FileNotFoundError(f"Dataset not found at {scored_path}. Run transform.py first!")

    df = pd.read_parquet(scored_path)
    print(f"📂 Loaded {len(df)} user profiles for integrity analysis.")

    mean_errors = df["total_errors"].mean()
    mean_cpu = df["avg_cpu_usage"].mean()
    high_risk_count = (df["compliance_status"] == "REVIEW_REQUIRED").sum()

    print("📊 System Metrics:")
    print(f"   - Average errors per user: {mean_errors:.2f}")
    print(f"   - Average CPU utilization: {mean_cpu:.2f}%")
    print(f"   - Users flagged for review: {high_risk_count}")

    error_threshold = 5.0
    if mean_errors > error_threshold:
        print(f"🚨 DRIFT ALERT: Average errors ({mean_errors}) exceed the critical threshold ({error_threshold})!")
    else:
        print("✅ Healthy Status: No data drift or abnormal regression detected.")

    print("🎯 Pipeline observability monitoring completed successfully.")

if __name__ == "__main__":
    check_data_drift_and_observability()