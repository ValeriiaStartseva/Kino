#!/bin/bash
# Wait until MySQL is ready
while ! mysqladmin ping -h"$DB_HOST" --silent; do
    echo "Waiting for database connection..."
    sleep 2
done

# Run migrations
python manage.py migrate

# Start Gunicorn
exec "$@"
