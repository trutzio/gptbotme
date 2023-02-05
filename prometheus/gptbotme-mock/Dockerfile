FROM alpine:latest
RUN apk add --update --no-cache python3 bash
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install prometheus-client
RUN mkdir /gptbotme
COPY src/*.py /gptbotme/
ENTRYPOINT [ "python3", "/gptbotme/gptbotme.py" ]