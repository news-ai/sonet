from external import context, twitter
from models.tweet import Tweet
from middleware.esclient import add_tweet_to_elastic
from middleware.log import logger

import json


def initialize():
    articles = context.get_article_urls()
    if len(articles) > 0:
        logger.debug('Processing ' + str(len(articles)) + ' articles')
        return articles
    return False


def collect_for_url(url, title):
    tweets, success = twitter.search_tweets([title, url])
    if success:
        logger.debug('Beginning processing data onto ElasticSearch')
        for single_tweet in tweets:
            tweet = Tweet(single_tweet, url)
            tweet.tweet_to_class(single_tweet, url)
            add_tweet_to_elastic(tweet.tweet_to_dict())
        logger.debug('Beginning processing data onto ElasticSearch')
