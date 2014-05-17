import ast
import codecs
from os import listdir
from os.path import isfile, join
from mining_utils import write_array_entries_to_file

__author__ = 'kiro'

trend_base = "/home/kiro/ntnu/master/code/trend/trend-data/"


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
        print filename
        lines = codecs.open(trend_base + filename, 'r', "utf-8")
        # for all tweets in this feature_file
        for l in lines.readlines():
            # if we don't have the tweet already:
            if l not in trend_tweets:
                line = ast.literal_eval(l)
                # get the key for this tweet, it's the date of creation
                key = "-".join(line['created_at'].split(" ")[1:3])
                # if new key, create the array for that key
                if key not in trend.keys():
                    trend[key] = []
                # append tweet to date.
                trend[key].append(line)

    # write tweets to file.
    for key in trend.keys():
        write_array_entries_to_file(trend[key], trend_base + "trend-" + key, "w")
    return


def remove_norwegian(feature_files):
    """
    Ignoring norwegian specific tweets on sort.
    @param feature_files:
    @return:
    """
    base = "/home/kiro/ntnu/master/code/trend/"
    filename = "_search-terms-norwegian"

    norwegian_terms = [line.strip().lower() for line in
                       codecs.open(base + filename, 'r', "utf-8").readlines()]
    result = []
    for term in feature_files:
        if term not in norwegian_terms:
            result.append(term)

    #print result, len(result)
    return result


def filename_separation(folder):
    """
    Run trend file compilation with all wanted files in the folder.
    @param folder: the folder containing tweet files.
    """
    files = [f for f in listdir(folder) if isfile(join(folder, f))]
    trend_files = []
    feature_files = []
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
        feature_files.append(filename)

    feature_files = remove_norwegian(feature_files)

    sort_tweets_on_date(feature_files, trend_files)


def do_tweet_trend_sorting(folder):
    """
    Run the trend tweet sorting.
    @param folder: name of the directory to find trend files containing tweets.
    """
    print "Info -- Sorting trend tweets to dates."
    filename_separation(folder)


def language_elimination(folder):
    #iso_language_code = no or en
    """
    Remove tweets of languages we cannot use.
    @param folder: the folder containing files containing tweets to look through.
    """
    files = [f for f in listdir(folder) if isfile(join(folder, f))]
    for filename in files:
        if ".meta" in filename:
            continue
        # don't aggregate the trend files, the trend files contains already sorted tweets
        if "trend" in filename:
            continue
        print filename
        lines = [ast.literal_eval(tweet) for tweet in
                 codecs.open(trend_base + filename, 'r', "utf-8").readlines()]
        tweets = []
        for line in lines:
            lang = line['metadata']['iso_language_code']
            if lang == "en" or lang == "no":
                tweets.append(line)
                #print line['metadata']['iso_language_code']
        write_array_entries_to_file(tweets, trend_base + filename)

if __name__ == "__main__":
    #language_elimination(trend_base)
    do_tweet_trend_sorting(trend_base)
