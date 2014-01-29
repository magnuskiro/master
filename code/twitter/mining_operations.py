import codecs
from twython import Twython
import ConfigParser
import io
from time import strftime

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
def search(term='NTNU', count=15, until='2013-1-1'):
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


def cursor_extraction(query='twitter', max_tweets=15):
    """
    creates a dataset with 'max_tweets' amount of tweets.
    limited by the 'query'
    tweets are stored in a file, one tweet per line.

    @param query: the search term that decides what data you get from twitter.
    @param max_tweets: the amount of tweets that are retrieved from tiwtter and stored.
    """
    count = 0

    # opens new file with today's date and time now as filename
    filename = "./twitter/dataset-" + strftime("%d-%b-%Y_%H:%M:%S") # getting data-time string
    data_set = open(filename, 'a') # opens the file for appending.

    # executes query on twitter, creating a result object that yields tweets.
    results = twitter.cursor(twitter.search, q=query, count="100")

    #print query

    # for tweets yielded by the result object.
    for result in results:
        # if we reach the desired amount of tweets we stop getting more.
        if count >= max_tweets:
            break
        count += 1
        #print result['created_at']
        #print result['id_str']
        #print result['id_str']
        # store tweet to file for later use.
        data_set.write(str(result) + "\n")

    # closing datafile and twitter result object.
    data_set.close()
    results.close()
    #print count

    # create metadata file for each dataset
    meta_file = codecs.open(filename + ".meta", "a", "utf-8") # opens the file for appending.
    meta_file.write("query:"+query+"\n")
    meta_file.write("count:"+str(count))
    meta_file.close()


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

#mine()
#print create_time_intervals()
#search("Finance")
#cursor_extraction("Finance", 1000)