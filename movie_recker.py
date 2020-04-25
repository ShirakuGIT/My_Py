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

def main(user_name="@rtindru"):
    """
    Goal: Searches twitter for the user name "rtindru"
    Input: user_name to search tweets for
    Output: All tweets with the username
    """
    pass

def keyword_search(user_tweet, search_keywords):
    """
    Goal: Does this tweet have the keywords "Recommend" and "Movie"
    Input1: user_tweet to return tweets 
    Input2: search_keywords to return specific keywords  
    Output: True/False
    """
    pass

def get_movie_name():
    pass

def bot_recc():
    """
    Goal: Get recommends from API      
    Input: movie_name provides movie name
    Output: Top 3 best movies

    """
    
    pass

def reply_recc():
    pass
