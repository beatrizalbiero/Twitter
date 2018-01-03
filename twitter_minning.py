#!/usr/bin/env python
# -*- coding: utf-8 -*-
from TwitterAPI import TwitterAPI
import time

'''
Keys so you can '"download" tweets. You must create a twitter account and go to 
https://developer.twitter.com/en/apply-for-access so you can get access to your keys.
'''
CONSUMER_KEY ='Your CONSUMER_KEY'
CONSUMER_SECRET='Your CONSUMER_SECRET'
ACCESS_TOKEN_KEY='Your ACCESS_TOKEN_KEY'
ACCESS_TOKEN_SECRET='Your ACCESS_TOKEN_SECRET'

TRACK_TERM = '#McDonalds' #some topic of your interest

api = TwitterAPI(CONSUMER_KEY, 
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)

r = api.request('statuses/filter', {'track':TRACK_TERM})
now = time.time()
future = now + 30
for item in r:
    try:
        tweeted_at = item['retweeted_status']['created_at']
    except:
        tweeted_at = ''
    try:
        text = item['retweeted_status']['text']
    except:
        text = ''
    try:
        retweets = item['retweeted_status']['retweet_count']
    except:
        retweets = ''
    try:
        followers = item['entities']['retweeted_status']['user']['followers_count']
    except:
        followers = ''
    try:
        idiom = item['entities']['retweeted_status']['user']['lang']
    except:
        idiom = ''
    try:
        favorites = item['entities']['retweeted_status']['user']['lang']['favourites_count']
    except:
        favorites = ''

    with open("info_tweets.csv","w") as info:
        info.write(str(tweeted_at) + ';' + text + ';' + str(retweets) + ';' + str(followers) + ';' + idiom + ';' + str(favorites) + '\n')
    info.close()

    if time.time < future:
        break
