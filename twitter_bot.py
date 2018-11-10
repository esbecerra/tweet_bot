import requests     # an http library written for humans
import tweepy       # tweepy is a twitter api wrapper
import time


consumer_key = 'kGkFCxqU4iOd4Xjqf6uJSddXE'
consumer_secret = 'H2pyH3KnDkcqcF2cAU2MYeN2Ua1eucmnTq2hKDJhE5rLbsswaO'
access_token = '1060959782947844096-SYXVwMKt4yKbeUFrWapCh0g1wBSaVY'
access_token_secret = 'm8txm04kzr4PU4xD7AY64WdvB8GDxahYVP2wc4Htv7voL'

# Twitter requires oAuth2 to access its API:
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)  # creates an object called api

# rapidAPI to get access to the Random Quote Generator
api_key = 'nK6l1pAhemmshKaMK0sF8KQbgBHWp1ggsr5jsn3vFt4kyCPm5D'
api_url = 'https://andruxnet-random-famous-quotes.p.mashape.com'


def get_quotes():
    # this function gets quotes from an API

    headers = {'X-Mashape-Key': api_key, 'X-Mashape-Host': api_url}
    response = requests.get(api_url, headers=headers)
    json = response.json()[0]
    tweet = json['quote'] + ' - ' + json['author']
    return tweet


def tweet_quote():
    for i in range(1, 10):
        quote = get_quotes()
        time.sleep(30)
        try:
            api.update_status(quote)  # this method is accessed in tweepy
            print('Done')
        except tweepy.error.TweepError:
            pass


if __name__ == '__main__':
    tweet_quote()
