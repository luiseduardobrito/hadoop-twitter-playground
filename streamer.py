#!/usr/bin/env python

import os, sys, json, re

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

# Consumer key, consumer secret, access token, access secret.
ckey = os.environ["TWITTER_CONSUMER_KEY"]
csecret = os.environ["TWITTER_CONSUMER_SECRET"]
atoken = os.environ["TWITTER_ACCESS_TOKEN"]
asecret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]


class listener(StreamListener):

    def __init__(self):
        self.max = 10
        self.count = 0

    def on_data(self, data):
        self.count += 1
        parsed_json = json.loads(data)
        print(re.sub(r'([^\s\w]|_)+', '', parsed_json["text"]) + "\n")

        if self.count > self.max:
            sys.exit()
        else:
            return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

query = "temer"
print("Listening for new tweets with query: " + query)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=[query])
