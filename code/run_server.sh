#!/bin/bash


echo "old: " `cat pidfile`
rm -rf pidfile

#python manage.py runserver > /dev/null 2>&1 &
python manage.py runserver > server.log 2>&1 &
echo $! >> pidfile
echo "new: " `cat pidfile`
