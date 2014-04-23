import ast
import codecs
from os import listdir
from os.path import isfile, join
import random
import matplotlib.pyplot as plt

__author__ = 'kiro'


trend_base = "/home/kiro/ntnu/master/code/twitter/trend-data/"


def calculate_trend_contribution(classifier, tweet):
    return


def calculcate_polarity_by_day(intra_day):
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
        # disregard special files.
        if filename[0] == "_":
            continue
        # skipping the metadata files.
        if ".meta" in filename:
            continue
        # don't aggregate the trend files, the trend files contains already sorted tweets
        if "trend" in filename:
            trend_files.append(filename)
            continue
        # append filename to list.

    compile_trend(trend_files)

if __name__ == "__main__":
    filename_separation(trend_base)
