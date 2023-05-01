#!/usr/bin/python3
"""
A script that takes 2 arguments in order to solve this challenge
"""


import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"\
          .format(argv[2], argv[1])
    res = requests.get(url)
    n = 0
    for i in res.json():
        if n < 10:
            print("{}: {}".format(i.get("sha"),
                  i.get("commit").get("author").get("name")))
        n += 1
