#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the body of the response
(decoded in utf-8).
You have to manage urllib.error.HTTPError exceptions and print:
Error code: followed by the HTTP status code
You must use the packages urllib and sys
You are not allowed to import other packages than urllib and sys"""

if __name__ == "__main__":
    from urllib import request, error
    import sys

    args = sys.argv
    URL = args[1]
    try:
        with request.urlopen(URL) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as errr:
        print("Error code: {}".format(errr.status))
