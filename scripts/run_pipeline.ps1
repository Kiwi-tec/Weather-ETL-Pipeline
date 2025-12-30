$ProjectRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
cd $ProjectRoot

if (!(Test-Path ".\venv")) {
  python -m venv venv
}
.\venv\Scripts\pip install --upgrade pip
.\venv\Scripts\pip install -r .\requirements.txt

Write-Host "==> Running weather pipeline"
.\venv\Scripts\python .\src\pipeline.py

docker compose up -d

docker exec weather_pg psql -U postgres -d weatherdb -c "SELECT COUNT(*) AS rows_in_weather FROM public.weather_hourly;"
docker exec weather_pg psql -U postgres -d weatherdb -c "SELECT * FROM public.weather_daily ORDER BY day_utc DESC LIMIT 5;"
