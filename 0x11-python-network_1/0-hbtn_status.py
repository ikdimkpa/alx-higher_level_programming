#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status" 

    with urllib.request.urlopen(url) as response:
        html = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(html))
    print(f"\t- content: {html}")
    print("\t- utf-8 content: {}".format(html.decode('utf8')))
