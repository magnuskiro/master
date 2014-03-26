
import codecs
import re
from utils import load_data, export_word_list, sanitize_tweet

__author__ = 'kiro'


def get_previous_tweets(filename):
    tweets = []
    data_file = open(filename)

    #count = 0
    for line in data_file.readlines():
        # 'ast.literal_eval(price)' interprets the json tweet string as a dictionary.
        #print line
        #count += 1
        #print count
        tweets.append(line.split(",")[1])

    return tweets

def classify():
    """
    Running manual classification.
    printing tweet, asking for y or n for positive or negative.
    Automatically exports positive and negative words to dictionaries.
    @return:
    """
    manually_classified_tweets = codecs.open("tweets_classified_manually", "a", "utf-8")

    count = 0
    rt = 0
    for tweet in load_data():

        print count
        count += 1

        # skip previously labeled tweets
        previous_tweets_list = get_previous_tweets("tweets_classified_manually")
        if str(tweet['id']) in str(previous_tweets_list):
            continue

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
            manually_classified_tweets.write("1,"+str(tweet['id'])+","+text+"\n")
            export_word_list(text.split(' '), True, "")
        elif input_argument == "n":
            manually_classified_tweets.write("-1,"+str(tweet['id'])+","+text+"\n")
            export_word_list(text.split(' '), False, "")
        else:
            manually_classified_tweets.write("0,"+str(tweet['id'])+","+text+"\n")
    print "rt: ", rt
    return

if __name__ == "__main__":
    classify()
