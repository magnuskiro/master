from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    message = db.Column(db.String)

    def __init__(self, username, message):
        self.username = username
        self.message = message

    def __unicode__(self):
        return self.username


class Tweet(db.Model):
    id = db.Column(db.BIGINT, primary_key=True)
    tweet = db.Column(db.String)
    polarity = {} #{ 'pos':0, 'neg':0 }

    def __init__(self, id, tweet):
        self.id = id
        self.tweet = tweet
