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
        self.id = [str(tweet['id'])]
        self.text = tweet['text']
        self.meta['favorite_count'] = tweet['favorite_count']
        self.meta['retweet_count'] = tweet['retweet_count']
        self.location = tweet['coordinates']
        self.language = tweet['lang']

        self.initial_user['id'] = tweet['user']['id']
        self.initial_user['verified'] = tweet['user']['verified']
        self.initial_user['followers_count'] = tweet['user']['followers_count']
        self.initial_user['time_zone'] = tweet['user']['time_zone']
        self.initial_user['lang'] = tweet['user']['lang']

        self.article_url = article_url

    def __init__(self, tweet, article_url):
        super(Tweet, self).__init__()

        # Basic information about the tweet
        self.id = []
        self.text = ""
        self.meta = {}
        self.location = None
        self.language = ""
        self.article_url = ""
        self.similar_tweets = 0

        # User information about the tweet
        self.initial_user = {}
