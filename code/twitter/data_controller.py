
import json

# loading and storing data to local disk.

cursor = mysql.get_db().cursor()


def load_tweets(filename="27-Nov-2013_04:07:49"):
    """
    Reading data from file and returning those tweets.
    @param filename:
    @return a list of tweets
    """
    tweets = []
    data_file = open(filename)
    for line in data_file.readlines():
        #json_tweet = line.convert.to.object.with.json
        # TODO change to import each tweet directly to an object, not a string.
        tweets.append(line)

    return

#from app import db
#from models import *

#def data():
#    # get 15 tweets and return them
#    create_user()
#    tweets = twtr.search()
#    users = User.query.all()
#    print users[0].username
#    return tweets


#def create_user(term = 'default'):
#    user = User('username1', 'message1')
#    db.session.add(user)
#    db.session.commit()
#    print "Created user"
