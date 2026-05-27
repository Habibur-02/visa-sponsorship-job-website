FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Seed on first run if DB doesn't exist, then start server
CMD ["sh", "-c", "[ -f /app/data/visa_jobs.db ] || (DB_PATH=/app/data/visa_jobs.db python seed.py); DB_PATH=/app/data/visa_jobs.db uvicorn main:app --host 0.0.0.0 --port 8001"]
