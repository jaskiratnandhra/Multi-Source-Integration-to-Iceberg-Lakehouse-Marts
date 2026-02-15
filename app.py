
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Multi-Source Integration → Iceberg Lakehouse (AWS)",
    page_icon="🔗",
    layout="wide",
)

# -----------------------------
# Update this to your image name/path
# -----------------------------
DIAGRAM_PATH = r"diagram.png"

# -----------------------------
# Helpers
# -----------------------------
def img_exists(p: str) -> bool:
    return Path(p).exists()

def st_image_full_width(img, caption=None):
    """Compatible across Streamlit versions (use_container_width vs use_column_width)."""
    try:
        st.image(img, caption=caption, use_container_width=True)
    except TypeError:
        st.image(img, caption=caption, use_column_width=True)

# -----------------------------
# Styling (responsive + subtle animations)
# -----------------------------
st.markdown(
    """
<style>
:root {
  --card-bg: rgba(255,255,255,0.06);
  --card-bd: rgba(255,255,255,0.12);
  --muted: rgba(255,255,255,0.72);
  --muted2: rgba(255,255,255,0.60);
  --shadow: 0 10px 30px rgba(0,0,0,0.35);
}

main .block-container {
  padding-top: 1.2rem;
  padding-bottom: 2.5rem;
  max-width: 1200px;
}

section[data-testid="stSidebar"] {
  position: sticky;
  top: 0;
  height: 100vh;
  overflow: auto;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(14px); }
  to   { opacity: 1; transform: translateY(0px); }
}
@keyframes slideIn {
  from { opacity: 0; transform: translateX(-16px); }
  to   { opacity: 1; transform: translateX(0px); }
}

.fade-up { animation: fadeUp 0.6s ease-out both; }
.slide-in { animation: slideIn 0.55s ease-out both; }

.hero {
  border: 1px solid var(--card-bd);
  background: linear-gradient(135deg, rgba(255,255,255,0.06), rgba(255,255,255,0.03));
  border-radius: 18px;
  padding: 1.25rem 1.25rem;
  box-shadow: var(--shadow);
}
.hero h1 {
  font-size: 2.05rem;
  margin: 0 0 0.25rem 0;
  letter-spacing: -0.02em;
}
.hero p {
  margin: 0.15rem 0 0 0;
  color: var(--muted);
  line-height: 1.45;
}

.chips { margin-top: 0.75rem; }
.chip {
  display: inline-block;
  padding: 0.28rem 0.65rem;
  margin: 0.25rem 0.35rem 0 0;
  border-radius: 999px;
  border: 1px solid var(--card-bd);
  background: rgba(255,255,255,0.05);
  font-size: 0.85rem;
  color: rgba(255,255,255,0.86);
}

.grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 12px;
  margin-top: 0.85rem;
}
.card {
  grid-column: span 3;
  border: 1px solid var(--card-bd);
  background: var(--card-bg);
  border-radius: 16px;
  padding: 0.95rem 0.95rem;
  box-shadow: 0 8px 22px rgba(0,0,0,0.25);
  min-height: 92px;
}
.card .k { font-size: 0.85rem; color: var(--muted2); margin-bottom: 0.35rem; }
.card .v { font-size: 1.1rem; font-weight: 650; }
.card .s { font-size: 0.85rem; color: var(--muted); margin-top: 0.3rem; line-height: 1.35; }

@media (max-width: 900px) {
  .card { grid-column: span 6; }
  .hero h1 { font-size: 1.7rem; }
}
@media (max-width: 560px) {
  main .block-container { padding-left: 0.85rem; padding-right: 0.85rem; }
  .card { grid-column: span 12; }
}

.section-title {
  font-size: 1.25rem;
  font-weight: 750;
  margin-top: 0.4rem;
  margin-bottom: 0.2rem;
  letter-spacing: -0.01em;
}
.section-sub {
  color: var(--muted);
  margin-bottom: 0.75rem;
}

img { border-radius: 14px; }

div[data-testid="stExpander"] {
  border: 1px solid rgba(255,255,255,0.10);
  border-radius: 14px;
}
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Sidebar navigation
# -----------------------------
st.sidebar.title("Sections")
page = st.sidebar.radio(
    "Go to",
    ["Overview", "Architecture", "Data Model", "Incremental Loads", "Dashboard Views"],
)
st.sidebar.markdown("---")
st.sidebar.caption("Multi-source lakehouse blueprint")

# -----------------------------
# Hero header
# -----------------------------
st.markdown(
    """
<div class="hero fade-up">
  <h1>🔗 Multi-Source Integration → Iceberg Lakehouse Marts</h1>
  <p>
    A unified analytics architecture that integrates IoT telemetry, ERP operational data, and Salesforce CRM events
    into conformed dimensions and fact tables stored as Apache Iceberg on Amazon S3 and queried through Athena.
  </p>
  <div class="chips">
    <span class="chip">S3 (Stage/Silver/Gold)</span>
    <span class="chip">EventBridge</span>
    <span class="chip">Step Functions</span>
    <span class="chip">Glue ETL (Spark)</span>
    <span class="chip">Glue Data Catalog</span>
    <span class="chip">Apache Iceberg</span>
    <span class="chip">Athena</span>
    <span class="chip">CloudWatch</span>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="grid fade-up">
  <div class="card">
    <div class="k">Sources</div>
    <div class="v">IoT + ERP + CRM</div>
    <div class="s">Telemetry + work orders + assets/cases unified for analytics.</div>
  </div>
  <div class="card">
    <div class="k">Output</div>
    <div class="v">Conformed Marts</div>
    <div class="s">Dimensions + facts built for reporting and investigation.</div>
  </div>
  <div class="card">
    <div class="k">Storage</div>
    <div class="v">Iceberg on S3</div>
    <div class="s">ACID tables with schema evolution and upserts.</div>
  </div>
  <div class="card">
    <div class="k">Query Layer</div>
    <div class="v">Athena SQL</div>
    <div class="s">Catalog-backed SQL access for dashboards and ad-hoc queries.</div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

# -----------------------------
# Content Sections
# -----------------------------
if page == "Overview":
    st.markdown('<div class="section-title slide-in">Overview</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub slide-in">Unify telemetry, operations, and customer signals into a single analytics layer.</div>',
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns([1.15, 1])

    with c1:
        st.markdown(
            """
**Problem**  
Enterprise environments store critical signals across multiple platforms:
- **IoT telemetry** (what the machine is doing)
- **ERP** (work orders, parts, inventory, costs)
- **CRM** (assets, accounts, cases, revenue risk)

Without integration, teams can’t reliably answer:
- Which devices are driving the most service activity and cost?
- Which customers are impacted and how severe is it?
- Which parts correlate with repeated failures?

**Solution**  
A lakehouse integration pipeline that lands source extracts in S3 staging, standardizes each source into
Silver tables, and produces Gold marts with conformed dimensions and facts.
"""
        )

    with c2:
        st.markdown(
            """
**Key outcomes**
- Conformed keys for device/customer/part across systems  
- Unified marts for reliability, customer impact, and parts correlation  
- Incremental loads with idempotent merges into Iceberg  
- Operational controls: retries, quarantine, freshness monitoring  
"""
        )

    st.markdown("### Gold mart examples")
    st.markdown(
        """
- `fact_customer_impact` — devices impacted, cases opened, work orders opened, anomaly hours, estimated cost  
- `fact_work_orders` — cost, labor hours, part replacements by device and time  
- `fact_cases` — severity and case lifecycle aligned to device and customer  
- `fact_telemetry_hourly` — hourly rollups and anomaly counts per device  
"""
    )

elif page == "Architecture":
    st.markdown('<div class="section-title slide-in">Architecture</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub slide-in">Arrow-correct data flow from sources to curated marts.</div>',
        unsafe_allow_html=True,
    )

    if img_exists(DIAGRAM_PATH):
        st_image_full_width(DIAGRAM_PATH, caption="IoT + ERP + Salesforce → Iceberg Lakehouse Marts (S3 + Athena)")
    else:
        st.warning(
            f"Diagram not found at: {DIAGRAM_PATH}\n\n"
            "Save your diagram next to this file as 'project3_diagram.png', or update DIAGRAM_PATH."
        )

    st.markdown("### High-level flow")
    st.markdown(
        """
1) IoT telemetry is read from existing Iceberg Silver/Gold tables  
2) ERP data is extracted (DMS CDC or JDBC batch) into **S3 Stage (ERP)**  
3) Salesforce objects are extracted incrementally into **S3 Stage (Salesforce)**  
4) **EventBridge** triggers **Step Functions** on schedule or new arrivals  
5) Step Functions orchestrates:
   - **Glue ETL Stage → Silver** (schema enforcement, dedupe, normalization)  
   - **Glue ETL Silver → Gold** (conformed dimensions + fact marts)  
6) **Glue Data Catalog** registers Iceberg tables for SQL access  
7) **Athena** queries marts for Streamlit dashboards  
"""
    )

elif page == "Data Model":
    st.markdown('<div class="section-title slide-in">Data Model</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub slide-in">Conformed dimensions and facts designed for enterprise analytics.</div>',
        unsafe_allow_html=True,
    )

    st.markdown("### Conformed dimensions (shared keys across systems)")
    st.markdown(
        """
- **dim_device**: `device_id, serial_number, site_id, model, install_date, customer_id, crm_asset_id`  
- **dim_customer**: `customer_id, account_id, customer_name, region, tier`  
- **dim_part**: `part_id, part_number, description, supplier, standard_cost`  
- **dim_time**: `date, hour, week, month, year`  
"""
    )

    st.markdown("### Facts (core measures)")
    st.markdown(
        """
- **fact_telemetry_hourly**: `(device_id, hour_ts) → avg/max/p95/anomaly_count/event_count`  
- **fact_work_orders**: `(work_order_id) → device_id, part_id, labor_hours, total_cost, status, opened/closed`  
- **fact_cases**: `(case_id) → customer_id, crm_asset_id, device_id, severity, status, opened/closed`  
- **fact_customer_impact**: `(date, customer_id) → impacted_devices, cases, work_orders, anomaly_hours, estimated_cost`  
"""
    )

    with st.expander("Identity resolution (device ↔ asset mapping)", expanded=True):
        st.markdown(
            """
Real systems use different identifiers:
- Telemetry may use `device_id` or `serial_number`
- Salesforce may use `asset_id`
- ERP may reference serials in work orders

Create a bridge table to align identities:

- **bridge_device_asset**
  - `device_id, serial_number, crm_asset_id, customer_id, effective_start, effective_end`

This table enables reliable joins across all facts.
"""
        )

elif page == "Incremental Loads":
    st.markdown('<div class="section-title slide-in">Incremental Loads</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub slide-in">Efficient ingestion and idempotent merges for correctness under retries.</div>',
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### Salesforce incremental extraction")
        st.markdown(
            """
- Use `SystemModstamp` as the watermark per object (Cases, Assets, Accounts)  
- Extract only `SystemModstamp > last_successful_watermark`  
- Store `watermark_state` per object (S3 or DynamoDB)  
"""
        )

        st.markdown("### ERP incremental strategy")
        st.markdown(
            """
- Prefer **DMS CDC** for inserts/updates/deletes  
- Alternative for batch: watermark by `updated_at` or numeric surrogate key  
"""
        )

    with c2:
        st.markdown("### Iceberg MERGE patterns (idempotent)")
        st.markdown(
            """
- Cases: MERGE on `case_id`  
- Work orders: MERGE on `work_order_id`  
- Telemetry hourly: MERGE on `(device_id, hour_ts)`  
- Late arrivals: reprocess last N days (e.g., 3–7)  
"""
        )

        st.markdown("### Audit & lineage columns")
        st.markdown(
            """
Add to all Silver/Gold tables:
- `etl_run_id`, `ingest_ts`, `source_system`, `source_file`  
"""
        )

elif page == "Dashboard Views":
    st.markdown('<div class="section-title slide-in">Dashboard Views</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub slide-in">What stakeholders can see from the unified marts.</div>',
        unsafe_allow_html=True,
    )

    a, b = st.columns(2)

    with a:
        st.markdown("### Customer Impact")
        st.markdown(
            """
- Customers ranked by impacted devices (7/30 days)  
- Cases + work orders correlated to telemetry anomalies  
- Estimated cost and severity breakdown  
"""
        )

        st.markdown("### Device Reliability")
        st.markdown(
            """
- Anomaly rate by model/site  
- Devices with repeated service actions  
- Trend of hourly metrics and anomaly counts  
"""
        )

    with b:
        st.markdown("### Parts Correlation")
        st.markdown(
            """
- Parts most frequently associated with work orders  
- Parts correlated with high anomaly periods  
- MTBF-style summaries by model/part  
"""
        )

        st.markdown("### Data Freshness & SLA")
        st.markdown(
            """
- Latest successful load per source (IoT/ERP/Salesforce)  
- Lag and failure tracking  
- Job duration and throughput indicators  
"""
        )

st.divider()
st.caption("Multi-Source Integration → Iceberg Lakehouse Marts (AWS) — Architecture & Solution Blueprint")