#!/usr/bin/env python
from sonet import collect


def begin_collecting(articles):
    for article in articles:
        collect.collect_for_url(article[0], article[1])

if __name__ == "__main__":
    articles = collect.initialize()
