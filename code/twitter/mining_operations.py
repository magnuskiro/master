import ast
import codecs
from time import strftime, sleep

# getting 'count' amount of tweets before 'until', with 'term' as search word.
from mining_utils import get_twython_instance, get_search_quota


def search(term='NTNU', count=15, since="2014-01-01", until='2014-01-02'):
    """

    @param term: the search term. decides what tweets you get back.
    @param count: the amount of tweets you want. (max 100)
    @param until: the earliest date you want tweets from.
    @return:
    """
    twitter = get_twython_instance()

    query = "NTNU OR Master OR Economy lang:en until:2014-04-15"

    #results = twitter.search(q='NTNU', count='15', until='2014-04-15')
    results = twitter.search(q=query, count='15')
    #results = twitter.search(q=term, count=count, since=since, until=until)
    #for result in results:
    #    print result
        #print result['id_str']

    print "len, ", len(results['statuses'])

    for status in results['statuses']:
        # status is the tweet
        print status['id_str']
        print status['created_at']

    return results['statuses']


def cursor_extraction(query='twitter', language='en', max_tweets=15, destination_folder="./twitter"):
    """
    creates a dataset with 'max_tweets' amount of tweets.
    limited by the 'query'
    tweets are stored in a file, one tweet per line.

    @param destination_folder: the folder to store the dataset we create.
    @param query: the search term that decides what data you get from twitter.
    @param max_tweets: the amount of tweets that are retrieved from tiwtter and stored.
    """

    twitter = get_twython_instance()

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
        if len(previous_tweets_list) > 0:
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
            # if we reach the max amount of unique tweets in this query we stop.
            if count >= 99:
                break
            count += 1

            # skip previously acquired tweets
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

    print "Complete: ", count * totcount

    # create metadata file for each dataset
    meta_file = codecs.open(filename + ".meta", "a", "utf-8")  # opens the file for appending.
    meta_file.write("query:" + query + "\n")
    meta_file.write("language:" + language + "\n")
    meta_file.write("count:" + str(count))
    meta_file.close()
    print "Metadata file created"


def start_minig():
    query = raw_input("input search query, press enter for standard. \n")
    if query == '':
        # all tweets containing one of the words and not 'RT'
        query = "Finance OR Investment OR Economy OR Growth AND -RT"

    language = "no"

    cursor_extraction(query, language, 1000, ".")


if __name__ == "__main__":
    print "(limit, remaining)\n", get_search_quota()
    #start_minig()
    #search()
