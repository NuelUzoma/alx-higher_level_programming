#!/bin/bash
# A script that sends a JSON POST request for the first argument
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"