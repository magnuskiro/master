
import re
from classification import aggregator
from dictionaries import dictionaries
from dictionaries.dictionaries import classify_word

neg = dictionaries.get_negative_dict()
pos = dictionaries.get_positve_dict()


def get_pos_neg_word_count(words):
    """

    @param words:
    @return: a dict with counted positive and negative words.
    """
    polarity = {'pos': 0, 'neg': 0}

    word_is_pos_or_neg = False
    for word in words:
        if word in pos:
            polarity['pos'] += 1
            word_is_pos_or_neg = True
            #print pos[word]
        if word in neg:
            polarity['pos'] -= 1
            #print neg[word]
            word_is_pos_or_neg = True
            # if the word don't appear in either dictionaries store it to be classified.
        if not word_is_pos_or_neg:
            classify_word(word)
            #print word

    #return polarity['pos'] + polarity['neg']
    return polarity


def positive_vs_negative_words_classification(tweet):
    """
    Classifies the text of a tweet by counting positive and negative words.
    @param tweet:
    @return:
    """
    p1 = get_pos_neg_word_count(tweet.monograms())
    p2 = get_pos_neg_word_count(tweet.bigrams())

    # positive monograms and bigrams divided by negative monograms and bigrams.
    # gives us the ratio of positive over negative words in the sentence.
    if (p1['pos'] == 0 and p2['pos'] == 0) or (p1['neg'] == 0 and p2['neg'] == 0):
        return "N/A"
    else:
        return (p1['pos'] + p2['pos']) / (p1['neg'] + p2['neg'])


def a2():
    # TODO create
    return "N/A"


def a3():
    # TODO create
    return "N/A"


def a4():
    # TODO create
    return "N/A"


def sanitize_tweet(tweet):
    """
    Sanitize and remove unwanted parts of a tweet.

    @param tweet: the tweet metadata object.
    @return: the tweet metadata object.
    """
    text = unicode(tweet.get_original_as_dict()['text'])

    # stripping the tweet of unwanted characters.
    regex = u"[\u2013\u2026+()\.:',-]"
    replacement = ""
    text = re.sub(regex, replacement, text)

    tweet.sanitized_text = text
    return tweet


def classify(tweet):
    """
    Classifying tweets. Getting all the data ready to aggregate a value of boolean result of the sentiment of the tweet
    as positive or negative.
    @param tweet:
    @return:
    """

    ## prepare tweet
    tweet = sanitize_tweet(tweet)

    # todo classify polarity based on 4 different algorithms, not just the pos/neg one.
    ## pos_neg count
    monogram_count = get_pos_neg_word_count(tweet.monograms())
    bigram_count = get_pos_neg_word_count(tweet.bigrams())
    tweet.negative_words = monogram_count['neg'] + bigram_count['neg']
    tweet.positive_words = monogram_count['pos'] + bigram_count['pos']

    ## part of speech
    # metadata
    ## location
    ## followers
    ## ect

    # todo aggregation
    # set polarity
    tweet.classified_polarity = aggregator.get_aggregated_polarity(tweet)
    tweet.polarity_value = aggregator.get_aggregated_polarity_value(tweet)
    return tweet

