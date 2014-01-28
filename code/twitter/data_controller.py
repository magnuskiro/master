import os
from models import *
import ast

# loading and storing data to local disk.
#cursor = mysql.get_db().cursor()

default_data_set = "testset"

def load_tweets(filename=default_data_set):
    """
    Reading data from file and returning those tweets.
    @param filename:
    @return a list of tweets
    """
    tweets = []
    base = "/home/kiro/ntnu/master/code/twitter/"
    data_file = open(base+filename)
    for line in data_file.readlines():
        # 'ast.literal_eval(line)' interprets the json tweet string as a dictionary.
        tweets.append(ast.literal_eval(line))
    return tweets


def get_one_tweet():
    tweet = load_tweets(default_data_set)[1]
    # todo get random tweet object from database.

    return tweet


def save_tweet(tweet):
    """

    @param tweet:
    @return:
    """
    # todo store tweets to database.
    print tweet
    db.session.add(tweet)
    db.session.commit()
    return


def get_dataset_names():
    datasets = []
    path = "./twitter/"
    for filename in os.listdir(path):
        if "dataset-" in filename and not ".meta" in filename:
            metadata = get_metadata(path+filename)
            print metadata
            set = { "name" : filename, "metadata" : metadata}
            datasets.append(set)
    return datasets

def get_metadata(filename):
    metadata = {}
    for line in open(filename+".meta"):
        line.strip("\n")
        line = line.split(":")
        metadata[line[0]] = line[1]
    return metadata

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
