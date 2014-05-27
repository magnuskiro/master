import ast
import codecs
import matplotlib.pyplot as plt
from trend_classification_utils import extract_features_from_text, get_classifier, get_trend_data_filenames, \
    sanitize_tweet
import urllib

__author__ = 'kiro'

trend_base = "/home/kiro/ntnu/master/code/trend/trend-data/"


def get_stock_exchange_values(url):
    """
    Code for getting stock exchange data from the internet.
    @param url: the file / link where the data is stored.
    @return: list of arrays, one for each day.
    """
    # get data file from internet. (csv)
    stock_exchange_history = urllib.urlopen(url).readlines()
    records = []
    for record in stock_exchange_history:
        # earlier records are not interesting.
        if "2014" in record:
            records.append(record.strip().lower().split(","))
        if "20140414" in record:
            break
    return records


def get_day_trend(trend_day_filename, classifier):
    """
    Extracting trend information from tweets in a specific day.
    @param trend_day_filename: File containing tweets from the given day.
    @param classifier: the classifier that will decide tweets as positive of negative.
    @return: array with three int values, representing the number of positive tweets, number og negative tweets and the
             total amount of tweets.
    """
    pos, neg = 0, 0

    # get tweets for this day.
    trend_day_tweets = [ast.literal_eval(tweet) for tweet in
                        codecs.open(trend_base + trend_day_filename, 'r', "utf-8").readlines()]

    # sentiment for each tweet.
    sentiment = []

    # for tweets in this day
    for tweet in trend_day_tweets:
        # get words of two or more characters.
        tweet_text = [e.lower() for e in sanitize_tweet(tweet['text']).split() if len(e) >= 2]
        #print tweet_text

        sentiment.append(classifier.classify(extract_features_from_text(tweet_text)))

        # classify pos/neg
        # value of day += value of tweet * popularity(the value that represents the spread an credibility of the tweet).

        # if the last tweet was positive.
        if sentiment[-1]:
            pos += 1
        else:
            neg += 1

    return [pos, neg, pos + neg]


def compile_pos_neg_for_tweets():
    """
    Compiling the trend data from tweets and returning it in a dict.
    @return: dictionary of trend data for the mined days.
    """

    # trains the classifier and returns the ready object.
    classifier = get_classifier()

    days = get_trend_data_filenames(trend_base)
    #compile_trend(trend_files)

    trend_days = {}
    # for all days
    print "Info -- Classifying tweets for each trend day"
    for day in days:
        # skipping days with too few tweets.
        if "Apr-19" in day or "Apr-20" in day or "Apr-21" in day or "Apr-22" in day:  # limit to 1 day in testing.
            continue
        # Storing stats for each day in dict.
        print day
        trend_days[day] = {}
        trend_days[day]['pos'], trend_days[day]['neg'], trend_days[day]['tot'] = get_day_trend(day, classifier)

    print trend_days
    return trend_days


def get_stock_graph_data():
    """
    Function for to simplify plotting of financial data.
    Calculate the percentage change from previous day.
    @return: list of graph plot values.
    """
    # get stock data
    #stock_records = get_stock_exchange_values(
    #    'http://www.netfonds.no/quotes/paperhistory.php?paper=OSEBX.OSE&csv_format=csv')

    stock_records = [
        ['20140423', 'osebx', 'oslo b\xf8rs', '561.13', '562.45', '557.74', '559.41', '0', '3339937790'],
        ['20140424', 'osebx', 'oslo b\xf8rs', '559.41', '565.65', '559.84', '562.89', '0', '4274186083'],
        ['20140425', 'osebx', 'oslo b\xf8rs', '562.89', '566.24', '562.41', '566.24', '0', '2924826814'],
        ['20140426', 'osebx', 'oslo b\xf8rs', '562.89', '566.24', '562.41', '566.24', '0', '2924826814'],  #
        ['20140427', 'osebx', 'oslo b\xf8rs', '562.89', '566.24', '562.41', '566.24', '0', '2924826814'],  #
        ['20140428', 'osebx', 'oslo b\xf8rs', '566.24', '567.14', '564.55', '566.82', '0', '2816490895'],
        ['20140429', 'osebx', 'oslo b\xf8rs', '566.82', '576.29', '566.82', '576.12', '0', '4483198308'],
        ['20140430', 'osebx', 'oslo b\xf8rs', '576.12', '580.93', '575.56', '578.37', '0', '5974359257'],
        ['20140501', 'osebx', 'oslo b\xf8rs', '578.37', '583.44', '578.50', '583.44', '0', '3938763164'],  #
        ['20140502', 'osebx', 'oslo b\xf8rs', '578.37', '583.44', '578.50', '583.44', '0', '3938763164'],
        ['20140503', 'osebx', 'oslo b\xf8rs', '578.37', '583.44', '578.50', '583.44', '0', '3938763164'],  #
        ['20140504', 'osebx', 'oslo b\xf8rs', '578.37', '583.44', '578.50', '583.44', '0', '3938763164'],  #
        ['20140505', 'osebx', 'oslo b\xf8rs', '583.44', '584.11', '579.28', '582.04', '0', '2268264138'],
        ['20140506', 'osebx', 'oslo b\xf8rs', '582.04', '585.01', '580.40', '582.77', '0', '3207736945'],
        ['20140507', 'osebx', 'oslo b\xf8rs', '582.77', '586.10', '579.60', '583.78', '0', '4674766325'],
        ['20140508', 'osebx', 'oslo b\xf8rs', '583.78', '589.11', '583.82', '589.05', '0', '4674766325'],
        ['20140509', 'osebx', 'oslo b\xf8rs', '589.05', '589.45', '586.11', '589.37', '0', '4054523151'],
        ['20140510', 'osebx', 'oslo b\xf8rs', '589.05', '589.45', '586.11', '589.37', '0', '4054523151'],  #
        ['20140511', 'osebx', 'oslo b\xf8rs', '589.05', '589.45', '586.11', '589.37', '0', '4054523151'],  #
        ['20140512', 'osebx', 'oslo b\xf8rs', '589.37', '596.02', '588.44', '596.01', '0', '3381405777'],
        ['20140513', 'osebx', 'oslo b\xf8rs', '596.01', '597.15', '593.49', '595.47', '0', '3381405777'],
        ['20140514', 'osebx', 'oslo b\xf8rs', '595.47', '598.00', '595.22', '597.78', '0', '3465552931'],
        ['20140515', 'osebx', 'oslo b\xf8rs', '597.78', '600.75', '594.40', '595.49', '0', '4062064215'],
        ['20140516', 'osebx', 'oslo b\xf8rs', '595.49', '597.49', '588.45', '593.60', '0', '3842116619']
    ]

    # convert to float.
    for i in range(0, len(stock_records)):
        #print stock_records[i]
        stock_records[i][6] = float(stock_records[i][6])
    # calculate graph plot points.
    results = []
    for i in range(1, len(stock_records)):
        closing_value_today = stock_records[i][6]
        closing_value_yesterday = stock_records[i - 1][6]

        average_value_today_yesterday = (stock_records[i][6] + stock_records[i - 1][6]) / 2

        # calculate percentage diff between this and the previous day.
        diff = (closing_value_today - closing_value_yesterday) / (
            average_value_today_yesterday * 1.0)

        # scaled to work with the tweet trend.
        results.append(diff * 100)

    print len(results)
    print results
    return results


def get_median_change_tweets(trend_days):
    """
    Function for calculating trend differences between days, based on tweets.
    @param trend_days: the data to calculate trend graph from.
    @return: list fo points for a graph.
    """
    keys = sorted(trend_days.keys())
    #print keys
    results = []
    for i in range(1, len(keys)):
        # difference from yesterday til today.
        # positive tweets
        positive_tweets_today = trend_days[keys[i]]['pos']
        positive_tweets_yesterday = trend_days[keys[i - 1]]['pos']

        # negative tweets
        negative_tweets_today = trend_days[keys[i]]['neg']
        negative_tweets_yesterday = trend_days[keys[i - 1]]['neg']

        # total amount of tweets
        total_amount_of_tweets = trend_days[keys[i]]['tot'] + \
                                 trend_days[keys[i - 1]]['tot']

        # change in positive tweets between this and the previous day.
        pos_diff = (positive_tweets_today - positive_tweets_yesterday) / (
            total_amount_of_tweets * 1.0)

        # change in negative tweets between this and the previous day.
        neg_diff = (negative_tweets_today - negative_tweets_yesterday) / (
            total_amount_of_tweets * 1.0)

        # median = the mid point between the positive and negative change points.
        # change in sentiment volume between this and the previous day.
        median = min([neg_diff, pos_diff]) + abs(pos_diff - neg_diff) / 2
        results.append(median)

        #print keys[i], "%.4f" % median, trend_days[keys[i]]['tot']
        #print "pos", keys[i], trend_days[keys[i]]['neg'] - trend_days[keys[i-1]]['neg']

    #print len(results)
    return results


def get_tweet_trend_data():
    """
    Method to simplify testing and plotting.
    @return: tweet trend data in a dict.
    """
    trend_days = {'trend-Apr-30': {'neg': 112, 'pos': 131, 'tot': 243},
                  'trend-May-19': {'neg': 523, 'pos': 1326, 'tot': 1849},
                  'trend-May-18': {'neg': 59, 'pos': 110, 'tot': 169},
                  'trend-May-15': {'neg': 1151, 'pos': 2255, 'tot': 3406},
                  'trend-May-14': {'neg': 596, 'pos': 1178, 'tot': 1774},
                  'trend-May-17': {'neg': 49, 'pos': 83, 'tot': 132},
                  'trend-May-16': {'neg': 1840, 'pos': 4320, 'tot': 6160},
                  'trend-May-11': {'neg': 121, 'pos': 169, 'tot': 290},
                  'trend-May-10': {'neg': 98, 'pos': 141, 'tot': 239},
                  'trend-May-13': {'neg': 1178, 'pos': 2108, 'tot': 3286},
                  'trend-May-12': {'neg': 980, 'pos': 2013, 'tot': 2993},
                  'trend-May-22': {'neg': 149, 'pos': 295, 'tot': 444},
                  'trend-May-24': {'neg': 341, 'pos': 1056, 'tot': 1397},
                  'trend-May-25': {'neg': 148, 'pos': 272, 'tot': 420},
                  'trend-May-23': {'neg': 256, 'pos': 468, 'tot': 724},
                  'trend-Apr-23': {'neg': 83, 'pos': 121, 'tot': 204},
                  'trend-Apr-24': {'neg': 104, 'pos': 195, 'tot': 299},
                  'trend-Apr-25': {'neg': 119, 'pos': 113, 'tot': 232},
                  'trend-Apr-26': {'neg': 198, 'pos': 371, 'tot': 569},
                  'trend-Apr-27': {'neg': 120, 'pos': 240, 'tot': 360},
                  'trend-Apr-28': {'neg': 260, 'pos': 446, 'tot': 706},
                  'trend-Apr-29': {'neg': 21, 'pos': 101, 'tot': 122},
                  'trend-May-21': {'neg': 64, 'pos': 190, 'tot': 254},
                  'trend-May-02': {'neg': 198, 'pos': 254, 'tot': 452},
                  'trend-May-03': {'neg': 130, 'pos': 174, 'tot': 304},
                  'trend-May-26': {'neg': 1691, 'pos': 4925, 'tot': 6616},
                  'trend-May-01': {'neg': 78, 'pos': 107, 'tot': 185},
                  'trend-May-06': {'neg': 1608, 'pos': 3737, 'tot': 5345},
                  'trend-May-07': {'neg': 206, 'pos': 391, 'tot': 597},
                  'trend-May-04': {'neg': 215, 'pos': 422, 'tot': 637},
                  'trend-May-05': {'neg': 227, 'pos': 437, 'tot': 664},
                  'trend-May-08': {'neg': 840, 'pos': 1807, 'tot': 2647},
                  'trend-May-09': {'neg': 117, 'pos': 215, 'tot': 332},
                  'trend-May-20': {'neg': 33, 'pos': 62, 'tot': 95}}

    return trend_days


def plot(trend_days):
    """
    Plotting the graphs of the two datasets for comparison.
    @param trend_days: the tweet trend data if we get it from somewhere else.
    """
    # plot stuffs.
    #xlen = len(trend_days.keys())
    xlen = 23

    x = [e for e in range(0, xlen)]

    # plot changes in tweets
    #y = get_median_change_tweets(trend_days)
    if trend_days:
        y = get_median_change_tweets(trend_days)
    else:
        y = get_median_change_tweets(get_tweet_trend_data())
    plt.plot(x, y, '-r')  # twitter data

    y = get_stock_graph_data()
    plt.plot(x, y, '-g')  # finance data

    # set axis, boundaries and labels.
    plt.axis([0, len(x) - 1, -1.0, max(y)])
    plt.xlabel('Days')
    plt.ylabel('Percentage change')

    plt.show()


def print_osebx():
    stock_records = [
        "20140526,OSEBX,Oslo Bors,601.82,606.37,600.59,600.80,0,2516585043",
        "20140523,OSEBX,Oslo Bors,599.06,601.85,597.25,601.82,0,2638282686",
        "20140522,OSEBX,Oslo Bors,595.18,599.08,595.35,599.06,0,2843077553",
        "20140521,OSEBX,Oslo Bors,591.75,595.35,591.50,595.18,0,2843077553",
        "20140520,OSEBX,Oslo Bors,594.43,595.16,589.51,591.75,0,3431501995",
        "20140519,OSEBX,Oslo Bors,593.60,595.95,591.57,594.43,0,2727302694",
        "20140516,OSEBX,Oslo Bors,595.49,597.49,588.45,593.60,0,3842116619",
        "20140515,OSEBX,Oslo Bors,597.78,600.75,594.40,595.49,0,4062064215",
        "20140514,OSEBX,Oslo Bors,595.47,598.00,595.22,597.78,0,3465552931",
        "20140513,OSEBX,Oslo Bors,596.01,597.15,593.49,595.47,0,3381405777",
        "20140512,OSEBX,Oslo Bors,589.37,596.02,588.44,596.01,0,3381405777",
        "20140509,OSEBX,Oslo Bors,589.05,589.45,586.11,589.37,0,4054523151",
        "20140508,OSEBX,Oslo Bors,583.78,589.11,583.82,589.05,0,4674766325",
        "20140507,OSEBX,Oslo Bors,582.77,586.10,579.60,583.78,0,4674766325",
        "20140506,OSEBX,Oslo Bors,582.04,585.01,580.40,582.77,0,3207736945",
        "20140505,OSEBX,Oslo Bors,583.44,584.11,579.28,582.04,0,2268264138",
        "20140502,OSEBX,Oslo Bors,578.37,583.44,578.50,583.44,0,3938763164",
        "20140430,OSEBX,Oslo Bors,576.12,580.93,575.56,578.37,0,5974359257",
        "20140429,OSEBX,Oslo Bors,566.82,576.29,566.82,576.12,0,4483198308",
        "20140428,OSEBX,Oslo Bors,566.24,567.14,564.55,566.82,0,2816490895",
        "20140425,OSEBX,Oslo Bors,562.89,566.24,562.41,566.24,0,2924826814",
        "20140424,OSEBX,Oslo Bors,559.41,565.65,559.84,562.89,0,4274186083",
        "20140423,OSEBX,Oslo Bors,561.13,562.45,557.74,559.41,0,3339937790"
    ]
    for r in reversed(stock_records):
        r = r.split(",")
        #Date,close,high,low,open,volume
        print str(r[0]) + "," + str(r[6]) + "," + str(r[4]) + str(",") + str(r[5]) + "," + str(r[3]) + "," + str(r[7])


def transform_tweet_data():
    #Date,close,high,low,open,volume
    #'trend-Apr-29': {'neg': 21, 'pos': 101, 'tot': 122},
    #print "data,h-l,pos,neg,open,tot"
    trend_days = get_tweet_trend_data()
    keys = sorted(trend_days.keys())
    date = ""
    for i in range(1, len(keys)):
        if "Apr" in keys[i]:
            date = "201404" + str(keys[i].split('-')[2])
        elif "May" in keys[i]:
            date = "201405" + str(keys[i].split('-')[2])
        volume = trend_days[keys[i]]['tot'] * 1.0
        # (positive_tweets / total_amount_of_tweets)*scale
        high = (trend_days[keys[i]]['pos'] / volume) * 1000
        # (negative_teets / total_amount_of_tweets)*scale
        low = (trend_days[keys[i]]['neg'] / volume) * 1000
        openv = 0
        close = high - low
        print str(date) + "," + str(close) + "," + str(high) + str(",") + str(low) + "," + str(volume / 10) + "," + str(
            0)


if __name__ == "__main__":
    #trend_data = compile_pos_neg_for_tweets()
    #plot(trend_data)
    #plot(get_tweet_trend_data())
    print_osebx()
    #transform_tweet_data()