import re
import requests
import json
from difflib import SequenceMatcher
from elasticsearch import Elasticsearch, RequestsHttpConnection
from middleware.log import logger

from .config import ELASTIC_USER, ELASTIC_PASSWORD, EXTENSIVE_LOG

host = 'knowledge-elastic-1.newsai.org'

es = Elasticsearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=(ELASTIC_USER, ELASTIC_PASSWORD),
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)


def es_link_clean(text):
    text = re.sub(r"(?:\@|https?\://)\S+", "", text)
    text = re.sub(r'[^\w]', ' ', text)
    return text


def text_similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


def find_similar_tweets_in_elastic(elastic_data):
    clean_link = es_link_clean(elastic_data['text'])
    es_data = es.search(index='twitter', doc_type='tweet', body={
                        "query": {"match_all": {}}}, q=clean_link)
    if es_data['hits']['total'] > 0:
        return (True, es_data)
    else:
        return (False, None)


def has_tweet_been_added(elastic_data):
    es_data = es.search(index='twitter', doc_type='tweet', body={
                        "query": {"match_all": {}}}, q=elastic_data['id'])
    if 'hits' in es_data and 'total' in es_data['hits'] and es_data['hits']['total'] > 0:
        return True
    else:
        return False


def add_tweet_to_elastic(elastic_data):
    if EXTENSIVE_LOG:
        logger.debug('Adding tweet: ' + elastic_data['title'])

    if not has_tweet_been_added(elastic_data):
        found_similar_tweet, tweets = find_similar_tweets_in_elastic(
            elastic_data)
        to_add = True
        if found_similar_tweet:
            if 'hits' in tweets and 'hits' in tweets['hits']:
                similarity = text_similarity(tweets['hits']['hits'][0]['_source'][
                    'text'], elastic_data['text'])
                if similarity > 0.70:
                    new_data = tweets['hits']['hits'][0]['_source']
                    new_data['id'].append(str(elastic_data['id'][0]))
                    new_data['similar_tweets'] += 1
                    new_data['meta'][
                        'retweet_count'] += elastic_data['meta']['retweet_count']
                    new_data['meta'][
                        'favorite_count'] += elastic_data['meta']['favorite_count']
                    res = es.index(index="twitter", doc_type='tweet', id=tweets[
                                   'hits']['hits'][0]['_id'], body=new_data)
                    to_add = False
        if to_add:
            res = es.index(index="twitter", doc_type='tweet',
                           body=elastic_data)
