# 🔗 Multi-Source Integration → Iceberg Lakehouse Marts (AWS)

Enterprise-grade data integration architecture that unifies IoT telemetry, ERP operational data, and Salesforce CRM records into conformed analytics marts using Apache Iceberg on Amazon S3 and Athena.

This project demonstrates scalable lakehouse modeling, incremental processing, identity resolution, and production-style orchestration.

## 📌 Problem Statement

Enterprise environments store critical signals across multiple systems:

IoT telemetry → machine behavior and anomaly signals

ERP systems → work orders, parts, inventory, costs

CRM (Salesforce) → assets, accounts, cases, revenue impact

Without integration, teams cannot reliably correlate device behavior with service events and customer impact.

This solution builds a unified analytics layer using a modern lakehouse architecture.

## 🏗 Architecture Overview
Core AWS Services

Amazon S3 → Stage / Silver / Gold storage

EventBridge → Event trigger layer

AWS Step Functions → Orchestration and retries

AWS Glue (Spark ETL) → Standardization + transformation

Glue Data Catalog → Table metadata

Apache Iceberg → ACID tables with schema evolution

Amazon Athena → SQL query engine

CloudWatch → Monitoring & observability

## 🔄 Data Flow

IoT telemetry read from Silver Iceberg tables

ERP data extracted via CDC (DMS) or batch JDBC → S3 Stage

Salesforce objects extracted incrementally using SystemModstamp → S3 Stage

EventBridge triggers Step Functions

Step Functions orchestrates:

Stage → Silver transformations

Silver → Gold conformed modeling

Glue Catalog registers Iceberg tables

Athena queries Gold marts

Streamlit dashboard presents unified analytics

## 🧱 Lakehouse Structure
Bronze / Stage (Raw Landing)

Source-aligned extracts

Immutable raw files

Partitioned by load date

Silver (Standardized Source Tables)

Schema enforcement

Deduplication

Type normalization

Data quality validation

Iceberg tables for each source

Gold (Conformed Marts)

Shared dimensions

Business-ready fact tables

Incremental MERGE patterns

Optimized for analytics queries

## 📊 Data Model
Conformed Dimensions

dim_device

dim_customer

dim_part

dim_time

bridge_device_asset (identity resolution layer)

Fact Tables

fact_telemetry_hourly

fact_work_orders

fact_cases

fact_customer_impact

## ⚙️ Incremental Processing Strategy

Salesforce incremental loads via SystemModstamp

ERP change capture via CDC or watermark columns

Iceberg MERGE for idempotent upserts

Late-arriving data window reprocessing

Audit fields (etl_run_id, ingest_ts, source_system)

## 📈 Example Analytics Enabled

Customer impact ranking by device anomalies

Correlation between failures and replaced parts

Device reliability trends by model

Work order cost analysis

SLA & freshness monitoring

## 🛡 Operational Controls

Quarantine bucket for invalid records

Retry logic in Step Functions

CloudWatch metrics for job monitoring

Schema evolution support via Iceberg

## 🔗 Links
https://multi-source-integration-to-iceberg-lakehouse-marts.streamlit.app/

## 🎯 Key Technical Concepts Demonstrated

Multi-source data integration

Lakehouse architecture (Iceberg)

Conformed dimensional modeling

Incremental + idempotent pipelines

Enterprise orchestration patterns

Cross-system identity resolution
