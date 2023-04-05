#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status
You must use the package urllib
No other package is allowed
You must use a with statement"""
if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen(
            'https://alx-intranet.hbtn.io/status') as response:
        page = response.read()
