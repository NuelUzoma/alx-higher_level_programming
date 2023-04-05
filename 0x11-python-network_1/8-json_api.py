#!/usr/bin/python3
"""
Write a Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
You must use the package requests and sys"""


if __name__ == "__main__":
    from requests import post
    import sys

    URL = 'http://0.0.0.0:5000/search_user'
    DATA = {'q': sys.argv[1] if len(sys.argv) >= 2 else ""}
    reply = post(URL, DATA)

    con_type = reply.headers['content-type']

    if con_type == 'application/json':
        results = reply.json()
        __id = results.get('id')
        _name = results.get('name')
        if (results != {} and __id and _name):
            print("[{}] {}".format(__id, _name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
