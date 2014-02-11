db='./db/db.db'

rm -rf $db 
touch $db
chmod 755 $db
python manage.py create_db

