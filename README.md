# Modern ELT Pipeline (Project 1)

A production-style ELT pipeline demonstrating orchestration, transformation, and warehouse design using modern data engineering tools.

### Key Design Elements:
- Multi-layer architecture: raw → staging → analytics
- Airflow-based orchestration for scheduling and dependency management
- Python + SQL-based transformation layer for data processing
- Dockerized infrastructure for reproducible environments
- PostgreSQL used as a lightweight analytical warehouse

### Real-World Relevance:
- Mimics batch ingestion pipelines used in analytics platforms
- Demonstrates workflow orchestration patterns used in modern data stacks
- Reflects warehouse-style data modeling for BI/reporting systems

## 🏗️ System Architecture

            ┌──────────────┐
            │ CSV / API    │
            │ Data Sources │
            └──────┬───────┘
                   ↓
        ┌──────────────────────┐
        │ Python Ingestion     │
        │ (Extract + Load)     │
        └────────┬─────────────┘
                 ↓
     ┌──────────────────────────┐
     │ PostgreSQL (Raw Layer)   │
     │ Staging Tables           │
     └────────┬─────────────────┘
              ↓
     ┌──────────────────────────┐
     │ Airflow Orchestration    │
     │ (DAG Scheduling Engine)  │
     └────────┬─────────────────┘
              ↓
     ┌──────────────────────────┐
     │ Transformation Layer     │
     │ (Python + SQL Logic)     │
     └────────┬─────────────────┘
              ↓
     ┌──────────────────────────┐
     │ Analytics Layer          │
     │ PostgreSQL Tables        │
     └──────────────────────────┘
  
## 🧰 Tech Stack
- Python (Data Processing)
- Apache Airflow (Orchestration)
- Docker & Docker Compose (Containerization)
- PostgreSQL (Data Warehouse)
- SQL (Transformations)

---

## 🔄 End-to-End Data Flow

1. Extract data from CSV/API sources  
2. Load raw data into staging tables (PostgreSQL)  
3. Trigger Airflow DAGs for orchestration  
4. Apply transformations using Python/SQL  
5. Store processed data in analytics tables  
6. Validate output via database queries  

---

## 🚀 How to Run

```bash
docker-compose up -d

Access Airflow UI:

http://localhost:8080
