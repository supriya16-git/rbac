FROM python:3.10-slim

RUN pip install --no-cache-dir kubernetes

COPY get_secrets.py /app/get_secrets.py

CMD ["python", "/app/get_secrets.py"]

