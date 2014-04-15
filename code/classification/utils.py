# coding=utf-8
import ast
import codecs
import re

__author__ = 'kiro'


def get_previous_tweets(filename):
    """
    Get IDs of manually labeled tweets.
    @param filename: file with manually labeled tweets.
    @return: array with tweet ids.
    """
    tweets = []
    data_file = open(filename)

    #count = 0
    for line in data_file.readlines():
        # 'ast.literal_eval(price)' interprets the json tweet string as a dictionary.
        #print line
        #count += 1
        #print count
        tweets.append(line.split(",")[1])

    data_file.close()

    return tweets


def load_data(filename):
    """
    Loads a dataset from disk.
    @param filename: the name of the file to load.
    @return: an array with dictionary tweet objects.
    """

    # base folder to look for files.
    # needs to be changed to your specific path.
    base = "/home/kiro/ntnu/master/code/twitter/"

    # if filename not give, get it.
    if filename == '':
        filename = raw_input("input the filename of the file containing tweets: \n")

    # if filename not given, use default data
    if filename == '':
        filename = "dataset-testset"

    data_file = open(base + filename)
    # load all tweets in the file.
    tweets = []

    for line in data_file.readlines():
        # 'ast.literal_eval(price)' interprets the json tweet string as a dictionary.
        tweets.append(ast.literal_eval(line))

    data_file.close()

    return tweets


def get_word_count(dictionary, text):
    """
    counts the number of words from a tweet that is present in the given dictionary.
    @param text:
    @param dictionary:
    @return:
    """
    count = 0
    for word in dictionary:
        #print word, count
        #print word, "----", count
        if word in text:
            #print word
            count += 1
    return count


def sanitize_tweet(tweet):
    # TODO should use clean_text() in dict_utils
    """
    Sanitize and remove unwanted parts of a tweet.

    @param tweet: the tweet text
    @return: the sanitized text.
    """
    #print tweet, "\n----"
    text = tweet.lower()
    replacement = " "

    # remove usernames from tweet
    # matches from @ until and not space.
    pattern = u"@[^\s]+"
    regex = re.compile(pattern, re.MULTILINE)
    text = regex.sub(replacement, text)

    # remove links from tweet
    # matches everything including http:// until and not space.
    pattern = u"http[s]*://[^ ]*"
    regex = re.compile(pattern, re.MULTILINE)
    text = regex.sub(replacement, text)

    # stripping the tweet of unwanted characters.
    pattern = u"[!\"\%&\*+,-_./:…;<=>?@~\r\n|\\[\\]}{)(]"
    regex = re.compile(pattern, re.MULTILINE)
    text = regex.sub(replacement, text)

    # remove unnecessary spaces.
    pattern = u" +"
    regex = re.compile(pattern, re.MULTILINE)
    text = regex.sub(replacement, text)

    return text


def export_words(text, polarity):
    """
    Appending negative or positive words to the auto-dictionary file.
    @param bigram: give the bigram parameter string as 'bigram' to save bigrams.
    @param words:
    @param polarity:
    """
    #if polarity:
    #    out = codecs.open("auto" + bigram + "-positive.txt", "a", "utf-8")
    #else:
    #    out = codecs.open("auto" + bigram + "-negative.txt", "a", "utf-8")
    #for w in words:
    #    out.write(w + "\n")
    #out.close()
    return


def get_positive_negative_tweets_from_manually_labeled_tweets(filename):
    """
    From manually labeled tweets get positive and negative tweets.
    @param filename: file with manually labeled tweets
    @return: return an array with two lists, positive and negative tweets.
    """
    pos = []
    neg = []

    # labeled tweet file format:
    # polarity,id,text
    # -1,578123, content, content content , content
    # 1,17823017,word, word word word, word
    # 0,76125391, word, word word word, word

    # for all manually labeled tweets
    for line in get_lines_from_file(filename):
        params = line.split(",")
        # if tweet is labeled negative
        if params[0] == '-1':
            neg.append(''.join(params[2:]))
        # if tweet is labeled positive
        elif params[0] == '1':
            pos.append(''.join(params[2:]))
    return pos, neg


def get_lines_from_file(filename):
    """
    Reads a file and returns all lines as array.
    @param filename: the location and name of the file.
    @return: array of lines from file.
    """
    # TODO fix lambda elegance.
    input_file = codecs.open(filename, 'r', "utf-8")
    lines = input_file.readlines()
    for i in range(len(lines)):
        # be wary of the \n new line. might or might not be needed.
        lines[i] = lines[i].lower().strip("\n")
    input_file.close()
    return lines