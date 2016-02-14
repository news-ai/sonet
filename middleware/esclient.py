import re
import requests
import json
from elasticsearch import Elasticsearch, RequestsHttpConnection

from .config import ELASTIC_USER, ELASTIC_PASSWORD

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


def find_similar_tweets_in_elastic(elastic_data):
    clean_link = es_link_clean(elastic_data['text'])
    es_data = es.search(index='twitter', doc_type='tweet', body={
                        "query": {"match_all": {}}}, q=clean_link)
    if es_data['hits']['total'] > 0:
        return (True, es_data)
    else:
        return (False, None)


def add_tweet_to_elastic(elastic_data):
    found_similar_tweet, tweets = find_similar_tweets_in_elastic(elastic_data)
    if found_similar_tweet:
        print 'similar tweet found'
    else:
        res = es.index(index="twitter", doc_type='tweet', id=1, body=elastic_data)
        print res
