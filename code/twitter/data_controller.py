import json

# loading and storing data to local disk.

def load_data(filename="27-Nov-2013_04:07:49"):
    tweets = []
    data_file = open(filename, 'r')
    for line in data_file.readlines():
        #json_tweet = line.convert.to.object.with.json
        # TODO change to import each tweet directly to an object, not a string.
        tweets.append(line)