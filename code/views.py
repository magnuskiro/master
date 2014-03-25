
import ast
import random
from flask import render_template, request, json
from werkzeug.utils import redirect
from app import app
from classification import classifier
from models import Tweet
from twitter import data_controller


@app.route('/grap_data_point')
def trend_data():
    """
    Returns the json object that represents a data point i the trend graph.
    @return: a json object
    """
#- innhente finnansdata
#    - volume
#    - pris

    positive_tweets = str(len(Tweet.query.filter_by(classified_polarity=True).all())) + " / " + str(
        len(Tweet.query.filter_by(manual_polarity=True).all()))
    negative_tweets = str(len(Tweet.query.filter_by(classified_polarity=False).all())) + " / " + str(
        len(Tweet.query.filter_by(manual_polarity=False).all()))
    return "{ trend: { date : 15-01-14, sentiment-value : 401, stock-value : 405 } }"


@app.route('/manual_classification', methods=['POST'])
def manual_classification():
    """
    Stores the manual input of tweet polarity. positive or negative.
    @return: redirect back to previous page.
    """
    assert request.path == '/manual_classification'
    assert request.method == 'POST'
    tweet = Tweet.query.get(request.form['id'])
    tweet.manual_polarity = ast.literal_eval(request.form['polarity'])
    #print request.form['polarity']
    data_controller.save_tweet(tweet)
    return redirect("/sentiment", code=302)


@app.route('/dataset', methods=['POST'])
def create_new_data_set():
    """
    @return:
    """
    assert request.path == '/dataset'
    assert request.method == 'POST'
    query = request.form['query']
    if "Twitter search Query" not in query:
        data_controller.create_new_data_set(query)
    return redirect("/tweets", code=302)


@app.route('/classify/<string:dataset>')
def classify(dataset):
    """
    Runs the classification process that gets the sentiment from tweets.
    @return:
    """
    # todo fix classification datetime for each dataset.
    tweet_list = data_controller.load_tweets_from_file(dataset)
    tweets = []
    for tweet in tweet_list:
        # classify the tweet
        tweet = classifier.classify(Tweet(tweet))
        #print classified_tweet.id, ":", classified_tweet.polarity

        #print len(tweets)
        tweets.append(tweet)

    data_controller.save_tweets(tweets)
#    return redirect("/tweets", code=302)
    return "classification complete: " + dataset


# Regular html routes, returning html/js only
@app.route('/')
def homepage():
    """
    the main entry point to the webapp /
    @return:
    """
    return render_template('main.html')


@app.route('/tweets')
def tweets():
    # todo add metadata to the template
    """
    The page where we view and create collection of tweets.
    @return:
    """
    datasets = data_controller.get_data_set_names()
    return render_template('tweets.html', datasets=datasets)


def calculate_accuracy():
    """
    calculates the accuracy of the polarity classification as of now.
    @return:
    """
    correct = 0
    all_tweets = Tweet.query.all()

    for tweet in all_tweets:
        if (not tweet.classified_polarity is None and not tweet.manual_polarity is None) and \
                (tweet.classified_polarity == tweet.manual_polarity):
            correct += 1

    #print "correct: " + str(correct) + " - all: " + str(len(all_tweets))
    if len(all_tweets) == 0 or correct == 0:
        return 0
    return correct / float(len(all_tweets))


@app.route('/sentiment')
def sentiment():
    """
    Views the sentiment page with a tweet and its sentiment classification.
    @return:
    """
    tweet = data_controller.get_random_unclassified_tweet()
    if tweet is None:
        tweet = Tweet(ast.literal_eval(
            '''{  u'text': u'There are no unclassified tweets',
            u'id': 0, u'created_at': u'Thu Nov 28 19:18:12 +0000 2013'}'''))

    num_tweets = len(Tweet.query.all())
    manually_classified_tweets = len(Tweet.query.filter_by(manual_polarity=True).all()) + len(
        Tweet.query.filter_by(manual_polarity=False).all())
    positive_tweets = str(len(Tweet.query.filter_by(classified_polarity=True).all())) + " / " + str(
        len(Tweet.query.filter_by(manual_polarity=True).all()))
    negative_tweets = str(len(Tweet.query.filter_by(classified_polarity=False).all())) + " / " + str(
        len(Tweet.query.filter_by(manual_polarity=False).all()))
    accuracy = float(calculate_accuracy())
    statistics = {'num_tweets': num_tweets,
                  'manually_classified_tweets': manually_classified_tweets,
                  'positive_tweets': positive_tweets,
                  'negative_tweets': negative_tweets,
                  'accuracy': accuracy}

    example = '''{u'contributors': None, u'truncated': False, u'text': u"Venezuela central bank denies transactions with Wall Street: Venezuela's central bank president denied on Thur... http://t.co/Zs9IXzDMuy", u'in_reply_to_status_id': None, u'id': 406139574092455936, u'favorite_count': 0, u'source': u'<a href="http://twitterfeed.com" rel="nofollow">twitterfeed</a>', u'retweeted': False, u'coordinates': None, u'entities': {u'symbols': [], u'user_mentions': [], u'hashtags': [], u'urls': [{u'url': u'http://t.co/Zs9IXzDMuy', u'indices': [114, 136], u'expanded_url': u'http://yhoo.it/1iXfyOw', u'display_url': u'yhoo.it/1iXfyOw'}]}, u'in_reply_to_screen_name': None, u'in_reply_to_user_id': None, u'retweet_count': 0, u'id_str': u'406139574092455936', u'favorited': False, u'user': {u'follow_request_sent': False, u'profile_use_background_image': True, u'contributors_enabled': False, u'id': 2211968749, u'verified': False, u'profile_text_color': u'333333', u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/378800000782570899/e333fe58fe55038f02bc41c179318dab_normal.jpeg', u'profile_sidebar_fill_color': u'EFEFEF', u'entities': {u'description': {u'urls': []}}, u'followers_count': 246, u'profile_sidebar_border_color': u'FFFFFF', u'location': u'Jakarta, ID', u'default_profile_image': False, u'id_str': u'2211968749', u'utc_offset': None, u'statuses_count': 5413, u'description': u'light as air, soft as feathers, calm like water, angry like fire, still as the earth, and I was like that', u'friends_count': 16, u'profile_link_color': u'FF0000', u'profile_image_url': u'http://pbs.twimg.com/profile_images/378800000782570899/e333fe58fe55038f02bc41c179318dab_normal.jpeg', u'notifications': False, u'geo_enabled': False, u'profile_background_color': u'642D8B', u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/2211968749/1385272996', u'profile_background_image_url': u'http://a0.twimg.com/profile_background_images/378800000123761396/d534bacab5afe04bc652ebe621e187c0.jpeg', u'screen_name': u'SahlJr', u'lang': u'en', u'following': False, u'profile_background_tile': True, u'favourites_count': 2, u'name': u'Sahl As-Siroj Jr.', u'url': None, u'created_at': u'Sun Nov 24 05:54:07 +0000 2013', u'profile_background_image_url_https': u'https://si0.twimg.com/profile_background_images/378800000123761396/d534bacab5afe04bc652ebe621e187c0.jpeg', u'time_zone': None, u'protected': False, u'default_profile': False, u'is_translator': False, u'listed_count': 0}, u'geo': None, u'in_reply_to_user_id_str': None, u'possibly_sensitive': False, u'lang': u'en', u'created_at': u'Thu Nov 28 19:16:34 +0000 2013', u'in_reply_to_status_id_str': None, u'place': None, u'metadata': {u'iso_language_code': u'en', u'result_type': u'recent'}} '''
    return render_template('sentiment.html', tweet_id=tweet.id, tweet_text=tweet.sanitized_text, tweet_example=example, statistics=statistics)


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
    return render_template('page_not_found.html'), 404

# Test methods:


@app.route('/test_save')
def test_save():
    """
    Test method for testing database connection and saving to the database.
    @return:
    """
    t = '''{u'contributors': None, u'truncated': False, u'text': u'RT @MattGranite: ALMOST EVERY BIG #BlackFriday deal online.. + doorbusters can be found right here. Amazing huge #Ways2Save Part #1: http:/\u2026', u'in_reply_to_status_id': None, u'id': 406139983032897536, u'favorite_count': 0, u'source': u'<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>', u'retweeted': False, u'coordinates': None, u'entities': {u'symbols': [], u'user_mentions': [{u'indices': [3, 15], u'screen_name': u'MattGranite', u'id': 383511120, u'name': u'Matt Granite', u'id_str': u'383511120'}], u'hashtags': [{u'indices': [34, 46], u'text': u'BlackFriday'}, {u'indices': [113, 123], u'text': u'Ways2Save'}], u'urls': []}, u'in_reply_to_screen_name': None, u'in_reply_to_user_id': None, u'retweet_count': 7, u'id_str': u'406139983032897536', u'favorited': False, u'retweeted_status': {u'contributors': None, u'truncated': False, u'text': u'ALMOST EVERY BIG #BlackFriday deal online.. + doorbusters can be found right here. Amazing huge #Ways2Save Part #1: http://t.co/pUXYoQBNTe', u'in_reply_to_status_id': None, u'id': 406047299597389824, u'favorite_count': 9, u'source': u'web', u'retweeted': False, u'coordinates': None, u'entities': {u'symbols': [], u'user_mentions': [], u'hashtags': [{u'indices': [17, 29], u'text': u'BlackFriday'}, {u'indices': [96, 106], u'text': u'Ways2Save'}], u'urls': [{u'url': u'http://t.co/pUXYoQBNTe', u'indices': [116, 138], u'expanded_url': u'http://www.wkyc.com/story/money/personal-finance/ways-to-save/2013/11/27/2013-black-friday-deals/3738039/', u'display_url': u'wkyc.com/story/money/pe\u2026'}]}, u'in_reply_to_screen_name': None, u'in_reply_to_user_id': None, u'retweet_count': 7, u'id_str': u'406047299597389824', u'favorited': False, u'user': {u'follow_request_sent': False, u'profile_use_background_image': True, u'id': 383511120, u'verified': True, u'profile_text_color': u'333333', u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/1588691893/twitter_normal.jpg', u'profile_sidebar_fill_color': u'DDEEF6', u'is_translator': False, u'geo_enabled': False, u'entities': {u'url': {u'urls': [{u'url': u'http://t.co/jX0SNnRUej', u'indices': [0, 22], u'expanded_url': u'http://www.mattgranite.com', u'display_url': u'mattgranite.com'}]}, u'description': {u'urls': []}}, u'followers_count': 49334, u'protected': False, u'location': u'Say hello to deals!', u'default_profile_image': False, u'id_str': u'383511120', u'utc_offset': -18000, u'statuses_count': 23389, u'description': u'Host of #Ways2Save on the TV and @USATodayVideo. I exist only to share my frugality with you.', u'friends_count': 395, u'profile_link_color': u'0084B4', u'profile_image_url': u'http://pbs.twimg.com/profile_images/1588691893/twitter_normal.jpg', u'notifications': False, u'profile_background_image_url_https': u'https://si0.twimg.com/profile_background_images/339738141/saving-money-during-hard-financial-times-01-af.jpg', u'profile_background_color': u'C0DEED', u'profile_background_image_url': u'http://a0.twimg.com/profile_background_images/339738141/saving-money-during-hard-financial-times-01-af.jpg', u'name': u'Matt Granite', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 2482, u'screen_name': u'MattGranite', u'url': u'http://t.co/jX0SNnRUej', u'created_at': u'Sun Oct 02 01:04:40 +0000 2011', u'contributors_enabled': False, u'time_zone': u'Eastern Time (US & Canada)', u'profile_sidebar_border_color': u'C0DEED', u'default_profile': False, u'following': False, u'listed_count': 111}, u'geo': None, u'in_reply_to_user_id_str': None, u'possibly_sensitive': False, u'lang': u'en', u'created_at': u'Thu Nov 28 13:09:54 +0000 2013', u'in_reply_to_status_id_str': None, u'place': None, u'metadata': {u'iso_language_code': u'en', u'result_type': u'recent'}}, u'user': {u'follow_request_sent': False, u'profile_use_background_image': True, u'id': 2182758172, u'verified': False, u'profile_text_color': u'333333', u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/378800000745726018/07d07d9a8cf0dd12bd9567fc1d2a4028_normal.jpeg', u'profile_sidebar_fill_color': u'DDEEF6', u'is_translator': False, u'geo_enabled': False, u'entities': {u'description': {u'urls': []}}, u'followers_count': 1, u'protected': False, u'location': u'', u'default_profile_image': False, u'id_str': u'2182758172', u'utc_offset': None, u'statuses_count': 80, u'description': u'', u'friends_count': 12, u'profile_link_color': u'0084B4', u'profile_image_url': u'http://pbs.twimg.com/profile_images/378800000745726018/07d07d9a8cf0dd12bd9567fc1d2a4028_normal.jpeg', u'notifications': False, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme1/bg.png', u'profile_background_color': u'C0DEED', u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/2182758172/1384576846', u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme1/bg.png', u'name': u'Kenya Watson', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 2, u'screen_name': u'KWatsonBrown', u'url': None, u'created_at': u'Sat Nov 16 04:34:22 +0000 2013', u'contributors_enabled': False, u'time_zone': None, u'profile_sidebar_border_color': u'C0DEED', u'default_profile': True, u'following': False, u'listed_count': 0}, u'geo': None, u'in_reply_to_user_id_str': None, u'lang': u'en', u'created_at': u'Thu Nov 28 19:18:12 +0000 2013', u'in_reply_to_status_id_str': None, u'place': None, u'metadata': {u'iso_language_code': u'en', u'result_type': u'recent'}}'''
    t = ast.literal_eval(t)
    t = Tweet(t)
    data_controller.save_tweet(t) # should store a tweet in the db if it's not there already
    t2 = '''{u'contributors': None, u'truncated': False, u'text': u'#hot #finance #news When rates are low, your nest egg suffers http://t.co/kYJYO6eZYs http://t.co/O1BULv4nUm #socialshakeup', u'in_reply_to_status_id': None, u'id': 406139865755947009, u'favorite_count': 0, u'source': u'<a href="http://dlvr.it" rel="nofollow">dlvr.it</a>', u'retweeted': False, u'coordinates': None, u'entities': {u'symbols': [], u'user_mentions': [], u'hashtags': [{u'indices': [0, 4], u'text': u'hot'}, {u'indices': [5, 13], u'text': u'finance'}, {u'indices': [14, 19], u'text': u'news'}, {u'indices': [108, 122], u'text': u'socialshakeup'}], u'urls': [{u'url': u'http://t.co/kYJYO6eZYs', u'indices': [62, 84], u'expanded_url': u'http://bit.ly/InEX5G', u'display_url': u'bit.ly/InEX5G'}, {u'url': u'http://t.co/O1BULv4nUm', u'indices': [85, 107], u'expanded_url': u'http://bit.ly/15Jngnf', u'display_url': u'bit.ly/15Jngnf'}]}, u'in_reply_to_screen_name': None, u'in_reply_to_user_id': None, u'retweet_count': 0, u'id_str': u'406139865755947009', u'favorited': False, u'user': {u'follow_request_sent': False, u'profile_use_background_image': True, u'default_profile_image': False, u'id': 23165988, u'verified': False, u'profile_text_color': u'666666', u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/378800000340696391/a7aba11b57386e8b8f2bf7f6638a9ff5_normal.jpeg', u'profile_sidebar_fill_color': u'252429', u'entities': {u'url': {u'urls': [{u'url': u'http://t.co/MsoqLpo34h', u'indices': [0, 22], u'expanded_url': u'http://watchinga.com', u'display_url': u'watchinga.com'}]}, u'description': {u'urls': []}}, u'followers_count': 1581, u'profile_sidebar_border_color': u'000000', u'id_str': u'23165988', u'profile_background_color': u'1A1B1F', u'listed_count': 39, u'profile_background_image_url_https': u'https://si0.twimg.com/profile_background_images/378800000086938815/e1b82b2220649732ee700a0fc0f30ed9.jpeg', u'utc_offset': -28800, u'statuses_count': 164063, u'description': u"#hot #nowreading Watching the world 24/7. And bringing it to you. Follow this account to keep up with what's #trending across the Internet. #news #video", u'friends_count': 1641, u'location': u'Los Angeles, CA', u'profile_link_color': u'C29C06', u'profile_image_url': u'http://pbs.twimg.com/profile_images/378800000340696391/a7aba11b57386e8b8f2bf7f6638a9ff5_normal.jpeg', u'following': False, u'geo_enabled': False, u'profile_background_image_url': u'http://a0.twimg.com/profile_background_images/378800000086938815/e1b82b2220649732ee700a0fc0f30ed9.jpeg', u'screen_name': u'WatchingaBuzz', u'lang': u'en', u'profile_background_tile': True, u'favourites_count': 57, u'name': u'WatchingaBuzz', u'notifications': False, u'url': u'http://t.co/MsoqLpo34h', u'created_at': u'Sat Mar 07 04:48:38 +0000 2009', u'contributors_enabled': False, u'time_zone': u'Pacific Time (US & Canada)', u'protected': False, u'default_profile': False, u'is_translator': False}, u'geo': None, u'in_reply_to_user_id_str': None, u'possibly_sensitive': False, u'lang': u'en', u'created_at': u'Thu Nov 28 19:17:44 +0000 2013', u'in_reply_to_status_id_str': None, u'place': None, u'metadata': {u'iso_language_code': u'en', u'result_type': u'recent'}}'''
    t2 = ast.literal_eval(t2)
    data_controller.save_tweet(t2)   # should print "not a tweet metadata object"
    t2 = Tweet(t2)
    data_controller.save_tweet(t2) # should store a tweet in the db if it's not there already
    return "saved to db"


@app.route('/test_load')
def test_load():
    """
    Test method for getting a tweet fro mthe database.
    @return:
    """
    tweet = data_controller.get_random_tweet()
    return str(tweet.id) + ":" + str(tweet.manual_polarity)
