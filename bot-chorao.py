from re import search
import tweepy
import time
# Esse Bot irá retwittar todos os posts publicados que contém a palavra "eu chorei"
# Onde possui "***" substituir por suas TOKEN API's
auth = tweepy.OAuthHandler('***', '***')
auth.set_access_token('***', '***')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'eu chorei'
numeroDeTweets = 100

for tweet in tweepy.Cursor(api.search, search).items(numeroDeTweets):
    try:
        print('Tweet retuitado')
        tweet.retweet()
        tweet.favorite()
        time.sleep(60)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
