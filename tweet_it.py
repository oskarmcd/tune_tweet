import tweepy

auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')


def tweet_song(tweet):
    api = tweepy.API(auth)
    status = api.update_status(tweet)
