from flask import render_template
from app import app

from data_mining import mining_operations

@app.route('/')
def homepage():
    return 'Welcome to nothingness'

@app.route('/data/')
def data():
    return str(mining_operations.data())

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404