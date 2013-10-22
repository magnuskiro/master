from flask import Flask, render_template
from twitter_integration import twtr
from data_mining import mining_operations

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/data/')
@app.route('/data/<term>')
def get_latest_data(term=None):
    return str(mining_operations.search(term=term))

@app.route('/twtr/search/')
@app.route('/twtr/search/<term>')
def search(term="NTNU"):
    return str(twtr.search(term=term))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

# starting the app.
if __name__ == '__main__':
    #app.run()
    app.run(debug=True)

