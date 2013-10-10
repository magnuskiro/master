from flask import Flask
from twitterIntegration import twitter

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/description')
def description():
    return 'description'

@app.route('/twtr/me')
def getTweet():
    cont = twitter.getTweet()
    return str(cont)


# starting the app.
if __name__ == '__main__':
    app.run()

