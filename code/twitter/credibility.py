import numpy as np

__author__ = 'kiro'

def calculate_credibility(tweet):
    credibility = [
        tweet['user']['followers_count'],
        tweet['user']['listed_count'],
        tweet['user']['friends_count'],
        tweet['user']['favourites_count']
    ]

    # weighting of the different parts.
    # TODO be tested an found.
    k = [0.7, 0.5, 0.3, 0.9] # randomly set variables.
    for i in range(0, len(credibility)):
        # weigh the values.
        credibility[i] *= k[i]

    # for the normalization.
    max_credibility = max(np.array(credibility))*1.0
    min_credibility = min(np.array(credibility))*1.0

    for i in range(0, len(credibility)):
        # normalization
        credibility[i] = ( (credibility[i] - min_credibility) / (max_credibility - min_credibility) )

    print credibility

    return credibility[0] + credibility[1] + credibility[2] + credibility[3]

def create_SVM_vector():
    # to become a tweet metadata object.
    line = [
        #tweet['id'],
        #tweet['text'],
        # todo get text features to use.
        #text: word_count, hastag_count, url_count, stock_count, positive_words, negative_words
        tweet['favorite_count'],
        tweet['retweet_count'],
        calculate_credibility(tweet),
        polarity
    ]