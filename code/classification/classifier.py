
import codecs
#from classification import aggregator
#from dictionaries import dictionaries
#from dictionaries.dictionaries import classify_word
from classification.utils import get_word_count, sanitize_tweet, export_word_list

#negative_words = dictionaries.get_negative_dict()
#positive_words = dictionaries.get_positve_dict()


def get_pos_neg_word_count(words, pos, neg):
    """

    @param words:
    @return: a dict with counted positive and negative words.
    """
    word_count_dict = {'pos': 0, 'neg': 0}

    word_is_pos_or_neg = False
    for word in words:
        if word in pos:
            word_count_dict['pos'] += 1
            word_is_pos_or_neg = True
            #print pos[word]
        if word in neg:
            word_count_dict['pos'] -= 1
            word_is_pos_or_neg = True
            #print neg[word]
            # if the word don't appear in either dictionaries store it to be classified.
        # uncomment later.
        #if not word_is_pos_or_neg:
            #classify_word(word)
            #print word

    return word_count_dict


def a3():
    # TODO create
    return "N/A"


def a4():
    # TODO create
    return "N/A"


def a2(tweets_list, negative_dict, positive_dict):
    positive_counts = []
    negative_counts = []
    for tweet in tweets_list:
        tweet = sanitize_tweet(tweet)
        words = tweet.lower().split(' ')
        word_count = len(words) * 1.0

        #print get_word_count(positive_dict, words), " / ", get_word_count(negative_dict, words)
        positive_counts.append(get_word_count(positive_dict, words) / word_count)
        negative_counts.append(get_word_count(negative_dict, words) / word_count)

        if positive_counts[-1] > negative_counts[-1]:
            export_word_list(words, True, "")
        else:
            export_word_list(words, False, "")

    pos = 0
    neg = 0
    na = 0
    for i in range(len(positive_counts)):
        if positive_counts[i] > negative_counts[i]:
            pos += 1
        elif positive_counts[i] < negative_counts[i]:
            neg += 1
        else:
            na += 1

    return pos, neg, na

def classify_obama():
    tweets = open("../twitter/obama_tweets.txt").read().split("\n")
    negative_words = open("../dictionaries/negative.txt").read().split("\n")
    positive_words = open("../dictionaries/positive.txt").read().split("\n")
    print a2(tweets, negative_words, positive_words)

if __name__ == "__main__":
    classify_obama()