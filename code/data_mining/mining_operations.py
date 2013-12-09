from twython import Twython
import ConfigParser
import io
from time import strftime

# reading twitter data from config file
# Default path is '.' aka open needs the full path from home.
conf = open('/home/kiro/ntnu/master/code/twitter_integration/auth.cfg', 'r').read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(conf))

# configuration of twitter connection data.
APP_KEY = config.get('twtrauth', 'app_key')
APP_SECRET = config.get('twtrauth', 'app_secret')
OAUTH_TOKEN = config.get('twtrauth', 'oauth_token')
OAUTH_TOKEN_SECRET = config.get('twtrauth', 'oauth_token_secret')

# authentication on twitter.
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


# getting 'count' amount of tweets before 'until', with 'term' as search word.
def search(term='NTNU', count=15, until='2013-1-1'):
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


# creates a dataset of 'max_tweets' amount of tweets.
# limited to the search word.
def cursor_extraction(query='twitter', max_tweets=15):
    count = 0

    # opens new file with date today and time now as filename
    filename = strftime("%d-%b-%Y_%H:%M:%S")
    dataset_file = open(filename, 'a')

    # queries twitter for tweets.
    results = twitter.cursor(twitter.search, q=query, count="100")

    # for all the tweets in the seach result
    for result in results:
        # if we reach the desired amount of tweets we stop getting more.
        if count >= max_tweets:
            break
        count += 1
        #print result['created_at']
        #print result['id_str']
        print result['id_str']
        # store tweet to file for later use.
        dataset_file.write(str(result)+"\n")

    dataset_file.close()
    print count


# might be useful for getting tweets distributed over time.
def create_time_intervals():
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
            intervals.append("2013-"+str(mnd)+"-"+str(day))
    print len(intervals)
    return intervals

def load_dataset(filename = "27-Nov-2013_04:07:49"):
    tweets = []
    dataset_file = open(filename, 'r')
    for line in dataset_file.readlines():
        #json_tweet = line.convert.to.object.with.json
        # TODO change to import each tweet directly to an object, not a string.
        tweets.append(line)

#mine()
#print create_time_intervals()
#search("Finance")
cursor_extraction("Finance", 100)