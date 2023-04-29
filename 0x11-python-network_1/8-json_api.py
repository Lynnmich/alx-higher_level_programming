#!/usr/bin/python3
"""
A script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
        payload = {'q': q}
        response = requests.post('http://0.0.0.0:5000/search_user',
                                 data=payload)

        try:
            data_json = response.join()
            if data_json:
                print("[{}] {}".format(data_json.get('id'),
                                       data_json.get('name')))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
