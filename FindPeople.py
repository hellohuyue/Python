#coding=utf-8
 
import urllib
import os
from bs4 import BeautifulSoup
  
f = open('F:\j2kly.csv','a')
i = 1500
resulty = 1
pos = str(i)
while (i < 2500):
	res = urllib.urlopen("http://www.timepill.net/people/" + pos)
	soup = BeautifulSoup(res,"html.parser")
	result = str(soup.title.encode('gb18030') + pos)
	if '404' in result:
		pass
	elif (result == resulty):
		pass
	else:
		resulty = result
		f.write(resulty +'\n')
	i = i + 1
	print i

f.close
	
	
	
