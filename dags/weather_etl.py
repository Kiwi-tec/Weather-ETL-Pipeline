from datetime import timedelta
import time
import sys
from pathlib import Path
from dotenv import load_dotenv

# Make your project importable
sys.path.insert(0, "/opt/project/src")
sys.path.insert(0, "/opt/project")

# Load env vars for util_db.get_conn() and pipeline
# This is necessary because your custom code uses os.environ variables
load_dotenv("/opt/project/.env") 

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator

from src.pipeline import main as run_pipeline
from src.util_db import get_conn, run_sql_file # uses psycopg & your .env

def apply_schema_fn():
    schema_path = Path("/opt/project/sql/weather_schema.pgsql")
    run_sql_file(str(schema_path))

def sanity_check_fn():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM public.weather_hourly;")
            rows = cur.fetchone()[0]
            print(f"rows_in_weather = {rows}")

default_args = {
    "owner": "data",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="weather_etl",
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval="@daily",
    catchup=False,
    tags=["weather"],
) as dag:
    # All tasks MUST be defined here
    apply_schema = PythonOperator(
        task_id="apply_schema",
        python_callable=apply_schema_fn,
    )

    run_etl = PythonOperator(
        task_id="run_pipeline",
        python_callable=run_pipeline, # calls your src/pipeline.py:main()
    )

    sanity_check = PythonOperator(
        task_id="sanity_check",
        python_callable=sanity_check_fn,
    )

    # Set the dependency chain
    apply_schema >> run_etl >> sanity_check