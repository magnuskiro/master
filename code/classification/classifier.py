# coding=utf-8
from utils import get_word_count, export_words, sanitize_tweet, \
    get_positive_negative_tweets_from_manually_labeled_tweets, get_lines_from_file


def a3():
    # TODO create
    return "N/A"


def word_count_classification(tweets_list, negative_dict, positive_dict, results):
    """
    Classifies tweets based on the given dictionaries.
    @param tweets_list: list of tweets to classify.
    @param negative_dict: list of negative words.
    @param positive_dict: list of positive words.
    @param results: the results of manual labeling.
    @return: the results: number of positive tweets, number of negative tweets, number of unclassified ones, accuracy by %.
    """

    # loading dictionaries
    dictionary_base = "/home/kiro/ntnu/master/code/dictionaries/"
    positive_dict = get_lines_from_file(dictionary_base + positive_dict)
    negative_dict = get_lines_from_file(dictionary_base + negative_dict)

    # init word count lists.
    positive_counts = []
    negative_counts = []

    # for all tweets to be classified.
    for tweet in tweets_list:
        # sanitize text.
        tweet = sanitize_tweet(tweet)

        # get word count for tweet
        word_count = len(tweet.split(' ')) * 1.0

        # get word count of pos/neg words.
        positive_counts.append(get_word_count(positive_dict, tweet) / word_count)
        negative_counts.append(get_word_count(negative_dict, tweet) / word_count)

        # store classified words from a tweet
        #export_words(tweet, (True if negative_counts[-1] < positive_counts[-1] else False))

    # result aggregation
    pos, neg, na = 0, 0, 0
    for i in range(len(positive_counts)):
        if positive_counts[i] > negative_counts[i]:
            pos += 1
        elif positive_counts[i] < negative_counts[i]:
            neg += 1
        else:
            na += 1

    # calculating accuracy just for nice print out:
    accuracy = 1 - ((abs(results[0] - pos) / (results[0] * 1.0) + abs(results[1] - neg) / (results[1] * 1.0)) / 2)

    return pos, neg, na, "%.2f" % accuracy


# Test function
def classify_obama(positive_dict, negative_dict, text, results):
    """
    Loads the obama tweets data to then call classification of tweets. Prints the results of the classification.
    @param positive_dict: name of file with positive words.
    @param negative_dict: name of file with negative words.
    @param text: the text to be printed for each classification run.
    @param results: the results of manual classification of the given dataset.
    @return: noting.
    """
    # load tweets
    tweets = open("../twitter/obama_tweets.txt").read().split("\n")

    print text
    print "(pos, neg, na, acc(%))"
    print word_count_classification(tweets, negative_dict, positive_dict, results)
    return


def classify_kiro_labeled(positive_dict, negative_dict, text, results):
    """
    Loads the dataset I have acquired and then call classification of tweets. Prints the results of the classification.
    @param positive_dict: name of file with positive words.
    @param negative_dict: name of file with negative words.
    @param text: the text to be printed for each classification run.
    @param results: the results of manual classification of the given dataset.
    @return: noting.
    """
    classification_base = "/home/kiro/ntnu/master/code/classification/"

    # load tweets
    # tweets[0] are the positive ones, tweets[1] are the negative ones.
    tweets = get_positive_negative_tweets_from_manually_labeled_tweets(
        classification_base + "tweets_classified_manually")

    # combine positive and negative tweets to one list.
    tweets = tweets[0] + tweets[1]

    print text
    print "(pos, neg, na, acc(%))"
    print word_count_classification(tweets, negative_dict, positive_dict, results)
    return

# easy running
if __name__ == "__main__":
    kiro_tweet_results = [575, 422, 0]
    obama_tweet_results = [507, 858, 0]
    print "--- Kiro"
    classify_kiro_labeled("compiled-positive.txt",
                          "compiled-negative.txt",
                          "Kiro, Monogram, self compile",
                          kiro_tweet_results)
    classify_kiro_labeled("obama-negative.txt",
                          "obama-positive.txt",
                          "Kiro, Monogram, obama",
                          kiro_tweet_results)
    classify_kiro_labeled("LoughranMcDonald_positive.txt",
                          "LoughranMcDonald_negative.txt",
                          "Kiro, Monogram LoughranMcDonald",
                          kiro_tweet_results)
    classify_kiro_labeled("positive.txt",
                          "negative.txt",
                          "Kiro, Monogram, combined Obama and LoughranMcDonald",
                          kiro_tweet_results)
    classify_kiro_labeled("bigram-compiled-positive.txt",
                          "bigram-compiled-negative.txt",
                          "Kiro, Bigram wordcount",
                          kiro_tweet_results)
    print "--- OBAMA"
    classify_obama("compiled-positive.txt",
                   "compiled-negative.txt",
                   "Obama, Monogram, self compile",
                   obama_tweet_results)
    classify_obama("obama-negative.txt",
                   "obama-positive.txt",
                   "Obama, Monogram, obama",
                   obama_tweet_results)
    classify_obama("LoughranMcDonald_positive.txt",
                   "LoughranMcDonald_negative.txt",
                   "Obama, Monogram LoughranMcDonald",
                   obama_tweet_results)
    classify_obama("positive.txt",
                   "negative.txt",
                   "Obama, Monogram, combined Obama and LoughranMcDonald",
                   obama_tweet_results)
    classify_obama("bigram-compiled-positive.txt",
                   "bigram-compiled-negative.txt",
                   "Obama, Bigram wordcount",
                   obama_tweet_results)
