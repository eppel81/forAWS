#!/bin/bash

set -e
PROJECT_BASE=/home/ubuntu/web
VENV=$PROJECT_BASE/venv
LOGFILE=$PROJECT_BASE/shared/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3

HOST=127.0.0.1
PORT=8000

HOSTNAME=$(hostname -f)

source $VENV/bin/activate

test -d $LOGDIR || mkdir -p $LOGDIR

export DJANGO_SETTINGS_MODULE=settings.prod

cd $PROJECT_BASE/forAWS
exec gunicorn -w $NUM_WORKERS -b $HOST:$PORT settings.wsgi:application \
        --timeout=600 --log-level=error