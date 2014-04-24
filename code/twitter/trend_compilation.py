import codecs
from os import listdir
from os.path import isfile, join
import random
import matplotlib.pyplot as plt
from trend_tweet_sorting import do_tweet_trend_sorting

__author__ = 'kiro'


trend_base = "/home/kiro/ntnu/master/code/twitter/trend-data/"


def calculate_trend_contribution(classifier, tweet):
    # todo finish
    return


def calculcate_polarity_by_day(intra_day):
    # todo finish
    pass


def compile_trend(trend_files):

    classifier = []  # todo import trained classifier from classification code.
    trend = []

    # get all previously observed tweets.
    # for all trend files
    for filename in trend_files:
        lines = codecs.open(trend_base + filename, 'r', "utf-8")
        # for all lines in file
        intra_day = []
        for line in lines.readlines():
            # calculate tweet trend contribution. aka Polarity of a tweet.
            #intra_day.append(calculate_trend_contribution(classifier, ast.literal_eval(line)))
            intra_day.append(random.random()*10)
        # calculate the polarity of given day based on input tweets.
        #trend.append(["-".join(filename.split("-")[1:]), calculcate_polarity_by_day(intra_day)])
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

if __name__ == "__main__":
    # do the tweet sorting, in case we have new tweets not sorted.
    do_tweet_trend_sorting(trend_base)
    # start the trend compiling
    do_tweet_trend_compiling(trend_base)