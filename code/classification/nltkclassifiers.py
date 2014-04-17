
import nltk
from utils import get_lines_from_file, get_positive_negative_tweets_from_manually_labeled_tweets

__author__ = 'kiro'


def get_list_of_possible_words_in_tweets():
    """
    Create frequency distribution of words from tweets.
    aka returning the dictionary consisting of all interesting words in the tweet set.
    @return:
    """
    dictionary_base = "/home/kiro/ntnu/master/code/dictionaries/"
    positive_dict, negative_dict = "compiled-positive.txt", "compiled-negative.txt"
    positive_dict = get_lines_from_file(dictionary_base + positive_dict)
    negative_dict = get_lines_from_file(dictionary_base + negative_dict)
    word_list = positive_dict + negative_dict

    word_list = nltk.FreqDist(word_list)
    features = word_list.keys()
    return features


def extract_features_from_text(text):
    word_features = get_list_of_possible_words_in_tweets()
    document_words = set(text)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


def load_tweets():
    # load tweets
    classification_base = "/home/kiro/ntnu/master/code/classification/"
    tweets = get_positive_negative_tweets_from_manually_labeled_tweets(
        classification_base + "tweets_classified_manually")

    all_tweets = []
    # for all positive tweets
    for tweet in tweets[0]:
        # get words of two or more characters.
        words_filtered = [e.lower() for e in tweet.split() if len(e) >= 2]
        # add (words, sentiment) tuple to list of tweets.
        all_tweets.append((words_filtered, "positive"))
    # for all negative tweets
    for tweet in tweets[1]:
        # get words of two or more characters.
        words_filtered = [e.lower() for e in tweet.split() if len(e) >= 2]
        # add (words, sentiment) tuple to list of tweets.
        all_tweets.append((words_filtered, "negative"))

    return all_tweets


def get_classifier(classifier):
    # get data
    print "INFO -- Loading data"
    tweets = load_tweets()
    #tweets = test_tweets()

    # get the training set.
    print "INFO -- Compile training set for the classifier"
    training_set = nltk.classify.apply_features(extract_features_from_text, tweets)

    # create the classifier.
    print "INFO -- Training classifier, this might take some time."
    classifier = classifier.train(training_set)

    print "INFO -- Training complete. "
    return classifier


def classify(classifier, tweets):
    print "INFO -- Classifying tweets, this might take some time."
    results = []
    # for all tweets
    for tweet in tweets:
        # classify the tweet and append the result to list.
        results.append(classifier.classify(extract_features_from_text(tweet)))
    # return classification results
    return results


def kiro_test(classifier, text):

    # load tweets
    tweets = load_tweets()
    # classifying all tweets as positive or negative.
    sentiment_classification = classify(classifier, [tweet[0] for tweet in tweets])

    print "INFO -- Aggregating results"
    classification_results = []
    # for all tweets
    for i in range(len(tweets)):
        # append the boolean value representing correct classification of the given tweet.
        classification_results.append(tweets[i][1] == sentiment_classification[i])

    # compiling the counts of correct and false classification
    counts = dict((k, classification_results.count(k)) for k in set(classification_results))
    # calculating the accuracy of the classifier
    accuracy = (counts[True]*1.0) / (counts[False]+counts[True])
    print "INFO -- Done", text
    print "{failed calssifications, correct classifications}, accuracy of the classifier"
    print counts, accuracy


# easy running
if __name__ == "__main__":
    # run the testing of the classifier.
    #test_classifier(get_classifier(nltk.NaiveBayesClassifier))
    kiro_test(get_classifier(nltk.NaiveBayesClassifier), "Kiro test results")