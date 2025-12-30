🌤️ Weather ETL Pipeline
An automated data pipeline orchestrating real-time weather data extraction from the OpenWeatherMap API into an AWS RDS PostgreSQL instance.

🚀 Overview
This project demonstrates a production-ready ETL workflow orchestrated by Apache Airflow. It is fully containerized using Docker Compose to ensure a consistent environment for data extraction, transformation, and cloud loading.

Key Features
Extraction: Automated calls to OpenWeatherMap API for localized data.

Transformation: Data cleaning and schema mapping using Python and Pandas.

Loading: Secure storage and "upsert" operations in a remote AWS RDS (PostgreSQL) database.

🛠️ Tech Stack
Orchestration: Apache Airflow 2.9.2

Language: Python 3.12

Database: AWS RDS (PostgreSQL 16)

Infrastructure: Docker & Docker Compose

📁 Project Structure

WEATHER_PROJECT/
├── dags/               # Airflow DAG (weather_etl.py)
├── sql/                # SQL schema (weather_schema.pgsql)
├── src/                # ETL logic (pipeline.py, util_db.py)
├── docker-compose.yml  # Container orchestration
├── requirements.txt    # Python dependencies
└── .env                # Local secrets (not tracked in Git)
⚙️ Quick Start
Clone the Repo: git clone <your-repo-url>

Environment Setup: Create a .env file with your PG_HOST, PG_USER, and PG_PASSWORD.

Run Containers: Execute docker compose up --build -d to start the Airflow environment.

Access Airflow: Open http://localhost:8080 (Credentials: admin/admin).