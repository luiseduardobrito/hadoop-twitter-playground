import os
import json

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#consumer key, consumer secret, access token, access secret.
ckey = os.environ["TWITTER_CONSUMER_KEY"]
csecret = os.environ["TWITTER_CONSUMER_SECRET"]
atoken = os.environ["TWITTER_ACCESS_TOKEN"]
asecret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

class listener(StreamListener):

    def on_data(self, data):
        parsed_json = json.loads(data)
        print("@" + parsed_json["user"]["screen_name"] + ": " + parsed_json["text"] + "\n")
        return(True)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["olympics"])
