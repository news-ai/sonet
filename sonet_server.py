#!/usr/bin/env python
from sonet import collect


def begin_collecting(articles):
    collect.collect_for_url('http://www.nytimes.com/2016/02/07/world/africa/released-from-guantanamo-but-in-legal-limbo-in-morocco.html', 'Released From Guantanamo, but in Legal Limbo in Morocco')

if __name__ == "__main__":
    articles = collect.initialize()
    if articles:
        begin_collecting(articles)
