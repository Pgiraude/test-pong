#!/bin/bash

cd /app

export PYTHONPATH=$PWD

# # wait for Postgre to be ready
# until nc -z $SQL_HOST $SQL_PORT; do
#     echo "Postgre is unavailable - sleeping"
#     sleep 1
# done
# echo "Postgre is available !"

echo "## INFO : Launching Django app"

# This will reset the database each time the container is launched
python manage.py flush --no-input 
python manage.py migrate

python manage.py runserver 0.0.0.0:8000
exit $?