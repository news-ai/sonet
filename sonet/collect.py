from external import context, twitter
from models.tweet import Tweet
from middleware import database

import json


def initialize():
    articles = context.get_article_urls()
    if len(articles) > 0:
        return articles
    return False


def collect_for_url(url, title):
    tweets, success = twitter.search_tweets([title, url])
    if success:
        for single_tweet in tweets:
            tweet = Tweet(single_tweet, url)
            tweet.tweet_to_class(single_tweet, url)
            database.tweet_to_mongo(tweet)
