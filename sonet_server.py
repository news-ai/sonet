#!/usr/bin/env python
import sys

from sonet.collect import initialize, collect_for_url
from middleware import esclient
from middleware.log import logger


def begin_collecting(articles):
    for article in articles:
        logger.debug('Processing article: ' + article[1])
        collect_for_url(article[0], article[1])
        logger.debug('Finishing article: ' + article[1])
    return

if __name__ == "__main__":
    logger.debug('Beginning processing')
    articles = initialize()
    if articles:
        begin_collecting(articles)
        logger.debug('Completed processing')
