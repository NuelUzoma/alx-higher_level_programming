#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email, sends
a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
The email must be sent in the email variable
You must use the packages urllib and sys
You are not allowed to import packages other than urllib and sys"""

if __name__ == "__main__":
    import urllib.request
    import sys
    import urllib.parse

    args = sys.argv
    URL = args[1]
    EMAIL = args[2]
    EMAIL_DATA = urllib.parse.urlencode({"email": EMAIL})
    EMAIL_DATA = EMAIL_DATA.encode('ascii')

    with urllib.request.urlopen(URL, EMAIL_DATA) as response:
        print(response.read().decode('utf-8'))
