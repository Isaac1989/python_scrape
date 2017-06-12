#!/usr/bin/env python3

from urllib.request import Request
from urllib.request import urlopen
from urllib.parse import urlparse
from lxml import etree
from bs4 import BeautifulSoup
import requests
from urllib.error import URLError




class Downloader(object):
    #Constructor
    def __init__(self,url,data=None,headers=\
    {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
         (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.3'}):

         #insanity checks
        assert len(url)>0, 'Your url is empty'
        assert url[:4]=='http' or url[:5]=='https',"Url must begin with 'http'\
        or 'https'. Example:: 'http(s)://www.example.com'"

        #Creating instance variables
        if isinstance(url,str) or isinstance(headers,dict):
            self.page=''
            self.url=url
            self.headers=headers
            self.data=data
            self.pretty_page=''
        else:
            print('headers must be a dictionary object')
            return

    def download(self):

        if self.url[:4]=='http' and self.data == None:
            try:
                req=Request(self.url,headers=self.headers)
                response  =  urlopen(req)

                self.page = self.page + response.read()

                print('status code: '+str(response.getcode()))

            except URLError as e:
                if hasattr(e, 'reason'):
                    print("Couldn't reach the server")
                    print("Reason: " + str(e.reason))
                if hasattr(e, 'code'):
                    print("Server couldn't honor the request")
                    print('http error code: ' + str(e.code))
        else:
            try:
                if self.data==None:
                    req=requests.get(self.url,headers=self.headers)

                    self.page=self.page + req.text

                    print('status code: '+ str(req.status_code))

                else:
                    req=request.get(self.url, params=self.data,headers=self.headers)

                    self.page= self.page + req.text

                    print('status code: ' + str(req.status_code))

            except requests.HTTPError as e:
                print('Server sent: '+ e)
            except requests.ConnectionError as e:
                    print('Connection problem: ' + e)
            except requests.Timeout as e:
                print('Connection timed out: '+ e)
            except requests.TooManyRedirects as e:
                print('Too many redirects: ' + e)

    def get_tree(self):
        print(self.page)
        return etree.HTML(self.page)

    def get_element(self,xpath="*"):
        return get_tree().xpath(xpath)








if __name__== '__main__':
    d = Downloader('http://www.pythonforbeginners.com/requests/using-requests-in-python')
    print(d.get_tree())
