
import nltk
from utils import get_lines_from_file, load_manually_labeled_tweets, aggregate_results

__author__ = 'kiro'


def get_list_of_possible_words_in_tweets():
    """
    Create frequency distribution of words from tweets.
    aka returning the dictionary consisting of all interesting words in the tweet set.
    @return: list of words
    """
    # TODO use full data from the input tweets, rather then the dictionaries.
    # TODO get dictionaries as input
    positive_dict, negative_dict = "compiled-positive.txt", "compiled-negative.txt"

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
    # TODO might be optimized by changing directions by checking words in dictionary rather than words in text.
    for word in dictionary:
        features['contains(%s)' % word] = (word in document_words)
    return features


def initialize_classifier(classifier_class, tweets):
    """
    Train and initialize classifier, then return it.
    @param tweets: list of tweets
    @param classifier_class: the nltk classifier class. Currently NaiveBayesClassifier and DecisionTreeClassifier tested
    @return: a nltk classifier.
    """

    # get the training set.
    print "INFO -- Compile training set for the classifier"
    training_set = nltk.classify.apply_features(extract_features_from_text, tweets)

    # create the classifier.
    print "INFO -- Training classifier, this might take some time."
    classifier = classifier_class.train(training_set)

    print "INFO -- Training complete. "
    return classifier


def classify(classifier_class, tweets):
    """
    Run the classification of tweets
    @param classifier_class: the nltk classifier class that we will use for the classification
    @param tweets: the list of tweets to classify
    @return: list of classification result (positive/negative)
    """
    # instantiate the classifier
    classifier = initialize_classifier(classifier_class, tweets)

    print "INFO -- Classifying tweets, this might take some time."
    results = []
    # for all tweets
    for tweet in [tweet[0] for tweet in tweets]:
        # classify the tweet and append the result to list.
        # runs classify() on the given classifier class in the nltk library.
        results.append(classifier.classify(extract_features_from_text(tweet)))
    # return classification results
    return results


def test_classifier(tweet_file, classifier_class, text):
    """
    Run the test of the classifier, so we can get some results.
    @param tweet_file: the file to load tweets from.
    @param classifier_class: the nltk classifier class to be used.
    @param text: text to be printed with the results.
    """
    # load tweets
    classification_base = "/home/kiro/ntnu/master/code/classification/"
    tweets = load_manually_labeled_tweets(classification_base + tweet_file)

    # classifying all tweets as positive or negative.
    sentiment_classification = classify(classifier_class, tweets)

    # aggregate results
    counts, accuracy = aggregate_results(tweets, sentiment_classification)

    print "INFO -- Done", text
    print "{failed classifications, correct classifications}, accuracy of the classifier"
    print counts, "%.2f" % accuracy, "\n"


# easy running
if __name__ == "__main__":
    # run the testing of the classifier.
    #test_classifier("tweets_classified_manually", nltk.NaiveBayesClassifier, "Kiro tweets, Naive Bayes")
    test_classifier("obama_tweets_classified_manually", nltk.NaiveBayesClassifier, "Obama tweets, Naive Bayes")
    # this takes a freakishly long time.
    #kiro_test(nltk.DecisionTreeClassifier, "Kiro tweets, Decision Tree")