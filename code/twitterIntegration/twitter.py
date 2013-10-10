from twython import Twython

#APP_KEY = 'YOUR_APP_KEY'
#APP_SECRET = 'YOUR_APP_SECRET'

APP_KEY = 'f7Yz3vVRSW8XPDRX5ph5xA'
APP_SECRET = 'u3XLwUsrqt6X2vNNbYVCQnau6RdUs7u0qv4f3jg'
OAUTH_TOKEN = '380036002-CwCObamKshJ7F0iztRUrrDSjNbZKAOVJVuQCGb0l'
OAUTH_TOKEN_SECRET = 'Ijzh3LIzHNvQa9ViahAskNJmndOj28OlZyFCJixm8sM'

def getTweet():
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    return twitter.verify_credentials()
