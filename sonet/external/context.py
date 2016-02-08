import requests
import json
from middleware.config import CONTEXT_API_USERNAME, CONTEXT_API_PASSWORD

requests.packages.urllib3.disable_warnings()


def get_article_urls():
    headers = {
        'content-type': 'application/json',
        'accept': 'application/json',
    }

    payload = {
        'username': CONTEXT_API_USERNAME,
        'password': CONTEXT_API_PASSWORD,
    }

    r = requests.post('https://context.newsai.org/api/jwt-token/',
                      headers=headers, data=json.dumps(payload), verify=False)
    data = json.loads(r.text)
    token = data['token']

    headers = {
        'content-type': 'application/json',
        'accept': 'application/json',
        'authorization': 'JWT ' + token
    }

    r = requests.get('https://context.newsai.org/api/articles/',
                     headers=headers, verify=False)
    data = json.loads(r.text)
    articles = []
    for article in data['results']:
        articles.append((article['url'].encode('utf8'),
                         article['name'].encode('utf8')))
    return articles
