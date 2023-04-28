#!/usr/bin/python3
"""
This script takes a URL as an argument,
sends a request to the URL using urllib,
and displays the value of the X-Request-Id variable
found in the header of the response.
"""

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        header = response.getheader('X-Request-Id')

    print(header)
