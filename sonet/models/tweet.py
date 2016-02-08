import json


class Tweet(object):
    """docstring for Tweet"""

    def __repr__(self):
        return '<Tweet by {0}>'.format(self.user['id'])

    def __str__(self):
        return self.text.encode('utf8')

    def tweet_to_dict(self):
        return self.__dict__

    def tweet_to_class(self, tweet, article_url):
        self.id = tweet['id']
        self.text = tweet['text']
        self.meta['favorite_count'] = tweet['favorite_count']
        self.meta['retweet_count'] = tweet['retweet_count']
        self.location = tweet['coordinates']
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
        self.location = None
        self.language = ""
        self.article_url = ""

        # User information about the tweet
        self.user = {}
