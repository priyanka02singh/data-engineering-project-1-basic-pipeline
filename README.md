# Modern ELT Pipeline (Project 1)

## 📌 Problem Statement
Modern data systems require reliable pipelines to extract raw data from multiple sources, transform it into structured formats, and load it into analytical databases for downstream use.

This project simulates a real-world ELT pipeline that demonstrates how raw data flows through ingestion, orchestration, transformation, and storage layers using industry-standard tools.

---

## 🏗️ System Architecture


CSV / API Sources
↓
Python Ingestion Layer
↓
PostgreSQL (Raw/Staging Tables)
↓
Airflow Orchestration (DAGs)
↓
Transformation Layer (Python + SQL)
↓
Analytics Tables (PostgreSQL)


---

## ⚙️ Pipeline Components

### 1. Data Ingestion Layer
- Extracts data from CSV files and APIs
- Loads raw data into PostgreSQL staging tables

### 2. Orchestration Layer (Airflow)
- Manages workflow execution using DAGs
- Ensures task dependencies and scheduling
- Handles retries and monitoring via Airflow UI

### 3. Transformation Layer
- Cleans and standardizes raw data
- Performs SQL-based transformations
- Prepares analytics-ready datasets

### 4. Storage Layer
- PostgreSQL used as the central data warehouse
- Stores both raw and transformed datasets

---

## 🧰 Tech Stack
- Python
- Apache Airflow
- Docker & Docker Compose
- PostgreSQL
- SQL

---

## 🔄 End-to-End Data Flow

1. Extract data from CSV/API sources  
2. Load raw data into staging tables (PostgreSQL)  
3. Trigger Airflow DAGs for orchestration  
4. Apply transformations using Python/SQL  
5. Store processed data in analytics tables  
6. Validate output via database queries  

---

## 📁 Project Structure

airflow/dags/ → Airflow workflow definitions
docker-compose.yml → Infrastructure setup (Airflow + Postgres)
.gitignore → File exclusion rules


---

## 🚀 How to Run

```bash
docker-compose up -d

Access Airflow UI:

http://localhost:8080
