FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "day07_serve_model:app", "--host", "0.0.0.0", "--port", "8000"]