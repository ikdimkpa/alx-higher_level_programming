#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body
of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}

    value = urllib.parse.urlencode(email)
    data = value.encode("ascii")
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(url) as response:
        print(response.read().encode("utf-8"))
