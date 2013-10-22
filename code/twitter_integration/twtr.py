from twython import Twython
import ConfigParser
import io

# reading twitter data from config file
# Default path is '.'i aka open needs the full path from home.
conf = open('ntnu/master/code/twitter_integration/auth.cfg', 'r').read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(conf))

# configuration of twitter connection data.
APP_KEY = config.get('twtrauth', 'app_key')
APP_SECRET = config.get('twtrauth', 'app_secret')
OAUTH_TOKEN = config.get('twtrauth', 'oauth_token')
OAUTH_TOKEN_SECRET = config.get('twtrauth', 'oauth_token_secret')

# authentication on twitter.
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def credentials():
    credentials = twitter.verify_credentials()
    return credentials

def timeline():
    timeline = twitter.get_home_timeline()
    return timeline

# Executing a search term(unicode string).
def search(term):
    result = twitter.search(q=term)
    return result
