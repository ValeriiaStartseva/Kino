FROM python:3.11-slim


WORKDIR /KinoCMS

# Встановлюємо pip
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-pip \

COPY requirements.txt /KinoCMS/

RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

COPY . /KinoCMS/

EXPOSE 8000

# Вказуємо команду для запуску Gunicorn з міграціями
CMD ["sh", "-c", "python manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:8000"]
