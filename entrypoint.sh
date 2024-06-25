#!/bin/bash

set -e

source /env/bien/activate

if [$1 == 'gunicorn']; then

    exec gunicorn portfolio.wsgi:application -b 0.0.0.0:8000

else

    exec python manage.py runserver 0.0.0.0:8000


fi