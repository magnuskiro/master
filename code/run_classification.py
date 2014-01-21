from dictionaries import dictionaries
from classification import classifier

neg = dictionaries.get_negative_dict()
pos = dictionaries.get_positve_dict()

tweet = "Todays winners are wrongfully wrong! Valuable" 

polarity = classifier.classify(tweet, pos, neg)
print 'score:', polarity

