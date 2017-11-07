#!/usr/bin/python
# coding=utf-8

import socket
import time
import sys

if len(sys.argv) != 2:
    print 'usage : python.exe <port>'
    exit()
else:
        print sys.argv


port = int(sys.argv[1])
file = open('ipfile','r')
host_list = file.readlines()
for line in host_list:
    ip = line.split(",")[0]
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2)
    try:
       s.bind(('',port))
       print "###connect %s:%s is success###"%(ip,port)
    except socket.error,e: 
       print "###connect %s:%s %s###"%(ip,port,e)
    finally:
       s.close()
file.close()
