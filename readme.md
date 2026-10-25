# CompliancePulse ⚡

> Production-grade telemetry ingestion, behavioral feature engineering, and data drift monitoring pipeline designed for enterprise software compliance workflows.

---

## 🏗️ Architecture Overview

**CompliancePulse** acts as an automated compliance and telemetry guardian for large-scale software licensing ecosystems. It processes high-volume operational event streams, validates payloads against strict data contracts, runs unsupervised anomaly detection to score risk profiles, and provides real-time observability guardrails.

```text
compliance-pulse/
├── dashboard/
│   └── index.html             # Standalone interactive dark-mode control center UI
├── data/
│   └── processed/             # Versioned Parquet analytical datasets
├── src/
│   ├── ingest.py              # ETL pipeline & Pydantic contract validation
│   ├── transform.py           # Behavioral feature extraction & Isolation Forest scoring
│   └── monitor.py             # Observability guardrails & data drift detection
├── AI_PLAYBOOK.md             # AI-assisted development and architectural documentation
└── requirements.txt           # Core Python dependencies