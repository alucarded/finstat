#!/bin/sh
export PYTHONPATH="${PYTHONPATH}:$(pwd)/../../finstat_libs"
python3 manage.py runserver
