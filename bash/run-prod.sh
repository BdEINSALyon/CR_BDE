#!/bin/sh
yes yes | export -p > /tmp/env.txt && python3 manage.py migrate && python3 manage.py crontab add && service cron start && gunicorn CR_BDE.wsgi -b 0.0.0.0:8000 --log-file -
