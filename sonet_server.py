#!/usr/bin/env python
from sonet.collect import initialize, collect_for_url
from middleware import esclient


def begin_collecting(articles):
    for article in articles:
        collect_for_url(article[0], article[1])

if __name__ == "__main__":
    articles = initialize()
    if articles:
        begin_collecting(articles)
