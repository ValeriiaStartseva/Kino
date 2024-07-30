PROJECT_NAME = KinoCMS
DJANGO_MANAGE = python manage.py
PYTHON = python

# Help
help:
	@echo "Makefile commands:"
	@echo "  help                Show this help message."
	@echo "  migrate             Apply database migrations."
	@echo "  make migrations      Create new database migrations based on the models."
	@echo "  runserver           Start the Django development server."
	@echo "  shell               Open the Django shell."
	@echo "  test                Run tests."
	@echo "  collectstatic       Collect static files."
	@echo "  createsuperuser     Create a new superuser."
	@echo "  clean               Remove Python file caches."
	@echo "  install             Install Python dependencies from requirements.txt."

# Django commands
migrate:
	$(DJANGO_MANAGE) migrate

makemigrations:
	$(DJANGO_MANAGE) make migrations

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

# Project setup commands
install:
	pip install -r requirements.txt

# Phony targets
.PHONY: help migrate makemigrations runserver shell test collectstatic createsuperuser install clean
