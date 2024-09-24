#FROM python:3.11-slim
#
#WORKDIR /KinoCMS
#
## Install necessary system dependencies including gcc and MySQL client libraries
#RUN apt-get update && \
#    apt-get install -y --no-install-recommends \
#    python3-pip \
#    pkg-config \
#    libmariadb-dev \
#    libmariadb-dev-compat \
#    gcc \
#    build-essential \
#    default-libmysqlclient-dev && \
#    rm -rf /var/lib/apt/lists/*
#
## Copy requirements.txt and install dependencies
#COPY requirements.txt /KinoCMS/
#RUN pip install --no-cache-dir --upgrade pip && \
#    pip install -r requirements.txt
#
## Copy the rest of the application code
#COPY . /KinoCMS/
#
#
## Expose the application port
#EXPOSE 8000
#
## Set the command to start Gunicorn
#CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]


FROM python:3.11-slim

WORKDIR /KinoCMS

# Встановлюємо необхідні системні залежності, включаючи gcc та MySQL клієнтські бібліотеки
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3-pip \
    pkg-config \
    libmariadb-dev \
    libmariadb-dev-compat \
    gcc \
    build-essential \
    default-libmysqlclient-dev \
    default-mysql-client && \
    rm -rf /var/lib/apt/lists/*

# Копіюємо requirements.txt та встановлюємо залежності
COPY requirements.txt /KinoCMS/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

# Копіюємо решту коду додатку
COPY . /KinoCMS/

# Забезпечуємо виконуваний доступ до скрипта очікування
RUN chmod +x /KinoCMS/wait-for-db-and-migrate.sh

# Виставляємо порт додатку
EXPOSE 8000

# Встановлюємо точку входу для запуску скрипта очікування
ENTRYPOINT ["/KinoCMS/wait-for-db-and-migrate.sh"]

# Встановлюємо команду для запуску Gunicorn
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
