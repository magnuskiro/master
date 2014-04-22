import ast
import codecs
from time import sleep
from mining_utils import date_range, get_lines_from_file, write_array_entries_to_file, get_twython_instance, \
    get_search_quota, create_meta_file

__author__ = 'kiro'

# base folder for these operations
base = "/home/kiro/ntnu/master/code/twitter/trend-data/"


def trend_minig():
    dates = date_range()
    for date in dates:
        #query = "Finance OR Investment OR Economy OR Growth AND -RT"
        query = "from:Norskoljeoggass OR " \
                "from:oljedir OR " \
                "from:oeddep OR " \
                "from: OR " \
                "from:tordlien " \
                "OR from:sprellnar OR from:IndustriEnergi OR " \
                "from:IndustriEnergiU OR from:_NITO_ " \
                "OR from:NorskIndustri OR from:TekniskMuseum OR from:UniResearch OR " \
                "from:linetrezz OR from:Geirseljeseth OR from:REINERTSENAS OR from:knebben OR " \
                "from: OR from: OR from:kobbaen OR from:GroBraekken OR from:ErlendJordal OR " \
                "from:nikolaiastrup OR from:AnnaLjunggren -RT"

        since = "2014-01-01"
        until = "2014-01-02"

        language = "no"

        # compile query

        # find ids matching days.

        # do mining

        # mine tweets for users, and terms we want
        # sort tweets on date from _daterange
        # remove duplicates from each day.
        # add more terms to search for.


def return_unique_tweets_in_search(results, previous_tweets_list):
    tweets = []

            #print "--unique tweet"
    #print "query count", count

    return tweets


def get_previous_tweet_ids(filename):
    tweets = []
    lines = codecs.open(base + filename, 'r', "utf-8")
    for line in lines.readlines():
        #print line
        tweets.append(ast.literal_eval(line)['id'])
        # 'ast.literal_eval(price)' interprets the json tweet string as a dictionary.
        #print tweets.append(ast.literal_eval(line)['id_str'])
    return tweets


def mine_tweets(query):
    twitter = get_twython_instance()

    # opens new file with today's date and time now as filename
    filename = base + query  # getting data-time string
    # opens the file for appending.
    data_set = open(filename, 'a')

    # list of tweets we already have for this query.
    previous_tweets_list = get_previous_tweet_ids(query)
    #print previous_tweets_list, len(previous_tweets_list)

    if len(set(previous_tweets_list)) != len(previous_tweets_list):
        exit("duplicates in previous tweets.")

    # do until we have reach date 2014-01-01, jan 1.
    while 1:
        print "-new query"

        #print "(limit, remaining)\n", get_search_quota()
        # executes query on twitter, creating a result object that yields tweets.
        if len(previous_tweets_list) > 0:
            #results = twitter.search(q=query, count='100', max_id=min(previous_tweets_list))
            results = twitter.cursor(twitter.search, q=query, count="100",
                                     max_id=min(previous_tweets_list))
        else:
            #results = twitter.search(q=query, count='100')
            results = twitter.cursor(twitter.search, q=query, count="100")

        print "(limit, remaining)\n", get_search_quota()
        print "tot tweets", len(previous_tweets_list), "\n"

        # get the quota for this results run.
        quota = get_search_quota()[1]
        # used to keep track of the number of tweets acquired
        count = 0

        try:
            # for tweets yielded by the result object.
            for result in results:  # twitter.cursor
            # if we use more then 10 queries to twitter, we expect this search to be exhausted.
            # todo fined a good walue for this.
                if count % 15 == 0:
                    if quota - get_search_quota()[1] >= 10:
                        break

                # if we reach the max amount of unique tweets in this query we stop.
                if count >= 99:
                    break
                count += 1
                print count

                if result['id'] in previous_tweets_list:
                    continue
                else:
                    previous_tweets_list.append(result['id'])
                    data_set.write(str(result)+"\n")
        except:
            print "Rate limit exceeded"
            break
        print "DONE trying"

        # if we have low quota and a lot of tweets.
        if len(previous_tweets_list) > 500 and quota <= 50:
            break

    # closing datafile and twitter result object.
    data_set.close()

    # create a file containing the metadata for the actual dataset.
    create_meta_file(query, filename, previous_tweets_list)


def mine(term):
    # TODO if user, format correctly.
    if "@" in term:
        term = "from:"+term
    print term

    # Waiting for full quota to continue
    while get_search_quota()[1] < 50:
        print "sleeping"
        sleep(60)
    mine_tweets(term)
    print "(limit, remaining)\n", get_search_quota()


def run_mining(filename):
    terms = get_lines_from_file(base + filename)
    # for all the search terms we want to mine, do the mining operation.
    for term in terms:
        mine(term)
        # only do one term
        exit()


if __name__ == "__main__":
    run_mining("_search-terms-norway")