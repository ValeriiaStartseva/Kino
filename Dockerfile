FROM python:3.11-slim

WORKDIR /KinoCMS

# Install necessary system dependencies, including gcc and MySQL client libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    pkg-config \
    libmariadb-dev \
    libmariadb-dev-compat \
    gcc \
    build-essential \
    default-libmysqlclient-dev \
    default-mysql-client && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install dependencies
COPY requirements.txt /KinoCMS/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the application code
COPY . /KinoCMS/

# Expose the application port
EXPOSE 8000

# Set the command to perform migrations and start Gunicorn
CMD ["sh", "-c", "python manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:8000"]
