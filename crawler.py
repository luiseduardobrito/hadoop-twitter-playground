#!/usr/bin/env python
import json
import os, tweepy, time, sys, re
from tweepy import OAuthHandler
from unicodedata import normalize


# Consumer key, consumer secret, access token, access secret.
ckey = os.environ["TWITTER_CONSUMER_KEY"]
csecret = os.environ["TWITTER_CONSUMER_SECRET"]
atoken = os.environ["TWITTER_ACCESS_TOKEN"]
asecret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

class Crawler():

    # Initialize the crawler
    def __init__(self, api, q):
        self.query = q
        self.max = 100
        self.count = 0

        for tweet in self.limit_handled(tweepy.Cursor(api.search, q=self.query).items()):

            self.count += 1
            print(self.normalize(tweet.text) + "\n")

            if self.count > self.max:
                sys.exit()

    # In this example, the handler is time.sleep(15 * 60),
    # but you can of course handle it in any way you want.
    def limit_handled(self, cursor):
        while True:
            try:
                yield cursor.next()
            except tweepy.RateLimitError:
                time.sleep(15 * 60)

    # Normalize the text replacing special characters
    def normalize(self, txt):
        return re.sub(r'([^\s\w]|_)+', '', normalize('NFKD', txt))


# Authenticate in Twitter API
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

# Construct the API instance
api = tweepy.API(auth)

# Construct the Crawler instance
crawler = Crawler(api, "temer")