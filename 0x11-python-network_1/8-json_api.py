#!/usr/bin/python3
"""

"""


import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ''

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    response = requests.post(url, data=data)

    try:
        json_data = response.json()
        if len(json_data) == 0:
            print("No result")
        else:
            print("[{}] {}".format(json_data["id"], json_data["name"]))
    except ValueError:
        print("Not a valid JSON")
