FROM python:3.10

WORKDIR /app

COPY factorial.py .

CMD ["python", "factorial.py"]