#!/usr/bin/python3
"""script that takes in a URL, 
    sends a request to the URL and 
    displays the value of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
