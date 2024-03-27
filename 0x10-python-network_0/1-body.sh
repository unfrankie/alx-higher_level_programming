#!/bin/bash
# Sends a GET request to a URL and displays the body of the response
curl -s -X GET "$1" -D - -o /dev/null
