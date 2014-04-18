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

        # adding sentiment value (True/False)
        if polarity[-1] > 0:
            # positive tweet
            results.append(True)
        else:
            # negative tweet
            results.append(False)

            # store classified words from a tweet
            #export_words(tweet, (True if negative_counts[-1] < positive_counts[-1] else False))

    return results


def test_classifier(tweet_file, positive_dict, negative_dict, text):
    """
    Loads the dataset I have acquired and then call classification of tweets. Prints the results of the classification.
    @param tweet_file: the name of the file to load tweets from.
    @param positive_dict: name of file with positive words.
    @param negative_dict: name of file with negative words.
    @param text: the text to be printed for each classification run.
    @return: noting.
    """
    # load tweets
    classification_base = "/home/kiro/ntnu/master/code/classification/"
    tweets = get_positive_negative_tweets_from_manually_labeled_tweets(classification_base + tweet_file)

    # classifying all tweets as positive or negative.
    sentiment_classification = word_count_classification(tweets[0] + tweets[1], negative_dict, positive_dict)

    # aggregate results
    counts, accuracy = aggregate_results(load_manually_labeled_tweets(tweet_file), sentiment_classification)

    print "INFO -- ", text
    print "{failed classifications, correct classifications}, accuracy of the classifier"
    print counts, "%.4f" % accuracy, "\n"


def run_classification():
    """
    Run all the classification tests.
    """
    print "--- Kiro dataset"
    test_classifier("tweets_classified_manually",
                    "compiled-positive.txt",
                    "compiled-negative.txt",
                    "Kiro, Monogram, self compiled")
    test_classifier("tweets_classified_manually",
                    "obama-negative.txt",
                    "obama-positive.txt",
                    "Kiro, Monogram, obama")
    test_classifier("tweets_classified_manually",
                    "LoughranMcDonald_Positive.txt",
                    "LoughranMcDonald_Negative.txt",
                    "Kiro, Monogram LoughranMcDonald")
    test_classifier("tweets_classified_manually",
                    "positive.txt",
                    "negative.txt",
                    "Kiro, Monogram, combined Obama and LoughranMcDonald")
    test_classifier("tweets_classified_manually",
                    "bigram-compiled-positive.txt",
                    "bigram-compiled-negative.txt",
                    "Kiro, Bigram wordcount")
    print "--- OBAMA dataset"
    test_classifier("obama_tweets_classified_manually",
                    "compiled-positive.txt",
                    "compiled-negative.txt",
                    "Obama, Monogram, self compiled")
    test_classifier("obama_tweets_classified_manually",
                    "obama-negative.txt",
                    "obama-positive.txt",
                    "Obama, Monogram, obama")
    test_classifier("obama_tweets_classified_manually",
                    "LoughranMcDonald_Positive.txt",
                    "LoughranMcDonald_Negative.txt",
                    "Obama, Monogram LoughranMcDonald")
    test_classifier("obama_tweets_classified_manually",
                    "positive.txt",
                    "negative.txt",
                    "Obama, Monogram, combined Obama and LoughranMcDonald")
    test_classifier("obama_tweets_classified_manually",
                    "bigram-compiled-positive.txt",
                    "bigram-compiled-negative.txt",
                    "Obama, Bigram wordcount")

# easy running
if __name__ == "__main__":
    run_classification()
