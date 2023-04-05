#!/bin/bash
# A script that sends a request to a URL and displays only the status code
curl -so /dev/null -w "%{http_code}" "$1"
