#!/usr/bin/env python

import httplib
import urllib
import urllib2
import socket

# #using urllibs
#baseurl='http://chrisalbon.com/python/monitor_a_website.html'

#response=urllib2.urlopen(baseurl).read()

# print response

##using httplib to create a connection
host='chrisalbon.com'
#
# # create a connection
# connection=httplib.HTTPConnection(host)
#
# #make a request
# request=connection.request('GET','/python/monitor_a_website.html')
# #get response
# response=connection.getresponse().read()
# print response

print socket.gethostbyname(host)

##############################################
import sys
import socket

if len(sys.argv) !=2:
    print >>sys.stderr, 'usage: network.py <hostname_or_ip>'
    sys.exit(1)

host_name=sys.argv[1]

try:
    infolist= socket.getaddrinfo(host_name,'www',0,socket.SOCK_STREAM,0,\
    socket.AI_ADDRCONFIG|socket.AI_V4MAPPED | socket.AI_CANONNAME)
except socket.gaierror, e:
    print 'Name service failure', e.args[1]
    sys.exit(1)

info= infolist[0]
socket_arg=info[:3]
address=info[[-1]
s=socket.socket(*socket_arg)
try:
    s.connect(address)
except socket.error, e:
    print 'Network failure', e.args[1]
else:
    print "success: host", info[3], "is listening on port 80"



#Checking validity of links without downloading content
class HeadRequest(urllib2.Request):
    def get_method(self):
        return 'HEAD'
