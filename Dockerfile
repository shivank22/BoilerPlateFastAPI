FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
    && pip install fastapi uvicorn sqlalchemy psycopg2-binary toml alembic

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]