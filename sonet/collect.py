from external import twitter


def begin_collection(url, title):
    tweets = twitter.search_tweets([title, url])
    for tweet in tweets:
        print tweet
