#!/usr/bin/python3
"""
A script that fetches https://alx-intranet.hbtn.io/status
"""


import urllib.request
if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        html = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8", "replace")))
