from twython import Twython
import ConfigParser
import io

# reading twitter twitter from config file
# Default path is '.'i aka open needs the full path from home.
conf = open('/home/kiro/ntnu/master/code/twitter_integration/auth.cfg', 'r').read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(conf))

# configuration of twitter connection twitter.
APP_KEY = config.get('twtrauth', 'app_key')
APP_SECRET = config.get('twtrauth', 'app_secret')
OAUTH_TOKEN = config.get('twtrauth', 'oauth_token')
OAUTH_TOKEN_SECRET = config.get('twtrauth', 'oauth_token_secret')

# authentication on twitter.
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


def get_credentials():
    credentials = twitter.verify_credentials()
    return credentials


def get_timeline():
    timeline = twitter.get_home_timeline()
    return timeline


# Executing a search term(unicode string).
# TODO term default should be something intuitive.
def search(term='NTNU'):
    result = twitter.search(q=term)
    return result
