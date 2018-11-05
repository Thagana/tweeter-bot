import time
import wikiquotes
import tweepy
import config
# from textblob import TextBlob

#Configuration 
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token  = config.access_token
access_token_secret = config.access_token_secret

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#List of Speakers
leaders = ['Eric Thomas', 'Tony Rob','Nelson Mandela','Zig Ziglar','Jim Rohn', 'Wayne Dyer','Robin Sharman','Brian Tracy']

try:
    for leader in leaders:
        quote = wikiquotes.get_quotes(leader, 'english')
        for index in range(0,len(quote)):
            data = wikiquotes.get_quotes(leader, 'english')[index] + ' -~ '+ leader
            info = (data[:270] + '...') if len(data) > 75 else data
            api.update_status(info)
            time.sleep(86400)
            
except Exception as e:
    print('Error:' + str(e))