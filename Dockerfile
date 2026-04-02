FROM python:3.10-slim
WORKDIR /app
COPY factorial.py .
CMD ["python", "factorial.py"]