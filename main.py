import time
import wikiquotes
import tweepy
from textblob import TextBlob

#Configuration 
consumer_key = '9HWO8diVfDlQdUMOtyag3wNFv'
consumer_secret = 'TlNlLFgis6tK7vBxY7MzTNnruc11j49IdQE3n2RHJQdb6cCyYa'
access_token = '772860297744875520-MIp1xxzLGefn8qeDA9EnpZIVLQhfmsN'
access_token_secret = 'aq5fXQJl6NMXpX7XLn0MAdSF4rBeKJYGpxgEynuri7KVd'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


#Re-tweet 
# public_tweets = api.search('Jobs South Africa')

# for tweet in public_tweets:
#     api.retweet(tweet.id)
#     time.sleep(20)


#follow people
# for tweet in public_tweets:
#     if api.exists_friendship(tweet.id, tweet.id):
#         pass
#     else:
#         api.create_friendship(tweet.id)
#         time.sleep(20)

# print(api.me())