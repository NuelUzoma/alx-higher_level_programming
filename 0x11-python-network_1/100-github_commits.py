#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments in order to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys"""


if __name__ == "__main__":
    from requests import get
    import sys

    REP = sys.argv[1]
    OWNER = sys.argv[2]
    i = 0

    URL = "https://api.github.com/repos/{}/{}/commits".format(OWNER, REP)

    reply = get(URL)
    json = reply.json()

    for element in json:
        if i > 9:
            break
        sha = element.get('sha')
        author = element.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
        i += 1
