#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status
   it uses urllib package
"""
from urllib.request import Request, urlopen

if __name__ == '__main__':


  req = Request('https://alx-intranet.hbtn.io/status')
  with urlopen(req) as response:
    page = response.read()

    print('Body response: ')
    print('\t- type: {}'.format(type(page)))
    print('\t- content: {}'.format(page))
    print('\t- utf8 content: {}'.format(page.decode('utf-8')))
