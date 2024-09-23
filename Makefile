PROJECT_NAME = KinoCMS
DJANGO_MANAGE = python manage.py
PYTHON = python

# Help
help:
	@echo "Makefile commands:"
	@echo "  help                Show this help message."
	@echo "  migrate             Apply database migrations."
	@echo "  makemigrations      Create new database migrations based on the models."
	@echo "  runserver           Start the Django development server."
	@echo "  shell               Open the Django shell."
	@echo "  test                Run tests."
	@echo "  collectstatic       Collect static files."
	@echo "  createsuperuser     Create a new superuser."
	@echo "  seed_data           Seed the database with fake data."
	@echo "  clean               Remove Python file caches."
	@echo "  install             Install Python dependencies from requirements.txt."
	@echo "  git_push            Add, commit, and push changes to Git."

# Django commands
migrate:
	$(DJANGO_MANAGE) migrate

makemigrations:
	$(DJANGO_MANAGE) makemigrations

runserver:
	$(DJANGO_MANAGE) runserver

shell:
	$(DJANGO_MANAGE) shell

test:
	$(DJANGO_MANAGE) test

collectstatic:
	$(DJANGO_MANAGE) collectstatic --noinput

createsuperuser:
	$(DJANGO_MANAGE) createsuperuser

# Seed the database with fake data
seed_data:
	$(DJANGO_MANAGE) seed_data

# Project setup commands
install:
	pip install -r requirements.txt

# Git commands
git_push:
	@git add .
	@git commit -m "Закомічено оновлення проекту $(PROJECT_NAME)"
	@git push origin main

# Phony targets
.PHONY: help migrate makemigrations runserver shell test collectstatic createsuperuser seed_data install clean git_push
