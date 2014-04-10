import ast
import codecs
import re

__author__ = 'kiro'

# base folder to look for files.
# needs to be changed to your specific path.
base = "/home/kiro/ntnu/master/code/twitter/"


def load_data(filename):

    # if filename not give, get it.
    if filename == '':
        filename = raw_input("input the filename of the file containing tweets: \n")

    # if filename not given, use default data
    if filename == '':
        filename = "dataset-testset"

    data_file = open(base+filename)
    # load all tweets in the file.
    tweets = []

    for line in data_file.readlines():
        # 'ast.literal_eval(price)' interprets the json tweet string as a dictionary.
        tweets.append(ast.literal_eval(line))

    return tweets

def get_word_count(dictionary, words):
    """
    counts the number of words from a tweet that is present in the given dictionary.
    @param dictionary:
    @param words:
    @return:
    """
    count = 0
    for word in words:
        if word in dictionary:
            count += 1
    return count

def sanitize_tweet(tweet):
    """
    Sanitize and remove unwanted parts of a tweet.

    @param tweet: the tweet metadata object.
    @return: the tweet metadata object.
    """
    text = tweet.lower()
    replacement = ""

    # TODO fix character replacement.
    # stripping the tweet of unwanted characters.
    regex = u"[\u2013\u2026+()!\"\#$%&'\()*+,-./:;<=>?@[]^_`{|}~\r\n]"
    # should use space so we don't create more words.
    text = re.sub(regex, " ", text)

    # remove usernames from tweet
    # matches from @ until and not space.
    username_regex = u"@[^\s]+"
    text = re.sub(username_regex, replacement, text)

    # remove links from tweet
    # matches everything including http:// until and not space.
    link_regex = u"http[s]*://[^ ]*"
    text = re.sub(link_regex, replacement, text)
    return text

def export_word_list(words, polarity, bigram):
    """
    Appending negative or positive words to the auto-dictionary file.
    @param bigram: give the bigram parameter string as 'bigram' to save bigrams.
    @param words:
    @param polarity:
    """
    if polarity:
        out = codecs.open("auto"+bigram+"-positive.txt", "a", "utf-8")
    else:
        out = codecs.open("auto"+bigram+"-negative.txt", "a", "utf-8")
    for w in words:
        out.write(w+"\n")
