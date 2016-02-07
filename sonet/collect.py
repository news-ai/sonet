from external import context, twitter
from models.tweet import Tweet

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
            print Tweet(single_tweet)
