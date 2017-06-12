#!/usr/bin/env python3

from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlparse
from urllib.parse import urlencode
from lxml import etree
# from bs4 import BeautifulSoup
import time
import pandas as pd

# """
# This module is meant to grab all the possible user agents
# """
#
# baseurl= 'http://www.useragentstring.com/pages/useragentstring.php'
# base= 'http://www.useragentstring.com/'
headers= {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.3'}
#
# request= Request(baseurlm , headers=headers)
#
# response= urlopen(request).read()
#
# tree=etree.HTML(response)
#
# clinks= tree.xpath("//td[@style='vertical-align:top;']/a[@class='unterMenuName']")
#
# bmlinks=tree.xpath("//td[@style='vertical-align:top;width:30%;'][1]/a[@class='unterMenuName']")
#
#
# clinks=[link.get('href') for link in clinks]
#
# bmlinks=[link.get('href') for link in bmlinks]
#
# print(clinks)
# print(bmlinks)
#
#
# def make_links(base,links):
#     final=[]
#     for link in links:
#         if (len(link)==0) or (len(link)==1):
#             continue
#         else:
#             final.append(base+link[1:])
#     return final
#
#
# crawlers=make_links(base,clinks)
# browsers=make_links(base,bmlinks)
# with open('/media/isaacoduro/senator/Documents/User-AgengtCrawlers.txt','w+') as f:
#     for lk in crawlers:
#         f.write(lk+',')
#
# with open('/media/isaacoduro/senator/Documents/User-AgengtBrowsers.txt','w+') as g:
#     for link in browsers:
#         g.write(link+',')
#
# print(crawlers)
# print(browsers)

browsers,crawlerslink=[],[]

with open('/media/isaacoduro/senator/Documents/User-AgengtCrawlers.txt','r') as c\
, open('/media/isaacoduro/senator/Documents/User-AgengtBrowsers.txt','r') as b:
    cr=c.read().split(','); cr.remove('')
    br=b.read().split(','); br.remove('')
    for link in cr:
        req=Request(link.strip(), headers=headers)

        the_page=urlopen(req).read()

        tree=etree.HTML(the_page)

        UA=[link.text for link in tree.xpath("//li/a[@href]")]
        crawlerslink += UA
        time.sleep(2)

    for ln in br:
        req=Request(ln.strip())

        the_page=urlopen(req).read()

        tree=etree.HTML(the_page)

        UA=[link.text for link in tree.xpath("//li/a[@href]")]
        browsers += UA
        time.sleep(2)
cl=len(crawlerslink)
bl=len(browsers)
if cl> bl:
    pd.DataFrame({'crawlers_UA':crawlerslink,'browsers_UA':browsers+\
    ['' for i in range(cl-bl)]}).\
    to_csv('/media/isaacoduro/senator/Documents/User-Agent.csv')
else:
    pd.DataFrame({'crawlers_UA':crawlerslink +\
    ['' for i in range(bl-cl)],'browsers_UA':browsers}).\
    to_csv('/media/isaacoduro/senator/Documents/User-Agent.csv')
