#!/bin/sh
python manage.py migrate --no-input
python manage.py collectstatic --no-input
exec gunicorn \
    --worker-class gevent \
    --workers 2 \
    --bind 0.0.0.0:8000 \
    siteathlets.wsgi:application
