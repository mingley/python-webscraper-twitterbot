#thedogtweetbot

import tweepy as tp
import time
import os

#twitter dev keys here
consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token = 'ACCESS_TOKEN'
access_secret = 'ACCESS_SECRET'

#login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

#for loop to iterate through pictures, posts one dog picture every 20 seconds to twitter
os.chdir('dogs')
for dog_image in os.listdir('.'):
    api.upate_with_media(dog_image)
    time.sleep(20)

