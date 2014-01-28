
from app import db

class Tweet(db.Model):
    """
    The classified tweet object that contains the metadata and classification data of a tweet.
    @param id:
    @param tweet: the original json tweet object.
    """
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String)
    positive_words = db.Column(db.Integer)
    negative_words = db.Column(db.Integer)
    sanitized_text = db.Column(db.String)
    polarity = db.Column(db.Boolean)
    polarity_value = db.Column(db.Integer)

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

    def __init__(self, tweet):
        #self.original = tweet
        self.original = "{ hei: { new : 20 }, old : 10 }"
        self.id = int(tweet['id'])

    def __unicode__(self):
        return self.id
