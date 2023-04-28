#!/usr/bin/python3
"""Sends a POST request with an email as parameter"""


import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        my_page = response.read()
        print(my_page.decode('utf-8'))i
