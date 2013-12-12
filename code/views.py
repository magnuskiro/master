from flask import render_template
from app import app


# API routes to be created

#
@app.route('/')
def homepage():
    return render_template('main.html')


@app.route('/tweets')
def tweets():
    return render_template('tweets.html')


@app.route('/sentiment')
def sentiment():
    return render_template('sentiment.html')


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
    print error
    return render_template('page_not_found.html'), 404