class Tweet(object):
    """docstring for Tweet"""

    def tweet_to_class(self, tweet):
        print 'g'

    def __init__(self, tweet):
        super(Tweet, self).__init__()
        self.tweet = self.tweet_to_class(tweet)
