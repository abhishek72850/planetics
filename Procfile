release: python manage.py migrate
web: gunicorn planetics.wsgi --log-file -
worker: celery -A planetics worker --beat --events --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler