#!/usr/bin/env python
import sys

from sonet.collect import initialize, collect_for_url
from middleware import esclient


def begin_collecting(articles):
    for article in articles:
        collect_for_url(article[0], article[1])
    return

if __name__ == "__main__":
    articles = initialize()
    if articles:
        begin_collecting(articles)
