import tweepy
import configparser
import json

if __name__ == '__main__':
    # resolve config
    config = configparser.ConfigParser()
    config.read('config.ini')

    api_key = config['twitter']['api_key']
    api_key_secret = config['twitter']['api_key_secret']

    access_token = config['twitter']['access_token']
    access_token_secret = config['twitter']['access_token_secret']

    bearer_token = config['twitter']['bearer_token']


    # authentication to the api
    client = tweepy.Client(bearer_token = bearer_token)

    # retrieve tweets: limit is 450 requests per 15 minute window with a maximum of 100 tweets per request
    keyword = 'Innsbruck'
    hashtag = '#Innsbruck'
    query = keyword + ' OR ' + hashtag

    response = client.search_recent_tweets(query = query, max_results = 100, tweet_fields = ['public_metrics', 'created_at'])
    tweets = response.data

    # write to json file
    with open('tweets.json', 'a', encoding='utf-8') as output_file:
        for tweet in tweets:
            json.dump(tweet.data, output_file, indent=4)
            print(",", file=output_file)