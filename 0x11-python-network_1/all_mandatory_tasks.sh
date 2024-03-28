#!/bin/bash

# Array of file names
files=("0-hbtn_status.py" "1-hbtn_header.py" "2-post_email.py" "3-error_code.py" "4-hbtn_status.py" "5-hbtn_header.py" "6-post_email.py" "7-error_code.py" "8-json_api.py" "10-my_github.py")

# Array of file contents
contents=(
"#!/usr/bin/python3
\"\"\"
Script that fetches https://alx-intranet.hbtn.io/status
\"\"\"

import urllib.request

if __name__ == \"__main__\":
    url = \"https://alx-intranet.hbtn.io/status\"
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print(\"Body response:\")
        print(\"\t- type: {}\".format(type(content)))
        print(\"\t- content: {}\".format(content))
        print(\"\t- utf8 content: {}\".format(content.decode('utf-8')))
"
"#!/usr/bin/python3
\"\"\"
Script that takes in a URL sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response
\"\"\"

import urllib.request
import sys

if __name__ == \"__main__\":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
"
"#!/usr/bin/python3
\"\"\"
Script that takes in a URL and an email sends a POST request to the passed URL
with the email as a parameter and displays the body of the response
\"\"\"

import urllib.parse
import urllib.request
import sys

if __name__ == \"__main__\":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
"
"#!/usr/bin/python3
\"\"\"
Script that takes in a URL sends a request to the URL and displays the body
of the response If an error occurs it prints the HTTP status code
\"\"\"

import urllib.error
import urllib.request
import sys

if __name__ == \"__main__\":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(\"Error code: {}\".format(e.code))
"
"#!/usr/bin/python3
\"\"\"
Script that fetches https://alx-intranet.hbtn.io/status using requests
\"\"\"

import requests

if __name__ == \"__main__\":
    url = \"https://alx-intranet.hbtn.io/status\"
    response = requests.get(url)
    print(\"Body response:\")
    print(\"\t- type: {}\".format(type(response.text)))
    print(\"\t- content: {}\".format(response.text))
"
"#!/usr/bin/python3
\"\"\"
Script that takes in a URL sends a request to the URL and displays the value
of the variable X-Request-Id in the response header using requests
\"\"\"

import requests
import sys

if __name__ == \"__main__\":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
"
"#!/usr/bin/python3
\"\"\"
Script that takes in a URL and an email address sends a POST request to the
passed URL with the email as a parameter and finally displays the body of the
response
\"\"\"

import requests
import sys

if __name__ == \"__main__\":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)
"
"#!/usr/bin/python3
\"\"\"
Script that takes in a URL sends a request to the URL and displays the body
of the response If the HTTP status code is greater than or equal to 400
prints an error message
\"\"\"

import requests
import sys

if __name__ == \"__main__\":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print(\"Error code: {}\".format(response.status_code))
    else:
        print(response.text)
"
"#!/usr/bin/python3
\"\"\"
Script that takes in a URL and an email address sends a POST request to the
passed URL with the email as a parameter and finally displays the body of the
response
\"\"\"

import requests
import sys

if __name__ == \"__main__\":
    url = \"http://0.0.0.0:5000/search_user\"
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = \"\"
    data = {'q': letter}
    response = requests.post(url, data=data)
    try:
        json_r = response.json()
        if json_r:
            print(\"[{}] {}\".format(json_r.get('id'), json_r.get('name')))
        else:
            print(\"No result\")
    except ValueError:
        print(\"Not a valid JSON\")
"
"#!/usr/bin/python3
\"\"\"
Script that takes your GitHub credentials and uses the
GitHub API to display your id
\"\"\"

import requests
import sys

if __name__ == \"__main__\":
    username = sys.argv[1]
    password = sys.argv[2]
    url = \"https://api.github.com/user\"
    response = requests.get(url, auth=(username, password))
    print(response.json().get('id', None))
"
)

# Loop through the files and write the contents
for i in ${!files[@]}; do
    echo "${contents[$i]}" > "${files[$i]}"
    chmod u+x "${files[$i]}"
done
