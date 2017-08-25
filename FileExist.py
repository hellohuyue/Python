#!/usr/bin/python
#-*-coding:utf-8-*-

import os
import time

SysTime = list(time.localtime())
if len(str(SysTime[1])) is 1:
        FileMonth = '0' + str(SysTime[1])
else:
        FileMonth = str(SysTime[1])

if len(str(SysTime[2]))  is 1:
        FileDay = '0' + str(SysTime[2])
else:
        FileDay = str(SysTime[2])	

if len(str(SysTime[3])) is 1:
        FileHour = '0' + str(SysTime[3])
else:
        FileHour = str(SysTime[3])

if len(str(SysTime[4])) is 1:
        FileMin = '0' + str(SysTime[4])
else:
        FileMin = str(SysTime[4])



if (FileMin == '00'):
        FileMin = 30
        FileHour = int(FileHour) - 1
elif (FileMin == '05')::
        FileMin = 35
        FileHour = int(FileHour) - 1
elif (FileMin == '10'):
        FileMin = 40
        FileHour = int(FileHour) - 1
elif (FileMin == '15'):
        FileMin = 45
        FileHour = int(FileHour) - 1
elif (FileMin == '20'):
        FileMin = 50
        FileHour = int(FileHour) - 1
elif (FileMin == '25'):
        FileMin = 55
        FileHour = int(FileHour) - 1		
else:
        FileMin = int(FileMin) - 30

		
if len(str(FileMin)) is 1:
        FileMin = '0' + str(FileMin)
else:
        pass


TimeMenu = str(SysTime[0]) + str(FileMonth) + str(FileDay) + str(FileHour) + str(FileMin)



FileList = os.listdir('/home/ipnet/tomcat_rec/savefile/DNMS_APP/DATA.PM.CMNET_PMDATA_DNS_5_2016082240.DNMS_APP')
FileLen = len(FileList) 
counter = 0
while(counter < FileLen):
		FileList[counter]= str(FileList[counter]).split('_')[4][0:12]
		counter = counter + 1

TimeMenu = list(TimeMenu)
TimeMenu = ''.join(TimeMenu)
if TimeMenu not in FileList:
	print 'ERRO:' + TimeMenu + 'not Exist!'
else:
	pass

