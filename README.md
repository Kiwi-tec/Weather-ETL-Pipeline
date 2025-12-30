# 🌤️ Weather ETL Pipeline
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Airflow 2.9.2](https://img.shields.io/badge/Airflow-2.9.2-017CEE?logo=apache-airflow&logoColor=white)](https://airflow.apache.org/)
[![AWS RDS](https://img.shields.io/badge/AWS_RDS-PostgreSQL-FF9900?logo=amazon-aws&logoColor=white)](https://aws.amazon.com/rds/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)

An automated, containerized data pipeline that orchestrates real-time weather data extraction from the OpenWeatherMap API into an AWS RDS PostgreSQL instance.

---

## 🚀 Overview
This project demonstrates a production-grade ETL (Extract, Transform, Load) workflow orchestrated by **Apache Airflow**. By utilizing **Docker Compose**, the entire environment is easily reproducible, ensuring consistent data processing from API to Cloud Storage.


### ✨ Key Features
* **Automated Extraction:** Scheduled pulls from OpenWeatherMap API for localized data.
* **Data Transformation:** Schema mapping and data cleaning using Python and Pandas.
* **Cloud Integration:** Secure data loading and "upsert" operations into **AWS RDS**.
* **Monitoring:** Integrated logging and task status tracking via the Airflow UI.

---

## 🛠️ Tech Stack
* **Orchestration:** Apache Airflow 2.9.2 (Dockerized)
* **Language:** Python 3.12
* **Database:** AWS RDS (PostgreSQL 16)
* **Infrastructure:** Docker & Docker Compose

---

## 📁 Project Structure
```text
WEATHER_PROJECT/
├── dags/               # Airflow DAG logic (weather_etl.py)
├── sql/                # SQL schema definitions (weather_schema.pgsql)
├── src/                # Core ETL logic (pipeline.py, util_db.py)
├── docker-compose.yml  # Container orchestration
├── requirements.txt    # Python dependencies
└── .env                # Local credentials (not tracked)

Environment Setup: Create a .env file with your PG_HOST, PG_USER, and PG_PASSWORD.

Run Containers: Execute docker compose up --build -d to start the Airflow environment.

Access Airflow: Open http://localhost:8080 (Credentials: admin/admin).
