
from classification import word_count_classification
import data_controller
from models import Tweet


def create_metadata_objects(tweets):
    return_tweets = []
    for tweet in tweets:
        tweet = Tweet(tweet)
        tweet = word_count_classification.sanitize_tweet(tweet)
        return_tweets.append(tweet)
    return return_tweets


def run_classify(dataset):
    """
    Runs the test for the classification algorithms.
    @return: a string for printing.
    """
    print "tweet id | " \
          "first | " \
          "second | " \
          "third | " \
          "forth algorithm"

    tweets = data_controller.load_tweets_from_file(dataset)
    tweets = create_metadata_objects(tweets)

    for tweet in tweets:
        print str(tweet.id) + "" \
                              " | " \
                              "A1: " + str(word_count_classification.positive_vs_negative_words_classification(tweet)) + \
              " | " \
              "A2: " + str(word_count_classification.word_count_classification()) + \
              " | " \
              "A3: " + str(word_count_classification.a3()) + \
              " | " \
              "A4: " + str(word_count_classification.bigram_classification())

run_classify("dataset-testset")