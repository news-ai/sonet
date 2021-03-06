from TwitterSearch import *
from middleware.config import SONET_TWTR_CONSUMER_KEY, SONET_TWTR_CONSUMER_SECRET, SONET_TWTR_ACCESS_TOKEN, SONET_TWTR_ACCESS_TOKEN_SECRET
from middleware.log import logger

"""
set_include_entities: Entities provide structured data from Tweets including resolved URLs, media, hashtags and mentions without having to parse the text to extract that information. 
"""


def search_tweets(topics):
    logger.debug('Begin collecting tweets')
    ts = TwitterSearch(
        consumer_key=SONET_TWTR_CONSUMER_KEY,
        consumer_secret=SONET_TWTR_CONSUMER_SECRET,
        access_token=SONET_TWTR_ACCESS_TOKEN,
        access_token_secret=SONET_TWTR_ACCESS_TOKEN_SECRET,
    )
    try:
        tso = TwitterSearchOrder()
        tso.set_keywords(topics)
        tso.set_include_entities(True)
        tweets = ts.search_tweets_iterable(tso)
        logger.debug('Finishing collecting tweets')
        return (tweets, True)
    except TwitterSearchException as e:  # take care of all those ugly errors if there are some
        return (e, False)


def stream_tweets(topics):
    return topics
