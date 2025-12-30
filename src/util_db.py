import os
import psycopg
from psycopg import sql

def get_conn():
    return psycopg.connect(
        host = os.getenv("PG_HOST"),
        port = os.getenv("PG_PORT"),
        dbname = os.getenv("PG_DB"),
        user = os.getenv("PG_USER"),
        password = os.getenv("PG_PASSWORD"),
        autocommit=True
    )

def run_sql_file(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        sql_text = f.read()
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql_text) # type: ignore[arg-type]

def upsert_weather(rows)-> int:
    if not rows:
        return 0
    cols = ["location","ts","temp_c","humidity_pct","wind_kph","precip_mm"]
    values = [[r.get(c) for c in cols] for r in rows]
    insert_sql = f"""
        INSERT INTO public.weather_hourly ({','.join(cols)})
        VALUES ({','.join(['%s']*len(cols))})
        ON CONFLICT (location, ts) DO UPDATE SET
            temp_c = EXCLUDED.temp_c,
            humidity_pct = EXCLUDED.humidity_pct,
            wind_kph = EXCLUDED.wind_kph,
            precip_mm = EXCLUDED.precip_mm;
    """
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.executemany(insert_sql, values) # type: ignore[arg-type]
            return cur.rowcount

