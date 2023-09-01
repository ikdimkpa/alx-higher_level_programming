#!/usr/bin/python3
"""
 Python script that takes your GitHub credentials
 (username and password) and uses the GitHub API to display your id
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    authenticate = HTTPBasicAuth(argv[1], argv[2])
    req = requests.get(url, auth=authenticate)

    print(req.json().get("id"))
