FROM python:3.10-slim

WORKDIR /app

COPY my_app.py .

CMD ["python", "my_app.py"]