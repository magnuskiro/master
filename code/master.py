from flask import Flask
from twitterIntegration import twtr

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/twtr/me')
def me():
    return str(twtr.timeline())

@app.route('/twtr/timeline')
def creds():
    return str(twtr.credentials())

@app.route('/twtr/search/')
@app.route('/twtr/search/<term>')
def search(term=None):
    return str(twtr.serach(term=term))

# starting the app.
if __name__ == '__main__':
    app.run()

