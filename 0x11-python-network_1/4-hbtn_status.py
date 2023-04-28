#!/usr/bin/python3
"""
Script that fetches the status of the URL usinf the requests package
and displays the response body
"""


import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(response.content)))
    print("\t- content: {}".format(response.content.decode()))
