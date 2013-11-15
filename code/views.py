from flask import render_template
from app import app

from data_mining import mining_operations
from classification import classifier


@app.route('/')
def homepage():
    return 'Welcome to nothingness'


@app.route('/data/')
def data():
    return str(mining_operations.data())


@app.route('/tweet/')
def classified():
    tweet = "This is the tweet text to be classified as positive or negative."
    return classifier.classify(tweet)


@app.errorhandler(404)
def page_not_found(error):
    print error
    return render_template('page_not_found.html'), 404