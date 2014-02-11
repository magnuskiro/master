#!/bin/bash

# todo fix pid file thingy.

echo "old: " `cat pidfile`
rm -rf pidfile

#python manage.py runserver > /dev/null 2>&1 &
python manage.py runserver > server.log 2>&1 &

sleep 1
echo `pidof python` >> pidfile
echo "new: " `cat pidfile`
