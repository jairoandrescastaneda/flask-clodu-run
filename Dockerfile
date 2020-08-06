FROM python:3.7-slim

WORKDIR /app
COPY . /app

RUN pip install -r requeriments.txt
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app