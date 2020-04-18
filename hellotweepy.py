import tweepy

auth = tweepy.OAuthHandler('wnHnUjjJVfGKIkjgAlAWIX7Ii', 'hLcXusk6opqfFJETXJAF4dzMx5x8Pr4v0TH22cGwY5SMRHPJhU')
auth.set_access_token('54509995-ZTtceIZD0esJ57apOshkRK5O8tKCeGCa82x7p7osF', 'Pnbrj0tapaPHBeGGShASEccBtrPIibEyVa1TgYnZW4MOq')

 

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)