#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests


url = "https://alx-intranet.hbtn.io/status"
req = requests.get(url)

print("Body response:")
print("\t- type: {}".format(type(req.text)))
print("\t- connect: {}".format(req.text))
