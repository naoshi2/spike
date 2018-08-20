# -*- coding:utf-8 -*-

import sys
import os.path
from twitter import *
import configparser
from requests_oauthlib import OAuth1Session

filename = 'key'

if not os.path.exists(filename):
    print('File not found : ' + filename)
    sys.exit()

parser = configparser.ConfigParser()
parser.read(filename)

access_key = parser.get('key', 'access_key')
access_secret = parser.get('key', 'access_secret')
consumer_key = parser.get('key', 'consumer_key')
consumer_secret = parser.get('key', 'consumer_secret')

auth = OAuth(consumer_key, consumer_secret,
             access_key, access_secret)

t = TwitterStream(auth=auth)
tweets = t.statuses.filter(track=u"Seattle")

print(tweets)

for tweet in tweets:
    print(tweet["text"].encode('utf_8'))
