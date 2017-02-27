#!/bin/bash

set -e
PROJECT_BASE=/home/ubuntu/web
VENV=$PROJECT_BASE/virtualenv
LOGFILE=$PROJECT_BASE/shared/logs/victoria-gunicorn.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=2

HOST=127.0.0.1
PORT=8002

HOSTNAME=$(hostname -f)

source $VENV/bin/activate

test -d $LOGDIR || mkdir -p $LOGDIR

export DJANGO_SETTINGS_MODULE=forAWS.settings.prod

cd $PROJECT_BASE/current
exec gunicorn -w $NUM_WORKERS -b $HOST:$PORT settings.wsgi:application \
        --timeout=600 --log-level=error