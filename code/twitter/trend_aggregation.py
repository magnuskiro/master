
import ast
import codecs
from os import listdir
from os.path import isfile, join
from mining_utils import write_array_entries_to_file

__author__ = 'kiro'

trend_base = "/home/kiro/ntnu/master/code/twitter/trend-data/"


def sort_trend_tweets_on_date(filename):
    """
    Compiles files of tweets with the same date based on the input file.
    @param filename: the file containing mined tweets.
    """
    #trend = { date : [tweet, tweet] }
    trend = {}

    lines = codecs.open(trend_base + filename, 'r', "utf-8")
    # for all tweets write them to correct date file
    for line in lines.readlines():
        #print line
        # get the time this tweet was created.
        time = ast.literal_eval(line)['created_at']
        # get the filename for this tweet
        filename = "-".join(time.split(" ")[1:3])
        if filename not in trend.keys():
            trend[filename] = []
        # add tweet to correct date array
        trend[filename].append(line)

    # add unique tweets trend file.
    # for all date files.
    for key in trend.keys():
        if isfile(trend_base + filename):
            lines = codecs.open(trend_base + filename, 'r', "utf-8")
            # for all lines in key file
            for line in lines.readlines():
                # for all tweet in
                for tweet in trend[key]:
                    # if the id's match
                    if tweet[id] == ast.literal_eval(line)['id']:
                        # remove duplicate tweet from list.
                        trend[key].remove(tweet)
            # append current array of tweets to it's designated file.
            write_array_entries_to_file(trend[key], trend_base + "trend-"+key, "a")
        else:
            # write current array of tweets to it's designated file.
            write_array_entries_to_file(trend[key], trend_base + "trend-"+key, "w")


def run_aggregation(folder):
    """
    Run trend file compilation with all wanted files in the folder.
    @param folder: the folder containing tweet files.
    """
    files = [f for f in listdir(folder) if isfile(join(folder, f))]
    files.sort()
    for filename in files:
        #
        if filename[0] == "_":
            continue
        # skipping the metadata files.
        if ".meta" in filename:
            continue
        # don't aggregate the trend files, the trend files contains already sorted tweets
        if "trend" in filename:
            continue
        print filename
        sort_trend_tweets_on_date(filename)

if __name__ == "__main__":
    run_aggregation(trend_base)
