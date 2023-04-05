#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
You must use Basic Authentication with a personal access token as password
to access to your information (only read:user permission is needed)
The first argument will be your username
The second argument will be your password
(in your case, a personal access token as password)
You must use the package requests and sys"""


if __name__ == "__main__":
    import sys
    from requests import get

    USER = sys.argv[1]
    PWD = sys.argv[2]

    URL = "https://api.github.com/user"
    reply = get(URL, auth=(USER, PWD))
    json = reply.json()

    print(json.get('id'))
