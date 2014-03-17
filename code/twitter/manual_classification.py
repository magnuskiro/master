
import codecs
import ast

__author__ = 'kiro'

# base folder to look for files.
base = "/home/kiro/ntnu/master/code/twitter/"

# input filename
filename = raw_input("input the filename of the file containing tweets: \n")
if filename == '':
    filename = "dataset-testset"

# load all tweets in the file.
tweets = []
data_file = open(base + filename)
for line in data_file.readlines():
    # 'ast.literal_eval(price)' interprets the json tweet string as a dictionary.
    tweets.append(ast.literal_eval(line))

for tweet in tweets:
    print tweet['text']
    input = raw_input("Pos/neg/neither? y/n\n")
    if input == "y":
        polarity = 1
    elif input == "n":
        polarity = -1
    else:
        polarity = 0

    line = tweet[id]+","+polarity
    #print line

    with codecs.open(base+"manually_classified_tweets.txt", "a", "utf-8") as unclassified_words:
       unclassified_words.write(str(line)+'\n')