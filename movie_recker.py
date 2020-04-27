"""
How it works / Logic flow
1a. Bot listens to the keyword "rtindru"
- Tweepy returns list of tweets
1b. Bot checks if the tweet is about "recommend movie"
2. Bot asks the user "what's your favorite movie?" - we got the movie_name inside the main function
- User responds with the movie name
3a.Takes  
3b.Bot gets recommendations from movie api
4. Bot replies to the user with top 2/3 recommendations
"""
import tweepy

auth = tweepy.OAuthHandler('wnHnUjjJVfGKIkjgAlAWIX7Ii', 'hLcXusk6opqfFJETXJAF4dzMx5x8Pr4v0TH22cGwY5SMRHPJhU')
auth.set_access_token('54509995-ZTtceIZD0esJ57apOshkRK5O8tKCeGCa82x7p7osF', 'Pnbrj0tapaPHBeGGShASEccBtrPIibEyVa1TgYnZW4MOq')

api = tweepy.API(auth)


class RecommendStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print("RecommendStreamListener", status.text)
        text = "@{} What's your favorite movie?".format(status.user.screen_name)
        reply = api.update_status(text, in_reply_to_status_id=status.id)
        print("Reply ID", reply.id)


class ResponseStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print("ResponseStreamListener", status.text)


def main():
    """
    Goal: Searches twitter for the user name "rtindru"
    Input: str, user_name to search tweets for
    Output: All tweets with the username
    """
    respStreamListener = ResponseStreamListener()
    respStream = tweepy.Stream(auth = api.auth, listener=respStreamListener, is_async=True)
    respStream.filter(follow=["54509995"])

    recStreamListener = RecommendStreamListener()
    recStream = tweepy.Stream(auth = api.auth, listener=recStreamListener)
    recStream.filter(track=["goosfraba recommendation movie", "@rtindru recommend movie"], is_async=True)


def get_movie_name():
    pass


def bot_recc(movie_name):
    """
    Goal: Get recommends from API      
    Input: str, movie_name provides movie name
    Output: Top 3 best movies

    """
    
    pass

def reply_recc():
    pass


if __name__ == "__main__":
    main()
