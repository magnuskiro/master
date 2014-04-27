# coding=utf-8
from classification_utils import get_word_count, sanitize_tweet, \
    get_positive_negative_tweets_from_manually_labeled_tweets, get_lines_from_file, load_manually_labeled_tweets, \
    aggregate_results


def word_count_classification(tweets_list, negative_dict, positive_dict):
    """
    Classifies tweets based on the given dictionaries.
    @param tweets_list: list of tweets to classify.
    @param negative_dict: list of negative words.
    @param positive_dict: list of positive words.
    @return: list of true/false values that represent the sentiment of a tweet, the result of the classification.
    """

    # loading dictionaries
    dictionary_base = "/home/kiro/ntnu/master/code/dictionaries/"
    positive_dict = get_lines_from_file(dictionary_base + positive_dict)
    negative_dict = get_lines_from_file(dictionary_base + negative_dict)

    # init polarity results list.
    polarity = []
    results = []

    # for all tweets to be classified.
    for tweet in tweets_list:
        # sanitize text.
        tweet = sanitize_tweet(tweet)

        # get word count for tweet
        word_count = len(tweet.split(' ')) * 1.0

        # get word count of pos/neg words.
        pos = get_word_count(positive_dict, tweet) / word_count
        neg = get_word_count(negative_dict, tweet) / word_count

        # storing the polarity value
        polarity.append(pos - neg)

        # TODO test threshold values .1 - .9
        threshold = .0  # .2 = 60% positive.
        # adding sentiment value (True/False), for the last classified tweet.
        if polarity[-1] > threshold:
            # positive tweet
            results.append(True)
        else:
            # negative tweet
            results.append(False)

            # store classified words from a tweet
            #export_words(tweet, (True if negative_counts[-1] < positive_counts[-1] else False))

    return results


def test_classifier(tweet_file, positive_dict, negative_dict, info_text):
    """
    Loads the dataset I have acquired and then call classification of tweets. Prints the results of the classification.
    @param tweet_file: the name of the file to load tweets from.
    @param positive_dict: name of file with positive words.
    @param negative_dict: name of file with negative words.
    @param info_text: the text to be printed for each classification run.
    @return: noting.
    """
    # load tweets
    classification_base = "/home/kiro/ntnu/master/code/classification/"
    tweets = get_positive_negative_tweets_from_manually_labeled_tweets(classification_base + tweet_file)

    # classifying all tweets as positive or negative.
    sentiment_classification = word_count_classification(tweets[0] + tweets[1], negative_dict, positive_dict)

    # aggregate results
    counts, accuracy = aggregate_results(load_manually_labeled_tweets(tweet_file), sentiment_classification)

    print "Info -- ", info_text
    print "{failed classifications, correct classifications}, accuracy of the classifier"
    print counts, "%.4f" % accuracy, "\n"


def run_classification():
    """
    Run all the classification tests.
    """
    # list of [filename, description]
    tweet_sets = [
        ["tweets_classified_manually", "Kiro compiled dataset"],
        ["obama_tweets_classified_manually", "Obama tweet set"]
    ]

    # static data defining filename of dictionaries and output text.
    dictionary_combinations = [
        # downloaded dictionaries.
        ["obama-negative.txt", "obama-positive.txt", "Monogram, obama"],
        ["LoughranMcDonald_Positive.txt", "LoughranMcDonald_Negative.txt", "Monogram LoughranMcDonald"],
        ["obama+mcdonald-positive.txt", "obama+mcdonald-negative.txt", "Monogram, combined Obama and LoughranMcDonald"],
        # selfcompiled dictionaries.
        # monogram
        ["kiro-monogram-positive.txt", "kiro-monogram-negative.txt", "Kiro, Monogram, self compiled"],
        ["obama-monogram-positive.txt", "obama-monogram-negative.txt", "Obama, Monogram, self compiled"],
        # bigram
        ["kiro-bigram-positive.txt", "bigram-negative.txt", "Kiro, Bigram, self compiled"],
        ["obama-bigram-positive.txt", "bigram-negative.txt", "Obama Bigram, self compiled"],
        # trigram
        ["kiro-trigram-positive.txt", "kiro-trigram-negative.txt", "Kiro, Trigram, self compiled"],
        ["obama-trigram-positive.txt", "obama-trigram-negative.txt", "Obama Trigram, self compiled"]
    ]

    # executing classification
    for filename, description in tweet_sets:
        print "--", description, "--"
        for combo in dictionary_combinations:
            positive_dict, negative_dict, info_text = combo
            test_classifier(filename, positive_dict, negative_dict, info_text)

# easy running
if __name__ == "__main__":
    run_classification()
