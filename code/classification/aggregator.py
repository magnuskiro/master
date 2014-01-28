__author__ = 'kiro'


# todo should be moved to classification package
def get_aggregated_polarity(tweet):
    """
    @return: the polarity of the tweet. true/false
    """
    if tweet.positive_words > tweet.negative_words:
        return True
    else:
        return False

# todo should be moved to classification package
def get_aggregated_polarity_value(tweet):
    """
    aggregate and return the numeric polarity value.
    @return: the numeric value of the polarity for this tweet
    """
    return tweet.positive_words - tweet.negative_words
