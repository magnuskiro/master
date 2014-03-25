
import codecs
from utils import load_data, export_word_list, sanitize_tweet

__author__ = 'kiro'


def classify():
    """
    Running manual classification.
    printing tweet, asking for y or n for positive or negative.
    Automatically exports positive and negative words to dictionaries.
    @return:
    """
    manually_classified_tweets = codecs.open("manually_classified_tweets", "a", "utf-8")

    for tweet in load_data():
        print tweet['id']
        text = sanitize_tweet(tweet['text'])

        # TODO skip retweets "^RT"

        print text
        input = raw_input("-----\nPos/neg/neither? y/n\n")
        if input == "y":
            manually_classified_tweets.write("1,"+str(tweet['id'])+","+text+"\n")
            export_word_list(text.split(' '), True, "")
        elif input == "n":
            manually_classified_tweets.write("-1,"+str(tweet['id'])+","+text+"\n")
            export_word_list(text.split(' '), False, "")
        else:
            next
    return

if __name__ == "__main__":
    classify()
