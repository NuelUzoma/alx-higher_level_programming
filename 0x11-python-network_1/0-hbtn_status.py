#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status
You must use the package urllib
No other package is allowed
You must use a with statement"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(
            'https://alx-intranet.hbtn.io/status') as response:
        page = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(page.decode("utf-8")))
