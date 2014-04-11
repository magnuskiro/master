import ast
import codecs
import datetime
from twython import Twython
import ConfigParser
import io
from time import strftime, sleep

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


# getting 'count' amount of tweets before 'until', with 'term' as search word.
def search(term='NTNU', count=15, until='2014-1-1'):
    """

    @param term: the search term. decides what tweets you get back.
    @param count: the amount of tweets you want. (max 100)
    @param until: the earliest date you want tweets from.
    @return:
    """
    print "executing query on twitter"

    #results = twitter.search(q="NTNU", count="15", until="2013-11-20")
    results = twitter.search(q=term, count=count, until=until)
    for result in results:
        print result
        #print result['id_str']

    print len(results['statuses'])

    for status in results['statuses']:
        # status is the tweet
        print status['id_str']

    return results['statuses']


def date_range(start, end):
    # yyyy-mm-dd
    start = datetime.date(2014, 01, 01)
    end = datetime.date(2014, 04, 01)

    r = (end + datetime.timedelta(days=1) - start).days
    return [start + datetime.timedelta(days=i) for i in range(r)]
    #dateList = date_range(start, end)


def cursor_extraction(query='twitter', language='en', max_tweets=15, destination_folder="./twitter"):
    """
    creates a dataset with 'max_tweets' amount of tweets.
    limited by the 'query'
    tweets are stored in a file, one tweet per line.

    @param destination_folder: the folder to store the dataset we create.
    @param query: the search term that decides what data you get from twitter.
    @param max_tweets: the amount of tweets that are retrieved from tiwtter and stored.
    """

    # opens new file with today's date and time now as filename
    filename = destination_folder + "/dataset-" + strftime("%d-%b-%Y_%H:%M:%S")  # getting data-time string
    # opens the file for appending.
    data_set = open(filename, 'a')

    # list of tweets we already have for this wuery.
    previous_tweets_list = []

    # total amount of tweets mined this execution
    totcount = 0

    for i in range(max_tweets / 100):
        totcount = i

        # executes query on twitter, creating a result object that yields tweets.
        if len(previous_tweets_list)>0:
            results = twitter.cursor(twitter.search, q=query, count="100", lauage=language,
                                     max_id=min(previous_tweets_list))
        else:
            results = twitter.cursor(twitter.search, q=query, count="100", lauage=language)

        # create rate limit check. if less then 90 queries remain, sleep 5 sec.
        status = ast.literal_eval(str(twitter.get_application_rate_limit_status()))
        remaining_quota = status['resources']['search']['/search/tweets']['remaining']

        if remaining_quota <= 90:
            sleep(5)
        #exit()

        # used to keep track of the number of tweets acquired
        count = 0
        #print "-------------------- NEW QUERY"
        #print min(previous_tweets_list)

        # for tweets yielded by the result object.
        for result in results:
            # if we reach the desired amount of tweets we stop getting more.
            if count >= 99:
                break
            count += 1

            # skip previously labeled tweets
            if str(result['id_str']) in str(previous_tweets_list):
                continue
            else:
                previous_tweets_list.append(result['id_str'])

            #print result['id_str']
            # store tweet to file for later use.
            data_set.write(str(result) + "\n")

        results.close()

    # closing datafile and twitter result object.
    data_set.close()

    print "Complete: ", count*totcount

    # create metadata file for each dataset
    meta_file = codecs.open(filename + ".meta", "a", "utf-8")  # opens the file for appending.
    meta_file.write("query:" + query + "\n")
    meta_file.write("language:" + language + "\n")
    meta_file.write("count:" + str(count))
    meta_file.close()
    print "Metadata file created"


def create_time_intervals():
    """
    Creating a set of date intervals.
    Might be useful for getting tweets distributed over time.

    @return: list of intervals.
    """
    # 100 queries
    # 100 tweets per query
    # resulting in 10k tweets.
    # first 100 days of 2013.

    # 100 intervals
    # until format: YYYY-MM-DD (unix time)
    #intervals = [the list of until items] # from 2013-01-02

    intervals = []
    for mnd in range(1, 5):
        for day in range(1, 26):
            intervals.append("2013-" + str(mnd) + "-" + str(day))
    print len(intervals)
    return intervals


def get_search_quota():
    # create rate limit check. if less then 90 queries remain, sleep 5 sec.
    status = ast.literal_eval(str(twitter.get_application_rate_limit_status()))
    limit = status['resources']['search']['/search/tweets']['limit']
    remaining_quota = status['resources']['search']['/search/tweets']['remaining']
    return limit, remaining_quota


def start_minig():
    query = raw_input("input search query, press enter for standard. \n")
    if query == '':
        # all tweets containing one of the words and not 'RT'
        query = "Finance OR Investment OR Economy OR Growth AND -RT"

    language = "no"

    cursor_extraction(query, language, 1000, ".")

if __name__ == "__main__":
    start_minig()
    print "(limit, remaining)\n", get_search_quota()


