import tweepy

auth = tweepy.OAuthHandler('wnHnUjjJVfGKIkjgAlAWIX7Ii', 'hLcXusk6opqfFJETXJAF4dzMx5x8Pr4v0TH22cGwY5SMRHPJhU')
auth.set_access_token('54509995-ZTtceIZD0esJ57apOshkRK5O8tKCeGCa82x7p7osF', 'Pnbrj0tapaPHBeGGShASEccBtrPIibEyVa1TgYnZW4MOq')

api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):


    def on_status(self, status):
        text = "@{} {}".format(status.user.screen_name, status.text.replace('@rtindru', ''))
        print(text)
        print(status.text)
        api.update_status(text, in_reply_to_status_id=status.id)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['@rtindru'])

