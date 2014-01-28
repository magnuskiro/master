
from time import sleep
from flask import render_template, request
from app import app
from classification import classifier
from models import *
from twitter import data_controller
#API routes and other internal tools.


@app.route('/trend_data')
def trend_data():
    """
    Returns the json object that represents a datapoint i the trend graph.
    @return:
    """
    return "{ trend: { date : 15-01-14, sentiment-value : 401, stock-value : 405 } }"


@app.route('/dataset', methods=['POST'])
def new_dataset():
    """
    @return:
    """
    assert request.path == '/dataset'
    assert request.method == 'POST'
    if "Twitter search Query" not in request.data:
        data_controller.create_new_data_set(request.data)
    sleep(10)
    return


@app.route('/newdataset')
def newdataset():
    data_controller.create_new_data_set("Financial times")


@app.route('/classify')
def classify():
    """
    Runs the classification process that gets the sentiment from tweets.
    @return:
    """
    tweet_list = data_controller.load_tweets()
    for tweet in tweet_list:
        # create tweet object
        classified_tweet = Tweet(tweet)

        # classify the tweet
        classified_tweet = classifier.classify(classified_tweet)
        print classified_tweet.id, ":", classified_tweet.polarity
        # todo save
        data_controller.save_tweet(classified_tweet)

    return "classification complete"


# Regular html routes, returning html/js only
@app.route('/')
def homepage():
    return render_template('main.html')


@app.route('/tweets')
def tweets():
    datasets = data_controller.get_data_set_names()
    return render_template('tweets.html', datasets=datasets)


@app.route('/sentiment')
def sentiment():
    """
    Views the sentiment page with a tweet and its sentiment classification.
    @return:
    """
    tweet = data_controller.get_one_tweet()
    return render_template('sentiment.html', tweet=tweet)


@app.route('/trend')
def trend():
    return render_template('trend.html')


@app.route('/finance')
def finance():
    return render_template('finance.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404