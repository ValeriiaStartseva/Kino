# Використовуємо офіційний Python імідж
FROM python:3.11-slim

# Зупиняємо буферизацію Python, щоб одразу отримувати логи
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Встановлюємо системні залежності для mysqlclient
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    default-libmysqlclient-dev \
    libmariadb-dev \
    pkg-config \
    && apt-get clean

# Встановлюємо робочу директорію в контейнері
WORKDIR /KinoCMS

# Копіюємо wait-for-it.sh для очікування сервісів
COPY wait-for-it.sh /KinoCMS/

# Додаємо права на виконання для wait-for-it.sh
RUN chmod +x /KinoCMS/wait-for-it.sh

# Копіюємо файл залежностей
COPY requirements.txt /KinoCMS/

# Оновлюємо pip і встановлюємо залежності з requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копіюємо всі файли проекту в контейнер
COPY . /KinoCMS/

# Відкриваємо порт 8000 для зовнішніх підключень
EXPOSE 8000

# Вказуємо команду для запуску Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
