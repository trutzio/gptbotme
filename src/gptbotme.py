import logging

from openai_service import OpenAIService
from tweets_stream import TweetsStream


def main():
    logging.basicConfig(level=logging.INFO)
    tweets_stream = TweetsStream(openai_service=OpenAIService())
    tweets_stream.filter()


if __name__ == '__main__':
    main()
