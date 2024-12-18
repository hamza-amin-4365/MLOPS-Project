FROM python:3.9-slim-buster

RUN apt-get update -y && apt-get install -y awscli  # Ensure awscli is installed if needed
RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt . # Copy requirements first for caching
RUN pip install -r requirements.txt

COPY . .  # Copy the rest of the application code

CMD ["python3", "app.py"]