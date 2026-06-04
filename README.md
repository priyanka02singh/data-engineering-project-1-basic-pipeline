# Modern ELT Pipeline (Project 1)

## 📌 Overview
This project demonstrates a simplified end-to-end ELT pipeline using Python, Airflow, Docker, and PostgreSQL. It simulates real-world data engineering workflows including ingestion, orchestration, transformation, and loading into a structured database.

The goal of this project is to showcase production-style data pipeline design using modular components and workflow orchestration.

---

## 🏗️ Architecture

The pipeline consists of:

### 1. Data Ingestion Layer
- Extracts data using Python scripts
- Loads raw data into PostgreSQL

### 2. Orchestration Layer
- Apache Airflow manages workflow execution
- DAGs handle task dependencies and scheduling

### 3. Transformation Layer
- Data cleaning and preprocessing
- Structured transformation logic applied before loading

### 4. Storage Layer
- PostgreSQL used as the analytical database

---

## 🧰 Tech Stack
- Python
- Apache Airflow
- Docker & Docker Compose
- PostgreSQL
- SQL

---

## 🔄 Workflow

1. Extract raw data (CSV/API)
2. Load into staging tables
3. Transform data using Python/SQL logic
4. Store processed data in PostgreSQL
5. Orchestrate using Airflow DAGs

---

## 📁 Project Structure
airflow/dags/ → Airflow DAGs
docker-compose.yml → Infrastructure setup
.gitignore → Ignored files configuration

---

## 🚀 How to Run

```bash
docker-compose up -d

Access Airflow UI:

http://localhost:8080
