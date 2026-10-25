from pathlib import Path
import pandas as pd
from sklearn.ensemble import IsolationForest

def transform_and_score():
    print("⚙️ Starting Feature Engineering & Scoring Pipeline...")
    in_path = Path("data/processed/telemetry_clean_v1.parquet")
    if not in_path.exists():
        raise FileNotFoundError("Run ingest.py first!")
    
    df = pd.read_parquet(in_path)
    print(f"📂 Loaded {len(df)} records from {in_path}")

    features = df.groupby("user_id").agg(
        avg_cpu_usage=("cpu_usage_pct", "mean"),
        total_errors=("error_count", "sum"),
        feature_diversity=("feature_code", "nunique")
    ).reset_index()

    features["risk_score_signal"] = features["total_errors"] * 1.28 + (features["avg_cpu_usage"] * 0.05)
    print("📊 Engineered behavioral features per user:")
    print(features)

    model = IsolationForest(contamination=0.1, random_state=42)
    X = features[["avg_cpu_usage", "total_errors", "risk_score_signal"]]
    features["anomaly_score"] = model.fit_predict(X)
    features["compliance_status"] = features["anomaly_score"].apply(lambda x: "REVIEW_REQUIRED" if x == -1 else "COMPLIANT")

    print("\n🎯 Model Scoring Results:")
    print(features[["user_id", "total_errors", "risk_score_signal", "compliance_status"]])

    out_path = Path("data/processed/user_risk_scores_v1.parquet")
    features.to_parquet(out_path)
    print(f"\n💾 Scored dataset successfully saved to {out_path}")

if __name__ == "__main__":
    transform_and_score()