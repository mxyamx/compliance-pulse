from pathlib import Path
import pandas as pd
from pydantic import BaseModel, Field

class TelemetryRecord(BaseModel):
    user_id: str
    session_id: str
    software_version: str
    feature_code: str
    error_count: int = Field(ge=0)
    cpu_usage_pct: float = Field(ge=0.0, le=100.0)

def ingest_telemetry():
    print("🚀 Starting Telemetry Ingestion Pipeline...")
    raw_data = [
        {"user_id": "usr_9981", "session_id": "ses_abc123", "software_version": "2027.1.0", "feature_code": "CAD_RENDER_3D", "error_count": 0, "cpu_usage_pct": 45.2},
        {"user_id": "usr_4421", "session_id": "ses_xyz789", "software_version": "2027.1.0", "feature_code": "CAM_TOOLPATH", "error_count": 3, "cpu_usage_pct": 12.8},
        {"user_id": "usr_bad_data", "session_id": "ses_err000", "software_version": "2027.1.0", "feature_code": "INVALID", "error_count": -5, "cpu_usage_pct": 150.0},
    ]
    
    valid_records = []
    for item in raw_data:
        try:
            record = TelemetryRecord(**item)
            valid_records.append(record.model_dump())
        except Exception:
            print(f"⚠️ Dropped malformed record for user {item.get('user_id')}: validation error.")

    Path("data/processed").mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(valid_records)
    out_path = Path("data/processed/telemetry_clean_v1.parquet")
    df.to_parquet(out_path)
    print(f"✅ Ingested {len(df)} valid telemetry records into {out_path}")

if __name__ == "__main__":
    ingest_telemetry()