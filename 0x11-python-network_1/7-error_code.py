#!/usr/bin/python3
""""""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".formar(response.status_code))
    else:
        print(response.text)
