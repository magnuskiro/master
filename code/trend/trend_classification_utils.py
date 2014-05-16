# coding=utf-8
from os import listdir
import re
import nltk
from os.path import isfile, join
from mining_utils import get_lines_from_file
from nltk import SklearnClassifier
from sklearn.svm import LinearSVC

__author__ = 'kiro'

# Code in this file is copied from classification.


def load_manually_labeled_tweets(filename):
    """
    Loads tweets from file and returns them in the right format.
    @param filename: the file to load tweets from.
    @return:
    """
    # load tweets
    tweets = get_positive_negative_tweets_from_manually_labeled_tweets(filename)

    all_tweets = []
    # for all positive tweets
    for tweet in tweets[0]:
        # get words of two or more characters.
        words_filtered = [e.lower() for e in sanitize_tweet(tweet).split() if len(e) >= 2]
        # add (words, sentiment) tuple to list of tweets.
        all_tweets.append((words_filtered, True))
    # for all negative tweets
    for tweet in tweets[1]:
        # get words of two or more characters.
        words_filtered = [e.lower() for e in sanitize_tweet(tweet).split() if len(e) >= 2]
        # add (words, sentiment) tuple to list of tweets.
        all_tweets.append((words_filtered, False))

    return all_tweets


def get_list_of_possible_words_in_tweets():
    """
    Create frequency distribution of words from dictionaries.
    aka setting the dictionary consisting of all interesting words in the tweet set.
    @param negative_dict: list of positive words
    @param positive_dict: list of negative words
    @return:
    """
    # TODO fix the shortcomings of not having the option of dynamically changing the feature we use.
    positive_dict, negative_dict = "kiro-monogram-positive.txt", "kiro-monogram-negative.txt"
    #positive_dict, negative_dict = "bigram-compiled-positive.txt", "bigram-compiled-negative.txt"

    dictionary_base = "/home/kiro/ntnu/master/code/dictionaries/"
    positive_dict = get_lines_from_file(dictionary_base + positive_dict)
    negative_dict = get_lines_from_file(dictionary_base + negative_dict)
    word_list = positive_dict + negative_dict

    # returns a list of all words that has an effect on the sentiment of a tweet
    return nltk.FreqDist(word_list).keys()


def extract_features_from_text(text):
    """
    Separating words from a tweet text.
    @param text: the tweet or to extract features from.
    @return: a list of words to be used for classification.
    """
    dictionary = get_list_of_possible_words_in_tweets()
    document_words = set(text)
    features = {}
    # more precision to iterate the word of a tweet then the whole dictionary.
    for word in document_words:
        features['contains(%s)' % word] = (word in dictionary)
    return features


def get_classifier():
    """
    Load tweets, trains the classifier, and returns it.
    @return: classifier object.
    """
    classification_base = "/home/kiro/ntnu/master/code/classification/"
    tweet_file = "tweets_classified_manually"

    tweets = load_manually_labeled_tweets(classification_base + tweet_file)

    # The kernel module to be used in the classifier.
    classifier_class = SklearnClassifier(LinearSVC())
    # instantiate the classifier
    classifier = initialize_classifier(classifier_class, tweets)
    print "Info -- Classifier initialized"
    return classifier


def initialize_classifier(classifier_class, tweets):
    """
    Train and initialize classifier, then return it.
    @param tweets: list of tweets
    @param classifier_class: the nltk classifier class. Currently NaiveBayesClassifier and DecisionTreeClassifier tested
    @return: a nltk classifier.
    """
    # get the training set.
    #print "INFO -- Compile training set for the classifier"
    training_set = nltk.classify.apply_features(extract_features_from_text, tweets)

    # create the classifier.
    print "INFO -- Training the classifier, this might take some time."
    classifier = classifier_class.train(training_set)

    #print "INFO -- Training complete."
    return classifier


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


def get_trend_data_filenames(folder):
    """
    Run trend file compilation with all wanted files in the folder.
    @param folder: the folder containing tweet files.
    """
    files = [f for f in listdir(folder) if isfile(join(folder, f))]
    trend_files = []
    files.sort()
    for filename in files:
        # if it's a file we want append it to list of files.
        if "trend" in filename:
            trend_files.append(filename)
            continue

    return trend_files