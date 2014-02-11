
import ast
from datetime import datetime
import re
from app import db

class Tweet(db.Model):
    """
    The classified tweet object that contains the metadata and classification data of a tweet.
    @param id:
    @param tweet: the original json tweet object.
    """
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String)
    date = db.Column(db.DateTime)

    sanitized_text = db.Column(db.String)
    positive_words = db.Column(db.Integer)
    negative_words = db.Column(db.Integer)
    polarity_value = db.Column(db.Integer)
    manual_polarity = db.Column(db.Boolean)
    classified_polarity = db.Column(db.Boolean)

    # tokens / mono-grams
    def monograms(self):
        return self.sanitized_text.lower().split(' ')

    def bigrams(self):
        monograms = self.monograms()
        # bi-grams
        bigrams = []
        for i in range(0, len(monograms)-1):
            bigrams.append(monograms[i]+" "+monograms[i+1])
            #print bigrams[-1] # probably not working.
        return bigrams

    def get_original_as_dict(self):
        return ast.literal_eval(self.original)

    def __init__(self, tweet):
        # store the original as a string.
        self.original = str(tweet)
        # store the ID.
        self.id = int(tweet['id'])
        # set date
        #datetime.strptime( string , format )datetime

        time = tweet['created_at']
        # stripping the tweet of unwanted characters.
        regex = u"\+\d\d\d\d "
        replacement = ""
        time = re.sub(regex, replacement, time)
        self.date = datetime.strptime(time, "%a %b %d %X %Y")

    def __unicode__(self):
        return self.id
