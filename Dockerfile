FROM python:3.11-slim

WORKDIR /app

# Install MySQL drivers and cryptography (required for MySQL 8.4)
RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy pymysql cryptography

COPY . .

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

