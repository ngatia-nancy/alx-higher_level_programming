#!/usr/bin/python3
"""Script that takes in a URL and an email,
   sends a POST request to the passed URL with the email as a parameter,
   displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.parse
import urllib.request

if __name__ == '__main__':
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('utf-8')

    post_request = urllib.request.Request(url, data)
    with urllib.request.urlopen(post_request) as response:
        page = response.read()
        print(page.decode('utf-8'))
