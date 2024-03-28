#!/usr/bin/python3
"""
Script that takes in a URL and an email address sends a POST request to the
passed URL with the email as a parameter and finally displays the body of the
response
"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    data = {'q': letter}
    response = requests.post(url, data=data)
    try:
        json_r = response.json()
        if json_r:
            print("[{}] {}".format(json_r.get('id'), json_r.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
