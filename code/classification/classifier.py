
import codecs
import re
from classification import aggregator
from dictionaries import dictionaries


neg = dictionaries.get_negative_dict()
pos = dictionaries.get_positve_dict()

# Save unpolarized words for classification.
def classify_word(word):
    """

    @param word:
    """
    with codecs.open("dictionaries/unclassified_words.txt", "a", "utf-8") as unclassified_words:
        unclassified_words.write(word+'\n')


def pos_neg(words):
    """
    @type tweet: tweet
    @param pos: corpus of positive words
    @param neg: corpus of negative words
    @param tweet: the python dictionary of a tweet.
    @return: a dictionary with counted positive and negative words.
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


def sanitize_tweet(tweet):
    """
    Sanitize and remove unwanted parts of a tweet.

    @param tweet: the tweet metadata object.
    @return: the tweet metadata object.
    """
    text = unicode(tweet.original['text'])

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
    monogram_count = pos_neg(tweet.monograms())
    bigram_count = pos_neg(tweet.bigrams())
    tweet.negative_words = monogram_count['neg'] + bigram_count['neg']
    tweet.positive_words = monogram_count['pos'] + bigram_count['pos']

    ## part of speech
    # metadata
    ## location
    ## followers
    ## ect

    # set polarity
    tweet.polarity = aggregator.get_aggregated_polarity(tweet)
    tweet.polarity_value = aggregator.get_aggregated_polarity_value(tweet)
    return tweet

