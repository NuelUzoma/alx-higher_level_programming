#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import requests

    req = requests.get('https://alx-intranet.hbtn.io/status')
    tex = req.text
    print('Body response:\n\t- type: {}\n\t- content: {}'
          .format(type(tex), tex))
