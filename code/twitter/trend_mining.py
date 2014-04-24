import ast
import codecs
from time import sleep
from mining_utils import date_range, get_lines_from_file, write_array_entries_to_file, get_twython_instance, \
    get_search_quota, create_meta_file

__author__ = 'kiro'

# base folder for these operations
trend_base = "/home/kiro/ntnu/master/code/twitter/trend-data/"


def trend_minig(query):
    twitter = get_twython_instance()

    # opens new file with today's date and time now as filename
    filename = trend_base + query  # getting data-time string
    # opens the file for appending.
    data_set = open(filename, 'a')

    # list of tweets we already have for this query.
    previous_tweets_list = get_previous_tweet_ids(query)

    results = twitter.search(q=query, count='100')

    count = 0
    for result in results['statuses']:
        if result['id'] not in previous_tweets_list:
            previous_tweets_list.append(result['id'])
            data_set.write(str(result)+"\n")
            count += 1

    print "Info -- Found %.f new tweets" % count

    # closing datafile and twitter result object.
    data_set.close()

    # create a file containing the metadata for the actual dataset.
    create_meta_file(query, filename, previous_tweets_list)


def get_previous_tweet_ids(filename):
    tweets = []
    lines = codecs.open(trend_base + filename, 'r', "utf-8")
    for line in lines.readlines():
        #print line
        tweets.append(ast.literal_eval(line)['id'])
        # 'ast.literal_eval(price)' interprets the json tweet string as a dictionary.
        #print tweets.append(ast.literal_eval(line)['id_str'])
    return tweets


def mine_tweets(query):
    twitter = get_twython_instance()

    # opens new file with today's date and time now as filename
    filename = trend_base + query  # getting data-time string
    # opens the file for appending.
    data_set = open(filename, 'a')

    # list of tweets we already have for this query.
    previous_tweets_list = get_previous_tweet_ids(query)
    #print previous_tweets_list, len(previous_tweets_list)

    if len(set(previous_tweets_list)) != len(previous_tweets_list):
        exit("duplicates in previous tweets.")

    while 1:
        print "NEW query"

        #print "(limit, remaining)\n", get_search_quota()
        # executes query on twitter, creating a result object that yields tweets.
        if len(previous_tweets_list) > 0:
            #results = twitter.search(q=query, count='100', max_id=min(previous_tweets_list))
            results = twitter.cursor(twitter.search, q=query, count="100",
                                     max_id=min(previous_tweets_list))
        else:
            #results = twitter.search(q=query, count='100')
            results = twitter.cursor(twitter.search, q=query, count="100")

        # get the quota for this results run.
        quota = get_search_quota()[1]
        print "tot tweets", len(previous_tweets_list)

        # used to keep track of the number of tweets acquired
        count = 0

        try:
            # for tweets yielded by the result object.
            for result in results:  # twitter.cursor
                # if we reach the max amount of unique tweets in this query we stop.
                if count >= 99:
                    break
                count += 1
                print count

                if result['id'] not in previous_tweets_list:
                    previous_tweets_list.append(result['id'])
                    data_set.write(str(result)+"\n")

                # if we use more then 10 queries to twitter, we expect this search to be exhausted.
                if count % 10 == 0:
                    if quota - get_search_quota()[1] >= 10:
                        print "Info -- count quota reached"
                        break
        except:
            print "Rate limit exceeded"
            break

        # if we get less than 100 tweet from a query we stop.
        if count <= 99:
            break

        print "tot tweets", len(previous_tweets_list)

    # closing datafile and twitter result object.
    data_set.close()

    # create a file containing the metadata for the actual dataset.
    create_meta_file(query, filename, previous_tweets_list)


def mine(term):
    # Waiting for full quota to continue
    while get_search_quota()[1] < 30 and get_search_quota()[2] < 30:
        print "sleeping: waiting for full quota"
        # 60 sec * number of min to sleep.
        sleep(60*5)

    print term
    trend_minig(term)
    #mine_tweets(term)


def run_mining(filename):
    terms = get_lines_from_file(trend_base + filename)
    # for all the search terms we want to mine, do the mining operation.
    for term in terms:
        if term == "":
            continue
        # get all tweets with containing the term we want.
        mine(term)


if __name__ == "__main__":
    run_mining("_search-terms-norway")