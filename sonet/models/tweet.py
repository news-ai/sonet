from middleware.database import db


class Tweet(object):
    """docstring for Tweet"""

    def __repr__(self):
        return '<Tweet by {0}>'.format(self.user['id'])

    def __str__(self):
        return self.text.encode('utf8')

    def tweet_to_json(self):
        return self.__dict__

    def tweet_to_mongo(self):
        tweet = self.tweet_to_json()

    def tweet_to_class(self, tweet, article_url):
        self.id = tweet['id']
        self.text = tweet['text']
        self.meta['favorite_count'] = tweet['favorite_count']
        self.meta['retweet_count'] = tweet['retweet_count']
        self.coordinates = tweet['coordinates']
        self.language = tweet['lang']

        self.user['id'] = tweet['user']['id']
        self.user['verified'] = tweet['user']['verified']
        self.user['followers_count'] = tweet['user']['followers_count']
        self.user['time_zone'] = tweet['user']['time_zone']
        self.user['lang'] = tweet['user']['lang']

        self.article_url = article_url

    def __init__(self, tweet, article_url):
        super(Tweet, self).__init__()

        # Basic information about the tweet
        self.id = 0
        self.text = ""
        self.meta = {}
        self.coordinates = None
        self.language = ""
        self.article_url = ""

        # User information about the tweet
        self.user = {}

        # Convert a single tweet into a Tweet class instance
        self.tweet_to_class(tweet, article_url)
        self.tweet_to_mongo()
