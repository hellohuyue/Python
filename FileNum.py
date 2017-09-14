#!/usr/bin/python
#-*-coding:utf-8-*-

import os
import time

#get current time
SysTime = list(time.localtime())
if len(str(SysTime[1])) == 1:
        SysMouth = '0' + str(SysTime[1])
else:
        SysMouth = str(SysTime[1])


CurrentTime = str(SysTime[0]) + SysMouth + str(SysTime[2])

#get filenum
SysHour = str(SysTime[3]) + str(SysTime[4])
if SysHour == '0000':
        msgtxtnum = '-1'
        FileWrite = open('/home/ipnet/mybin/FileExistCheck/FileNum.txt','w')
        FileWrite.write(msgtxtnum)
        FileWrite.close
else:
        msgmenu = '/home/ipnet/tomcat_rec/savefile/DNMS_APP/DATA.PM.CMNET_PMDATA_DNS_5_2016082240.DNMS_APP|'
        msgcmd = 'ls %s grep %s'%(msgmenu,CurrentTime)
        msgtxt = os.popen(msgcmd)
        msgtxt1 = msgtxt.read()
        msgtxtnum = str(len(msgtxt1.split('\n')) - 1)

#get last filenum
FileWrite = open('/home/ipnet/mybin/FileExistCheck/FileNum.txt','r')
FileWrite.seek(0,0)
LastFilenum = FileWrite.readline().strip()
FileWrite.close

#is last filename = currentfilename
if LastFilenum < msgtxtnum:
        pass
else:
        print 'ERRO:FileNumHasNotIncreasedOneHour!!'


#write filenum
os.system('echo > /home/ipnet/mybin/FileExistCheck/FileNum.txt')
FileWrite = open('/home/ipnet/mybin/FileExistCheck/FileNum.txt','w')
FileWrite.write(msgtxtnum)
FileWrite.close
