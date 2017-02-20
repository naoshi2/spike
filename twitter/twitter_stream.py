# -*- coding:utf-8 -*-

from twitter import *
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('key')

access_key = parser.get('key', 'access_key')
access_secret = parser.get('key', 'access_secret')
consumer_key = parser.get('key', 'consumer_key')
consumer_secret = parser.get('key', 'consumer_secret')

auth = OAuth(consumer_key, consumer_secret, access_key, access_secret)

t = TwitterStream(auth = auth)
tweets = t.statuses.filter(track = "Seattle")

for tweet in tweets:
    print tweet["text"].encode('utf_8')
