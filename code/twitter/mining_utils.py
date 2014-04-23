import ConfigParser
import ast
import codecs
import io
import datetime
from time import strftime
from twython import Twython

__author__ = 'kiro'


# reading twitter data from config file
# Default path is '.' aka open needs the full path from home.
# on windows it would be something like: "c:\Users\username\project\code\folder\twitter.cfg"
conf = open('/home/kiro/ntnu/master/code/twitter/auth.cfg').read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(conf))

# getting data from conf object.
APP_KEY = config.get('twtrauth', 'app_key')
APP_SECRET = config.get('twtrauth', 'app_secret')
OAUTH_TOKEN = config.get('twtrauth', 'oauth_token')
OAUTH_TOKEN_SECRET = config.get('twtrauth', 'oauth_token_secret')

# creating authentication object for twython twitter.
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


def get_twython_instance():
    return twitter


def create_meta_file(query, filename, previous_tweets_list):
    print "Complete: ", len(previous_tweets_list)

    # create metadata file for each dataset
    meta_file = codecs.open(filename + ".meta", "w", "utf-8")  # opens the file for appending.
    meta_file.write("last edited: " + strftime("%d-%b-%Y_%H:%M:%S") + "\n")
    meta_file.write("query:" + query + "\n")
    meta_file.write("count:" + str(len(previous_tweets_list)) + "\n")
    meta_file.close()
    print "Info -- Metadata file created"


def get_search_quota():
    # create rate limit check. if less then 90 queries remain, sleep 5 sec.
    status = ast.literal_eval(str(twitter.get_application_rate_limit_status()))
    limit = status['resources']['search']['/search/tweets']['limit']
    remaining_quota = status['resources']['search']['/search/tweets']['remaining']
    rate_remaining = status['resources']['application']['/application/rate_limit_status']['remaining']
    print "Info -- quota, search, rate:", limit, remaining_quota, rate_remaining
    return limit, remaining_quota, rate_remaining


def date_range():
    """

    @return:
    """
    # yyyy-mm-dd
    start = datetime.date(2014, 01, 01)
    end = datetime.date(2014, 04, 01)

    r = (end + datetime.timedelta(days=1) - start).days
    return [start + datetime.timedelta(days=i) for i in range(r)]
    #dateList = date_range(start, end)


def get_lines_from_file(filename):
    """
    Reads a file and returns all lines as array.
    @param filename: the location and name of the file.
    @return: array of lines from file.
    """
    input_file = codecs.open(filename, 'r', "utf-8")
    lines = input_file.readlines()
    for i in range(len(lines)):
        # removed .rstrip() don't think we need this here. to much regex fixing elsewhere.
        lines[i] = lines[i].lower().strip("\n")
    input_file.close()
    return lines


def write_array_entries_to_file(array, filename, mode="w"):
    """
    writes all entries in an array to file, if the entry is not in the file already.
    @param mode: write or append mode
    @param array: all the items to write.
    @param filename: the name of the output file
    @return: null
    """
    output = codecs.open(filename, mode, "utf-8")
    output.writelines([str(item).strip("\n")+"\n" for item in array])
    output.close()
    return
