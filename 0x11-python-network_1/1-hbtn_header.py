#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
and displays the value of the
X-Request-Id variable found in the header of the response.
You must use the packages urllib and sys
You are not allow to import packages other than urllib and sys
The value of this variable is different for each request"""


if __name__ == "__main__":
    import urllib.request
    import sys

    args = sys.argv[1]
    with urllib.request.urlopen(args) as response:
        print(response.headers["X-Request-Id"])
