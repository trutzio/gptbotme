import logging
import time

from prometheus_client import Summary, start_http_server

REQUEST_TIME = Summary('gptbotme_request_seconds',
                       'Time spent processing request')


@REQUEST_TIME.time()
def process_request(t):
    logging.debug('sleeping %i seconds...', t)
    time.sleep(t)


def main():
    logging.basicConfig(level=logging.DEBUG)
    start_http_server(8000)
    while True:
        process_request(3)


if __name__ == '__main__':
    main()
