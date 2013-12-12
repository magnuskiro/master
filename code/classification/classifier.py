from dictionaries import dictionaries

# Save unpolarized words for classification.
def classify_word(word):
    with open("unclassified_words.txt", "a") as unclassified_words:
        unclassified_words.write(word+'\n')


def pos_neg(pos, neg, tweet):
    tweet = tweet.lower()

    polarity = {'pos': 0, 'neg': 0}

    for word in tweet.split(' '):
        print word
        if word in pos:
            polarity['pos'] += 1
            print pos[word]
        else:
            classify_word(word)
        if word in neg:
            polarity['pos'] -= 1
            print neg[word]
        else:
            classify_word(word)

    return polarity['pos'] + polarity['neg']


def prepare():
    # todo
    # strip
    # tokenize
    # mono-grams
    # bi-grams
    pass


def classify(tweet):
    # todo
    # execute all classification methods and aggregate a total.

    # text
    ## get dictionaries

    ## prepare tweet
    prepare()

    ## pos_neg count
    pos_neg(dictionaries.get_positve_dict(), dictionaries.get_positve_dict(), "this is the tweet")

    ## part of speech

    # metadata
    ## location
    ## followers
    ## ect

