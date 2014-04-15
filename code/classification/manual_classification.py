# coding=utf-8
import codecs
import re
import sys
from utils import load_data, export_words, sanitize_tweet, get_previous_tweets

__author__ = 'kiro'


def classify(filename):
    """
    Running manual classification.
    printing tweet, asking for y or n for positive or negative.
    Automatically exports positive and negative words to dictionaries.
    @param filename:
    @return:
    """
    manually_classified_tweets = codecs.open("tweets_classified_manually", "a", "utf-8")
    previous_tweets_list = get_previous_tweets("tweets_classified_manually")

    count = 0
    rt = 0
    for tweet in load_data(filename):

        print count
        count += 1

        # skip previously labeled tweets
        if str(tweet['id']) in str(previous_tweets_list):
            continue
        else:
            previous_tweets_list.append(tweet['id'])

        # skip retweets "^RT"
        if re.search(r"^RT", tweet['text']):
            rt += 1
            continue

        # skip tweets that has less then two words.
        #print tweet['text'].split(' ')
        if len(tweet['text'].split(' ')) < 2:
            continue

        print tweet['id']

        # remove urls, usernames and other unwanted characters.
        text = sanitize_tweet(tweet['text'])

        print text
        input_argument = raw_input("-----\nPos/neg/neither? y/n\n")
        if input_argument == "y":
            # save verdict to file
            manually_classified_tweets.write("1," + str(tweet['id']) + "," + text + "\n")
            # save positive words
            export_words(text.split(' '), True, "")
        elif input_argument == "n":
            # save verdict to file
            manually_classified_tweets.write("-1," + str(tweet['id']) + "," + text + "\n")
            # save positive words
            export_words(text.split(' '), False, "")
        else:
            manually_classified_tweets.write("0," + str(tweet['id']) + "," + text + "\n")

    manually_classified_tweets.close()

    print "rt: ", rt
    return


def classify_obama():
    filename = "obama_tweets_classified.txt"
    manually_classified_tweets = codecs.open("obama_tweets_classified_manually", "a", "utf-8")
    count = 0

    for text in open(filename).readlines():

        count += 1
        print count
        # if I mess up something it's easy to start the script again and get right back where i left off.
        if count < 1355:
            continue

        print text
        input_argument = raw_input("-----\nPos/neg/neither? y/n\n")
        # positive
        if input_argument == "y":
            # save verdict to file
            manually_classified_tweets.write("1," + text)
        # negative
        elif input_argument == "n":
            # save verdict to file
            manually_classified_tweets.write("-1," + text)

    manually_classified_tweets.close()
    return

if __name__ == "__main__":
    #if sys.argv[1]:
    #    classify(sys.argv[1])
    #else:
    #   classify("")
    classify_obama()