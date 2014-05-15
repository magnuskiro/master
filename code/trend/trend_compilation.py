import ast
import codecs
from os import listdir
from os.path import isfile, join
import random
from sklearn.svm import LinearSVC

import matplotlib.pyplot as plt
from nltk import SklearnClassifier

from trend_classification_utils import extract_features_from_text, initialize_classifier, load_manually_labeled_tweets
import urllib

__author__ = 'kiro'


trend_base = "/home/kiro/ntnu/master/code/trend/trend-data/"


def calculate_tweet_contribution_to_trend(classifier, tweet):
    # todo finish
    classifier.classify(extract_features_from_text(tweet))
    return


def calculate_polarity_by_day(intra_day):
    # todo finish
    pass

# for tweets in this day
    # classify pos/neg
    # value of day += value of tweet * popularity(the value that represents the spreading or what not of a tweet).
    # return pos, neg, trend value

# for all days
    #create a dict containing:
    #pos
    #neg
    #graph plot point / trend value.
    #stock closing value.
    #stock volume.
    #calculate moving average for plotting.


def get_calssifier():
    tweet_file = "tweets_classified_manually"
    classification_base = "/home/kiro/ntnu/master/code/classification/"
    tweets = load_manually_labeled_tweets(classification_base + tweet_file)
    classifier_class = SklearnClassifier(LinearSVC())
    # instantiate the classifier
    classifier = initialize_classifier(classifier_class, tweets)
    print "Info -- Classifier initialize."
    return classifier


def compile_trend(trend_files):

    classifier = get_calssifier()
    trend = []

    # get all previously observed tweets.
    # for all trend files
    for filename in trend_files:
        lines = codecs.open(trend_base + filename, 'r', "utf-8")
        # for all lines in file
        intra_day = []
        for line in lines.readlines():
            # calculate tweet trend contribution. aka Polarity of a tweet.

            calculate_tweet_contribution_to_trend(classifier, ast.literal_eval(line))
            #intra_day.append(calculate_tweet_contribution_to_trend(classifier, ast.literal_eval(line)))
            intra_day.append(random.random()*10)
        # calculate the polarity of given day based on input tweets.
        #trend.append(["-".join(filename.split("-")[1:]), calculate_polarity_by_day(intra_day)])
        trend = [i for i in intra_day]

    x = [i for i in range(0, len(trend))]
    plt.plot(x, trend)
    plt.show()
    return


def filename_separation(folder):
    """
    Run trend file compilation with all wanted files in the folder.
    @param folder: the folder containing tweet files.
    """
    files = [f for f in listdir(folder) if isfile(join(folder, f))]
    trend_files = []
    files.sort()
    for filename in files:
        # if it's a file we want append it to list of files.
        if "trend" in filename:
            trend_files.append(filename)
            continue

    compile_trend(trend_files)


def do_tweet_trend_compiling(folder):
    """
    Run the trend tweet sorting.
    @param folder: name of the directory to find trend files containing tweets.
    """
    print "Info -- Creating trend."
    filename_separation(folder)


def get_stock_exhange_values(url):
    # get the stock exchange data from oslo bors.
    stock_exchange_history = urllib.urlopen(url).readlines()
    for record in stock_exchange_history:
        # earlier records are not interesting.
        if "20140411" in record:
            break
        print record


if __name__ == "__main__":
    # do the tweet sorting, in case we have new tweets not sorted.
    #do_tweet_trend_sorting(trend_base)
    # start the trend compiling
    #do_tweet_trend_compiling(trend_base)
    get_stock_exhange_values('http://www.netfonds.no/quotes/paperhistory.php?paper=OSEBX.OSE&csv_format=csv')