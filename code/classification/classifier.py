# coding=utf-8
from utils import get_word_count, export_words, sanitize_tweet, \
    get_positive_negative_tweets_from_manually_labeled_tweets, get_lines_from_file


def a3():
    # TODO create
    return "N/A"


def word_count_classification(tweets_list, negative_dict, positive_dict):
    positive_counts = []
    negative_counts = []

    for tweet in tweets_list:
        # sanitize text.
        tweet = sanitize_tweet(tweet)

        # get word count for tweet
        word_count = len(tweet.split(' ')) * 1.0

        # get word count of pos/neg words.
        positive_counts.append(get_word_count(positive_dict, tweet) / word_count)
        negative_counts.append(get_word_count(negative_dict, tweet) / word_count)

        #print positive_counts[-1]
        #print negative_counts[-1]
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

    return pos, neg, na


# Test function
def classify_obama(pos_dict, neg_dict, text):
    tweets = open("../twitter/obama_tweets.txt").read().split("\n")
    positive_words = open("../dictionaries/" + pos_dict).read().split("\n")
    negative_words = open("../dictionaries/" + neg_dict).read().split("\n")

    print text
    print "(pos, neg, na)"
    print word_count_classification(tweets, negative_words, positive_words)
    return


def classify_kiro_labeled(pos_dict, neg_dict, text):
    classification_base = "/home/kiro/ntnu/master/code/classification/"
    dictionary_base = "/home/kiro/ntnu/master/code/dictionaries/"

    # get labeled tweets
    # tweets[0] are the positive ones, tweets[1] are the negative ones.
    tweets = get_positive_negative_tweets_from_manually_labeled_tweets(
        classification_base + "tweets_classified_manually")

    #print len(tweets[0]), len(tweets[1])
    tweets = tweets[0] + tweets[1]
    #print len(tweets)

    positive_words = get_lines_from_file(dictionary_base + pos_dict)
    negative_words = get_lines_from_file(dictionary_base + neg_dict)
    print text
    print "(pos, neg, na)"
    print word_count_classification(tweets, negative_words, positive_words)
    return

# easy running
if __name__ == "__main__":
    print "--- Kiro"
    classify_kiro_labeled("compiled-positive.txt",
                          "compiled-negative.txt",
                          "Kiro, Monogram, self compile")
    classify_kiro_labeled("obama-negative.txt",
                          "obama-positive.txt",
                          "Kiro, Monogram, obama")
    classify_kiro_labeled("LoughranMcDonald_lower_positive.txt",
                          "LoughranMcDonald_lower_negative.txt",
                          "Kiro, Monogram LoughranMcDonald")
    classify_kiro_labeled("positive.txt",
                          "negative.txt",
                          "Kiro, Monogram, combined Obama and LoughranMcDonald")
    classify_kiro_labeled("bigram-compiled-positive.txt",
                          "bigram-compiled-negative.txt",
                          "Kiro, Bigram wordcount")
    print "--- OBAMA"
    classify_obama("compiled-positive.txt",
                   "compiled-negative.txt",
                   "Obama, Monogram, self compile")
    classify_obama("obama-negative.txt",
                   "obama-positive.txt",
                   "Obama, Monogram, obama")
    classify_obama("LoughranMcDonald_lower_positive.txt",
                   "LoughranMcDonald_lower_negative.txt",
                   "Obama, Monogram LoughranMcDonald")
    classify_obama("positive.txt",
                   "negative.txt",
                   "Obama, Monogram, combined Obama and LoughranMcDonald")
    classify_obama("bigram-compiled-positive.txt",
                   "bigram-compiled-negative.txt",
                   "Obama, Bigram wordcount")

