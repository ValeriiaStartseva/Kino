FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /KinoCMS

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libmariadb-dev-compat \
    libmariadb-dev \
    pkg-config \
    default-libmysqlclient-dev \
    curl \
    && apt-get clean

# Copy requirements file
COPY requirements.txt //

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /KinoCMS/

# Create a Celery user and set permissions
RUN useradd -ms /bin/bash celery_user && chown -R celery_user:celery_user /KinoCMS

# Expose Django port
EXPOSE 8000

# Start Gunicorn server (Django)
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
