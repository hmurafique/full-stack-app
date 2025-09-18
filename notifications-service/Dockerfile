FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 7200
CMD ["gunicorn", "-b", "0.0.0.0:7200", "app:app"]
