import pandas as pd
import mysql.connector as msc
import json
import tweepy
import csv
import re
import string

# read config file into JSON object
configFile = open('config.json')
config = json.load(configFile)

# make connection to the GCloud database
db_config = config['database']
connection = msc.connect(
    host=db_config['host'], 
    port=db_config['port'],
    user=db_config['user'],
    password=db_config['password'],
    database=db_config['database']
)

# authorize Twitter app with Tweepy OAuthHandler
twit_config = config['twitter']
auth = tweepy.OAuthHandler(twit_config['api_key'], twit_config['api_key_secret'])
auth.set_access_token(twit_config['access_token'], twit_config['access_token_secret'])
twitapi = tweepy.API(auth, wait_on_rate_limit=True)

# extract Tweets from Malaysian MOH about Malaysian COVID-19 case data
# write to pandas database
tweet_collection = twitapi.search("KKMPutrajaya")
print(tweet_collection.__len__)
