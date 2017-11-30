#coding=utf-8
 
import urllib
import os
from bs4 import BeautifulSoup
import time
import socket

timeout = 20
socket.setdefaulttimeout(timeout)  
i = 100684881
resulty = 1
while (i < 100693727):
	pos = str(i)
	res = urllib.urlopen("http://www.timepill.net/people/" + pos)
	soup = BeautifulSoup(res,"html.parser")
	result = str(soup.title.encode('gb18030') + pos)
	if '404' in result:
		pass
	elif (result == resulty):
		pass
	else:
		resulty = result
		f = open('F:\j2kly.csv','a')
		f.write(resulty +'\n')
		f.close
	print result
	i = i + 1
	time.sleep(0.5)
print result
