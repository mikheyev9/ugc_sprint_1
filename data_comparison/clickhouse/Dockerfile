FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY clickhouse_research.py .

CMD ["python", "clickhouse_research.py"]