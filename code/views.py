from flask import render_template
from app import app

@app.route('/')
def homepage():
    return render_template('main.html')

# routes to be created

# API routes to be created


@app.errorhandler(404)
def page_not_found(error):
    print error
    return render_template('page_not_found.html'), 404