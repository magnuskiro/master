from app import db
from models import *
from twitter_integration import twtr


def data():
    # get 15 tweets and return them
    create_user()
    tweets = twtr.search()
    users = User.query.all()
    print users[0].username
    return tweets


def create_user(term = 'default'):
    user = User('username1', 'message1')
    db.session.add(user)
    db.session.commit()
    print "Created user"
