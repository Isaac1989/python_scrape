#!/usr/bin/env python3

import requests
from lxml import etree
import sys

# insanity check
if len(sys.argv) != 4:
    sys.stderr.write('Usage: login.py <url> <username> <pwd> \n')
    sys.exit(2)

url=sys.argv[1]

#login info
payload={
    'login':sys.argv[2],
    'password': sys.argv[3]
}

with requests.Session() as c:

    c.post(url,data=payload)

    req=requests.get('https://github.com/Isaac1989/Project_github').text

    tree=etree.HTML(req)

    print([x.text for x in tree.xpath("//a")])
    print('Isaac1989' in req)
