import os
import datetime as dt
from pathlib import Path
import pandas as pd
import requests
from dotenv import load_dotenv
from util_db import run_sql_file, upsert_weather

load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")

LOCATION = os.getenv("LOCATION_NAME")
LAT = os.getenv("LAT")
LON = os.getenv("LON")
TZ = os.getenv("TIMEZONE")

def fetch_open_meteo(lat, lon, tz):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation",
        "timezone": tz,
        "past_days": 2
    }
    r = requests.get(url, params=params, timeout=30)
    r.raise_for_status()
    return r.json()

def normalize(payload, location):
    hourly = payload.get("hourly", {})
    df = pd.DataFrame({
        "ts": pd.to_datetime(hourly.get("time", []), utc=True),
        "temp_c": hourly.get("temperature_2m", []),
        "humidity_pct": hourly.get("relative_humidity_2m", []),
        "wind_kph": hourly.get("wind_speed_10m", []),
        "precip_mm": hourly.get("precipitation", []),
    })
    df["location"] = location
    return df

def main():
    schema_path = Path(__file__).resolve().parents[1] / "sql" / "weather_schema.pgsql"
    run_sql_file(str(schema_path))

    payload = fetch_open_meteo(LAT, LON, TZ)
    df = normalize(payload, LOCATION)
    rows = df.to_dict(orient="records")
    n = upsert_weather(rows)
    print(f"Upserted {n} rows for {LOCATION}")

if __name__ == "__main__":
    main()
