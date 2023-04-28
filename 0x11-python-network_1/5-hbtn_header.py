#!/usr/bin/python3
"""
Script that takes a URL as an argument
sends a request and displays the value of the 'X-Request-Id' header
"""


import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)

    print(response.headers.get('X-Request-Id'))
