# -*- coding:utf-8 -*-

import sys
import os.path
import json
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

twitter = OAuth1Session(access_key, access_secret,
                        consumer_key, consumer_secret)

url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {u'q': u'seattle', u'count': 10}
tweets = twitter.get(url, params=params)

search_timeline = json.loads(tweets.text)
for tweet in search_timeline['statuses']:
    print(tweet['user']['name'] + '::' + tweet['text'])
    print(tweet['created_at'])
    print('----------------------------------------------------')
