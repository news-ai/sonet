#!/usr/bin/env python
import tornado.ioloop
import tornado.web
import json

from sonet import collect
from middleware import database


def begin_collecting(articles):
    for article in articles:
        collect.collect_for_url(article[0], article[1])


class ResourceListHandler(tornado.web.RequestHandler):

    def get(self):
        BASE_URL = self.request.protocol + '://' + self.request.host + '/api'
        resources = {
            'tweets': BASE_URL + '/tweets/',
        }
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(resources))


class TweetHandler(tornado.web.RequestHandler):

    def get(self):
        resources = {}
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(resources))


def make_app():
    return tornado.web.Application([
        (r"/api/?", ResourceListHandler),
        (r"/api/tweets/?", TweetHandler),
    ])

if __name__ == "__main__":
    articles = collect.initialize()
    if articles:
        app = make_app()
        app.listen(8000)
        tornado.ioloop.IOLoop.current().start()
