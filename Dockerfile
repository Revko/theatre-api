FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
COPY wait_for_db.py .

CMD ["sh", "-c", "python wait_for_db.py && python manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:8000"]
