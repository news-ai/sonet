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


def add_tweet_to_elastic(elastic_data):
    headers = {'content-type': 'application/json'}
    url = 'https://knowledge-elastic-1.newsai.org/twitter/tweet'
    data = requests.post(url, data=json.dumps(
        elastic_data), headers=headers, verify=False)
    print data
