#!/usr/bin/env python3

import requests
from lxml import html, etree
import pandas as pd
from bs4 import BeautifulSoup
import re

"""
olympics Us medalist for Rio2016
"""

url= "https://www.rio2016.com/en/swimming"

#Get webpage
contents=requests.get(url).content

####################################
#    Using lxml to parse
###################################
#Creat custome parser
parser= etree.HTMLParser(encoding='utf-8')

#create tree
tree = etree.fromstring(contents,parser)

#Get information
top_medalists= tree.xpath("//span[@class='top-medalist-table__medalist-name']/text()")

golds=tree.xpath("//span[@class='top-medalist-table__number-medals']")

golds=[int(x.text) for x in golds]

j=3
medals=[]
for i in range(6):
	medals.append(golds[:3])
	golds=golds[3:]

df=pd.DataFrame(dict(zip(top_medalists,medals)))
df=df.T.rename(columns={0:'Gold',1:'Silver',2:'Bronze'})
df.to_csv('/media/isaacoduro/senator/Downloads/DATA/olympic_swim_top_medalist.csv')


##################################################
#    Using Beautifulsoup to parse content
##################################################
soup=BeautifulSoup(contents,'lxml')

name_el=soup.find_all('span',class_=re.compile(r'medalist-name'))

names=[n.string for n in name_el]

print(names)

num_el=soup.find_all('span',class_=re.compile(r'number'))

print([int(str(num.string)) for num in num_el])
