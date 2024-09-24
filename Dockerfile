version: "3.9"

services:
  web:
    build: ./web
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/config
    ports:
      - '8000:8000'
    depends_on:
      - db
  django:
    build:
      context: .
      dockerfile: Dockerfile
    command: "gunicorn config.wsgi:application --bind 0.0.0.0:8000"
    volumes:
      - .:/KinoCMS
    ports:
      - "8001:8000"
    env_file:
      - .env.prod
    depends_on:
      - db
      - redis
    networks:
      - mynetwork
    entrypoint: ["./wait-for-db-and-migrate.sh"]

  celery:
    build:
      context: .
      dockerfile: Dockerfile
    command: ["celery", "-A", "config", "worker", "--loglevel=info"]
    volumes:
      - .:/KinoCMS
    depends_on:
      - redis
      - db
    env_file:
      - .env.prod
    networks:
      - mynetwork

  celery-beat:
    build:
      context: .
      dockerfile: Dockerfile
    command: ["celery", "-A", "config", "beat", "--loglevel=info"]
    volumes:
      - .:/KinoCMS
    depends_on:
      - redis
      - db
    env_file:
      - .env.prod
    networks:
      - mynetwork

  db:
    image: mysql:8.0
    volumes:
      - mysql_data:/var/lib/mysql
      - ./Kino_DB_backup.sql:/docker-entrypoint-initdb.d/dump.sql
    env_file:
      - .env.prod
    ports:
      - "3306:3306"
    networks:
      - mynetwork
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}

  redis:
    image: "redis:alpine"
    volumes:
      - redis_data:/data
    networks:
      - mynetwork

volumes:
  mysql_data:
  redis_data:

networks:
  mynetwork:
