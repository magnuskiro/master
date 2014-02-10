import codecs
import os
import random
from models import *
import ast
from twitter.mining_operations import cursor_extraction

# loading and storing data to local disk.
#cursor = mysql.get_db().cursor()

#base = "./twitter/"
base = "/home/kiro/ntnu/master/code/twitter/"
default_data_set = "testset"


def load_tweets_from_file(filename=default_data_set):
    """
    Reading data from file and returning those tweets.
    @param filename:
    @return a list of tweets
    """
    tweets = []
    data_file = open(base + filename)
    for line in data_file.readlines():
        # 'ast.literal_eval(line)' interprets the json tweet string as a dictionary.
        tweets.append(ast.literal_eval(line))
    return tweets


def get_random_tweet():
    """
    returns a randomly selected tweet metadata object.
    @return: a tweet metadata object.
    """
    tweets = Tweet.query.all()
    tweet = random.choice(tweets)
    return tweet

def get_random_unclassified_tweet():
    """
    returns the first unclassified tweet metadata object.
    @return: a tweet metadata object.
    """
    return Tweet.query.filter_by(manual_polarity=None).first()

def save_tweet(tweet):
    """
    stores a tweet object to the database.
    @param tweet: a tweet metadata obejct.
    @return: nothing.
    """
    if isinstance(tweet, Tweet):
        # if the tweet metadata object already exists, delete it
        if Tweet.query.get(tweet.id):
            db.session.delete(tweet)
        # save tweet metadata object to db.
        db.session.add(tweet)
        db.session.commit()
    else:
        print "not a tweet metadata object: "
        #print "not a tweet metadata object: ", str(tweet)
    return


def get_data_set_names():
    """
    Creates a list of the names of the data sets we have now.
    @return: a list of data sets.
    """
    datasets = []
    for filename in sorted(os.listdir(base)):
        if "dataset-" in filename and not ".meta" in filename:
            metadata = get_metadata(filename)
            #print metadata
            set = {"name": unicode(filename), "metadata": metadata}
            datasets.append(set)
    return datasets


def get_metadata(filename):
    """
    Returns a  dictionary with the metadata for a given dataset.
    @param filename: the file the metadata should be retrieved from.
    @return: the content of the file in a dictionary.
    """
    metadata = {}
    if os.path.isfile(base + filename + ".meta"):
        for line in codecs.open(base + filename + ".meta", "r", "utf-8"):
            line.strip("\n")
            line = line.split(":")
            metadata[line[0]] = line[1]
    else:
        metadata['query'] = "There was an error in loading the metadata file."
    return metadata


def create_new_data_set(query, count=2000):
    """
    Calls the mining operations to create a new set of tweet defined by the query input argument.
    @param query: the search terms that define the
    @param count: the amount of tweets wanted in the new dataset.
    @return:
    """
    cursor_extraction(query, count)
    return


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
