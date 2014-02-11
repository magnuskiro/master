from classification import classifier
from models import Tweet
from twitter import data_controller


def create_metadata_objects(tweets):
    return_tweets = []
    for tweet in tweets:
        tweet = Tweet(tweet)
        tweet = classifier.sanitize_tweet(tweet)
        return_tweets.append(tweet)
    return return_tweets


def run_classify():
    """
    Runs the test for the classification algorithms.
    @return: a string for printing.
    """
    print "tweet id | " \
          "first | " \
          "second | " \
          "third | " \
          "forth algorithm"

    tweets = data_controller.load_tweets_from_file()
    tweets = create_metadata_objects(tweets)

    for tweet in tweets:
        print str(tweet.id) + "" \
                              " | " \
                              "A1: " + str(classifier.a1(tweet)) + \
              " | " \
              "A2: " + str(classifier.a2()) + \
              " | " \
              "A3: " + str(classifier.a3()) + \
              " | " \
              "A4: " + str(classifier.a4())


run_classify()