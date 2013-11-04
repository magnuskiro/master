from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path="/static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/kiro/ntnu/master/code/db/db.db'
db = SQLAlchemy(app)
