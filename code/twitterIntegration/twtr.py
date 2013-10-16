from twython import Twython
import ConfigParser, io

twtr = ''
APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

def configure():
    conf = open('/home/kiro/ntnu/master/code/twitterIntegration/auth.cfg', 'r').read()
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.readfp(io.BytesIO(conf))
    APP_KEY = config.get('twtrauth', 'app_key')
    APP_SECRET = config.get('twtrauth', 'app_secret')
    OAUTH_TOKEN = config.get('twtrauth', 'oauth_token')
    OAUTH_TOKEN_SECRET = config.get('twtrauth', 'oauth_token_secret')

    return Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def credentials():
    twtr = configure()
    credentials = twtr.verify_credentials()
    return credentials

def timeline():
    twtr = configure()
    timeline = twtr.get_home_timeline()
    return timeline

def serach(term):
    twtr = configure()
    result = twtr.search(q=term)
    return result
