#!/usr/bin/env bash
# exit on error
set -o errexit


pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py shell -c "from django.contrib.auth.models import User; \
                           User.objects.filter(username='admin1').exists() or \
                           User.objects.create_superuser('admin1',
                           'admin1@example.com', 'admin1')"
python manage.py migrate
