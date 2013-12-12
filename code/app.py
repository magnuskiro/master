
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

host = "localhost"
username = "tweetrend"
password = "KhJ587mwCWvzsvCD"
database = "tweetrend"

app = Flask(__name__, static_url_path="/static")
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/kiro/ntnu/master/code/db/db.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + username + ':' + password + '@' + host + '/' + database
db = SQLAlchemy(app)
