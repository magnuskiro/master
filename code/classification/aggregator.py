__author__ = 'kiro'


def get_aggregated_polarity(tweet):
    """
    Aggregate the boolean polarity value for this tweet.
    @param tweet: my tweet metadata object.
    @return: the polarity of the tweet. true/false
    """
    if tweet.positive_words > tweet.negative_words:
        return True
    else:
        return False


def get_aggregated_polarity_value(tweet):
    """
    aggregate and return the numeric polarity value.
    @param tweet: my tweet metadata object.
    @return: the numeric value of the polarity for this tweet
    """
    return tweet.positive_words - tweet.negative_words
