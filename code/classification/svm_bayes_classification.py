# coding=utf-8
import nltk
from classification_utils import get_lines_from_file, load_manually_labeled_tweets, aggregate_results
from sklearn.svm import LinearSVC, NuSVC, NuSVR, OneClassSVM, SVC, SVR
from nltk.classify.scikitlearn import SklearnClassifier

__author__ = 'kiro'


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
    # extracts all words that are both in the dictionary and in the tweet
    for word in document_words:
        features['contains(%s)' % word] = (word in dictionary)
    return features


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
        #print tweet
        # classify the tweet and append the result to list.
        # runs classify() on the given classifier class in the nltk library.
        results.append(classifier.classify(extract_features_from_text(tweet)))
        #print results[-1], type(results[-1])
    return results


def run_classifier(tweet_file, classifier_class, text):
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

    print "INFO -- ", text
    print "{failed classifications, correct classifications}, accuracy of the classifier"
    print counts, "%.4f" % accuracy, "\n"


def test_svm_classes():
    """
    Testing all the possible classes of the sklearn.svm library.
    """
    # SVM, Linear Support Vector Classification
    classifiers = [
        LinearSVC(),
        NuSVC(),
        NuSVR(),
        OneClassSVM(),
        SVC(),
        SVR()
    ]
    for c in classifiers:
        print c
        classifier = SklearnClassifier(c)
        run_classifier("tweets_classified_manually", classifier, "Kiro tweets, SVM")


# easy running
if __name__ == "__main__":
    # list of [filename, description]
    tweet_sets = [
        ["tweets_classified_manually", "Kiro compiled dataset"],
        ["obama_tweets_classified_manually", "Obama tweet set"]
    ]

    classification_classes = [
        # Decision Tree classification.
        # Using this takes so long that I have always canceled the execution.
        #nltk.DecisionTreeClassifier,

        # Naive Bayes classification
        nltk.NaiveBayesClassifier,

        # SVM, Linear Support Vector Classification
        SklearnClassifier(LinearSVC())
    ]

    for classification_class in classification_classes:
        for data_file, description in tweet_sets:
            print "--", description, "--"
            run_classifier(data_file, classification_class, str(classification_class))
