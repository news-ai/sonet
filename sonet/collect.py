from external import context, twitter


def initialize():
    print context.get_article_urls()


def begin_collection(url, title):
    tweets = twitter.search_tweets([title, url])
    for tweet in tweets:
        print tweet
