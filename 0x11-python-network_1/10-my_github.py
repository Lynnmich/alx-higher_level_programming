#!/usr/bin/python3
"""
A script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""


import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    try:
        res = response.json()
        user_id = res.get("id")
        if user_id is not None:
            print(user_id)
    except ValueError:
        print("None")
