import os

import tweepy

from openai_service import OpenAIService

__bot_name__ = '@gptbotme'
__max_tweet_len__ = 280


class TweetsStream(tweepy.StreamingClient):

    openai_service: OpenAIService
    twitter_client: tweepy.Client

    def __init__(self, openai_service: OpenAIService) -> None:
        self.openai_service = openai_service
        bearer_token = os.getenv("BEARER_TOKEN")
        consumer_key = os.getenv("CONSUMER_KEY")
        consumer_secret = os.getenv("CONSUMER_SECRET")
        access_token = os.getenv("ACCESS_TOKEN")
        access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
        self.twitter_client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key,
                                            consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)
        super().__init__(bearer_token=bearer_token)

    def on_tweet(self, tweet):
        if __bot_name__ in tweet.text:
            prompt = tweet.text.replace(__bot_name__, '')
            answer = self.openai_service.answer(prompt=prompt)
            self.reply(tweet, answer)

    def reply(self, tweet, answer) -> None:
        last_tweet_id = tweet.id
        for tweet_text in self.split(answer):
            answer_tweet = self.twitter_client.create_tweet(
                in_reply_to_tweet_id=last_tweet_id, text=tweet_text)
            last_tweet_id = answer_tweet.data['id']

    def split(self, answer: str) -> list:
        tweets = []
        tweet = ''
        for word in answer.split():
            word_spaced = word + ' '
            if len(tweet + word_spaced) <= __max_tweet_len__:
                tweet += word_spaced
            else:
                tweets.append(tweet)
                tweet = word_spaced
        tweets.append(tweet.rstrip())
        return tweets
