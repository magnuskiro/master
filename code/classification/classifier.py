
# Save unpolarized words for classification.
def classify_word(word):
    with open("unclassified_words.txt", "a") as unclassified_words:
        unclassified_words.write(word+'\n')


def classify(pos, neg, tweet):
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



