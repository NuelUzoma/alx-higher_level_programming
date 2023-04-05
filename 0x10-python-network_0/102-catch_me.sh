#!/bin/bash
# A Bash Script that causes the server to respond a specific message
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:HolbertonSchool"
