#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL and
displays the body of the response.
If the HTTP status code is greater than or equal to 400, print:
Error code: followed by the value of the HTTP status code
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys"""


if __name__ == "__main__":
    from requests import get
    import sys

    URL = sys.argv[1]

    reply = get(URL)
    ERROR_TEXT = 'Error code: {}'
    STAT = reply.status_code
    print(ERROR_TEXT.format(STAT) if (STAT >= 400) else reply.text)
