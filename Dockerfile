# Використовуємо офіційний Python імідж
FROM python:3.11-slim

# Зупиняємо буферизацію Python, щоб одразу отримувати логи
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Встановлюємо робочу директорію в контейнері
WORKDIR /KinoCMS

# Копіюємо файл залежностей
COPY requirements.txt /KinoCMS/

# Оновлюємо pip і встановлюємо залежності
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копіюємо всі файли проекту в контейнер
COPY . /KinoCMS/

# Відкриваємо порт 8000 для зовнішніх підключень
EXPOSE 8000

# Вказуємо команду для запуску Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "KinoCMS.wsgi:application"]
