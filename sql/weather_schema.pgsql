CREATE TABLE IF NOT EXISTS public.weather_hourly(
    location TEXT NOT NULL,
    ts TIMESTAMPTZ NOT NULL,
    temp_c NUMERIC(6,2),
    humidity_pct NUMERIC(5,2),
    wind_kph NUMERIC(7,2),
    precip_mm NUMERIC(6,2),
    PRIMARY KEY (location, ts)
);

CREATE OR REPLACE VIEW public.weather_daily AS
SELECT
  location,
  date_trunc('day', ts AT TIME ZONE 'UTC')::date AS day_utc,
  ROUND(AVG(temp_c), 2) AS avg_temp_c,
  ROUND(MAX(temp_c), 2) AS max_temp_c,
  ROUND(MIN(temp_c), 2) AS min_temp_c,
  ROUND(AVG(humidity_pct), 2) AS avg_humidity_pct,
  ROUND(SUM(precip_mm), 2) AS total_precip_mm
FROM public.weather_hourly
GROUP BY 1,2;


