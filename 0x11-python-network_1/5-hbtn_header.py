#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header
You must use the packages requests and sys
You are not allow to import other packages than requests and sys"""


if __name__ == "__main__":
    from requests import get
    import sys

    args = sys.argv[1]
    req = get(args)
    print(req.headers.get('X-Request.Id'))
