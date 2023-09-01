#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 1:
        arg = {'q': ""}
    else:
        arg = {'q': argv[1]}

    response = requests.post("http://0.0.0.0:5000/search_user", data=arg)
    try:
        res = response.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
