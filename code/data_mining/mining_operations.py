from app import db
from models import User
from twitter_integration import twtr


def data():
    # get 15 tweets and return them
    tweets = twtr.search()
    return tweets


def create_user(term = 'default'):
    user = User('username1', 'message1')
    db.session.add(user)
    db.session.commit()
    return "Created user"
