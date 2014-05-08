
from time import sleep
from mining_utils import get_lines_from_file, get_twython_instance, \
    get_search_quota, create_meta_file, get_previous_tweet_ids

__author__ = 'kiro'

# base folder for these operations
trend_data_base = "/home/kiro/ntnu/master/code/trend/trend-data/"
trend_base = "/home/kiro/ntnu/master/code/trend/"


def trend_mining(query):
    # get the object that executes queries on twitter.
    """
    Runs one search on twitter and stores new tweets to correct file.
    @param query: the string used for search on twitter.
    """
    twitter = get_twython_instance()

    # opens new file with today's date and time now as filename
    filename = trend_data_base + query  # getting data-time string

    # list of tweets we already have for this query.
    previous_tweets_list = get_previous_tweet_ids(filename)

    # opens the file for appending.
    data_set = open(filename, 'a')

    # get tweets from twitter.
    results = twitter.search(q=query, count='100')

    count = 0
    # for all the results in the search
    for result in results['statuses']:
        # if we don't have this tweet already store it.
        if result['id'] not in previous_tweets_list:
            # keep the id for later tweets.
            previous_tweets_list.append(result['id'])
            # write tweet to file.
            data_set.write(str(result) + "\n")
            count += 1

    print "Info -- Found %.f new tweets" % count

    # closing datafile and twitter result object.
    data_set.close()

    # create a file containing the metadata for the actual dataset.
    create_meta_file(query, filename, previous_tweets_list)


def mine_tweets(query):
    """
    Exhaustive mining, runs until we are sure that there are no more tweets for this search available in the twitter api
    and stores new tweets to file.
    @param query: the string used for search on twitter.
    """
    # get the object that executes queries on twitter.
    twitter = get_twython_instance()

    # opens new file with today's date and time now as filename
    filename = trend_data_base + query  # getting data-time string
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
                    data_set.write(str(result) + "\n")

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
    """
    While we can't get tweets from twitter: sleep, otherwise do mining with the given query.
    @param term: the search query we are going to use for gathering tweets.
    """
    while get_search_quota()[1] < 10 and get_search_quota()[2] < 10:
        print "sleeping: waiting for full quota"
        # 60 sec * number of min to sleep.
        sleep(60 * 5)

    print term
    trend_mining(term)
    #mine_tweets(term)


def run_mining(filename):
    """
    for all search queries in file, extract tweets for that query.
    @param filename: the name of the file containing search terms for mining.
    """
    terms = get_lines_from_file(filename)
    # for all the search terms we want to mine, do the mining operation.
    for term in terms:
        if term == "":
            continue
        # get all tweets with containing the term we want.
        mine(term)


if __name__ == "__main__":
    run_mining(trend_base+"_search-terms")