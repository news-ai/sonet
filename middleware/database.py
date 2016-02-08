from pymongo import MongoClient
from datetime import datetime
from config import SONET_ENVIRONMENT, SONET_MONGO_USER, SONET_MONGO_PASSWORD
import json


if SONET_ENVIRONMENT is 'prod':
    uri = "mongodb://{0}:{1}@10.240.0.4:27017/sonet"
    client = MongoClient(uri.format(SONET_MONGO_USER, SONET_MONGO_PASSWORD))
else:
    client = MongoClient()

db = client.sonet


def get_tweets_by_url(article_url):
    count = db.tweets.count({"article_url": article_url})
    if count > 0:
        tweets = db.tweets.find({"article_url": article_url})
        for tweet in tweets:
            print tweet['name']


def tweet_to_mongo(tweet):
    tweet_id = tweet.id
    tweet = tweet.tweet_to_dict()

    count = db.tweets.count({"id": tweet_id})
    if count is 0:
        result = db.tweets.insert_one(tweet)
