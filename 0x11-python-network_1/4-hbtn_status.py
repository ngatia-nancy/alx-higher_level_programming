#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status.
   Uses the request package
"""

import requests

if __name__ == '__main__':
    with requests.get('https://alx-intranet.hbtn.io/status') as r:
        response = r.text
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
