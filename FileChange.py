#!/usr/bin/env python
#-*-coding:utf-8-*-

import os
import time

#deal file
def FileDeal(FileNeedToDo):
	f = open('/rawdata/xdr/gn/gn_dns/' + TimeMenu + '/' + FileName + '/' + FileNeedToDo,'rb')
	s = open('/rawdata/xdr/gn/gn_dns_bak/' + TimeMenu + '/' + FileName + '/' + FileNeedToDo,'w')
	f.seek(0,0)
	Happends = len(f.readlines())
	f.seek(0,0)
	Lines = f.readline()
	OneLine = Lines.strip() + '\n'
	Happends = len(f.readlines())
	counter = 0
	while (counter < Happends + 1):
		Middle = str(OneLine)
		ValueStr = Middle.split('|')
		MixList = ValueStr[0:15] + ['***************'] + ValueStr[17:]
		AnswerList = '|'.join(MixList)
		s.write(AnswerList)
		counter = counter + 1
	f.close()
	s.close()

SysTime = list(time.localtime())
TimeMenu = str(SysTime[0])+'0'+str(SysTime[1])+str(SysTime[2])
FileName = str(SysTime[3])


IsExists1 = os.path.exists('/rawdata/xdr/gn/gn_dns_bak/'+TimeMenu)
if IsExists1 is False:
    	os.makedirs('/rawdata/xdr/gn/gn_dns_bak/'+TimeMenu)

IsExists2 = os.path.exists('/rawdata/xdr/gn/gn_dns_bak/'+TimeMenu+'/'+FileName)
if IsExists2 is False:
	os.makedirs('/rawdata/xdr/gn/gn_dns_bak/'+TimeMenu+'/'+FileName)

        
fileList1 = os.listdir('/rawdata/xdr/gn/gn_dns/'+TimeMenu+'/'+FileName)
fileList2 = os.listdir('/rawdata/xdr/gn/gn_dns_bak/'+TimeMenu+'/'+FileName)

#file numbers in fileDir
num1 = 0
for file1 in fileList1:
		num1 = num1 + 1
	
num2 = 0
for file2 in fileList2:
		num2 = num2 + 1

		
#compare file numbers
if num1 == num2:
	pass
else:
	try:
		FileToDoList = [i for i in fileList1 if i not in fileList2]
		for FileNeedToDo in FileToDoList:
			FileDeal(FileNeedToDo)
			print FileNeedToDo
	except Exception,e:
		pass
