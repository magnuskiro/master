
import ast
import codecs
from os import listdir
from os.path import isfile, join
from mining_utils import write_array_entries_to_file

__author__ = 'kiro'

trend_base = "/home/kiro/ntnu/master/code/twitter/trend-data/"


def sort_tweets_on_date(feature_files, trend_files):
    """
    @param feature_files: all files containing unsorted tweets.
    @param trend_files: files containing already sorted tweets.
    @return: nothing
    """
    trend_tweets = []

    # get all previously observed tweets.
    # for all trend files
    for filename in trend_files:
        lines = codecs.open(trend_base + filename, 'r', "utf-8")
        # for all lines in file
        for line in lines.readlines():
            trend_tweets.append(line)

    #trend = { date : [tweet, tweet] }
    trend = {}
    # for all feature files:
    for filename in feature_files:
        lines = codecs.open(trend_base + filename, 'r', "utf-8")
        for l in lines.readlines():
            # if we don't have the tweet already:
            if l not in trend_tweets:
                line = ast.literal_eval(l)
                # get the key for this tweet, it's the date of creation
                key = "-".join(line['created_at'].split(" ")[1:3])
                if key not in trend.keys():
                    trend[key] = []
                trend[key].append(line)

    # write tweets to file.
    for key in trend.keys():
        write_array_entries_to_file(trend[key], trend_base + "trend-"+key, "w")
    return


def filename_separation(folder):
    """
    Run trend file compilation with all wanted files in the folder.
    @param folder: the folder containing tweet files.
    """
    files = [f for f in listdir(folder) if isfile(join(folder, f))]
    trend_files = []
    feature_files = []
    files.sort().reverse()
    for filename in files:
        #
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
        feature_files.append(filename)

    sort_tweets_on_date(feature_files, trend_files)

if __name__ == "__main__":
    filename_separation(trend_base)
