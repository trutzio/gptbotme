import logging

from prometheus_client import start_http_server

from openai_service import OpenAIService
from tweets_stream import TweetsStream


def main():
    logging.basicConfig(level=logging.DEBUG)
    start_http_server(8000)
    tweets_stream = TweetsStream(openai_service=OpenAIService())
    tweets_stream.filter()


if __name__ == '__main__':
    main()
