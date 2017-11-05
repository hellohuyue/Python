#!/usr/bin/python
#-*-coding:utf-8-*-

import time
import os

# get current time
SysTime = list(time.localtime())
imazero = '0'
if len(str(SysTime[1])) == 1:
        SysMouth = imazero + str(SysTime[1])
else:
        SysMouth = str(SysTime[1])

if len(str(SysTime[2])) == 1:
                SysDay = imazero + str(SysTime[2])
else:
                SysDay = str(SysTime[2])

CurrentTime = str(SysTime[0]) + SysMouth + SysDay



# write initial filenum 
SysHour = str(SysTime[3])
if SysHour == '0':
        msgtxtnum = '0'
        FileWrite = open('/home/ipms/mybin/OrigTypeFileNum/OrigType1.txt','w')
        FileWrite.write(msgtxtnum)
        FileWrite.close
        os.system('echo > /home/ipms/mybin/OrigTypeFileNum/OrigTypename.txt')
else:
        # get current .orig filename
        msgmenu = '/home/ipms/report_data/4g/*.orig|'
        msgvalue = 'ls %s grep %s'%(msgmenu,CurrentTime)
        msgvaluetxt = os.popen(msgvalue)
        msgvaluetxt1 = msgvaluetxt.read()
        msgtxtvalue = msgvaluetxt1.split('\n/home/ipms/report_data/4g/')
        # get current .orig filename
        msgcountcmd = '|wc -l'
        msgcount = 'ls %s grep %s %s'%(msgmenu,CurrentTime,msgcountcmd) 
        msgcounttxt = os.popen(msgcount)
        msgcounttxt1 = msgcounttxt.read()
        msgtxtnum = str(msgcounttxt1.split('\n')[0])

# get last filenum
FileRead = open('/home/ipms/mybin/OrigTypeFileNum/OrigType1.txt','r')
FileRead.seek(0,0)
LastFilenum = FileRead.readline().split('\n')[0]
FileRead.close

# get currentfilename
FileRead1 = open('/home/ipms/mybin/OrigTypeFileNum/OrigTypename.txt','r')
FileRead1.seek(0,0)
middlefilename = FileRead1.readline()
FileRead1.close

LastFilename = []
for i in msgtxtvalue:
        if i not in middlefilename:
                LastFilename.append(i)

LastFilename = str(LastFilename)[2:-4]
print LastFilename

if LastFilenum < msgtxtnum:
    msg = '部省接口实时数据平滑告警,共' + msgtxtnum + '个文件,小时平滑文件:' + LastFilename
elif msgtxtnum == '0':
    pass
else:
    pass


# write current filenum into txt 
os.system('echo > /home/ipms/mybin/OrigTypeFileNum/OrigType1.txt')
FileWrite1 = open('/home/ipms/mybin/OrigTypeFileNum/OrigType1.txt','w')
FileWrite1.write(msgtxtnum)
FileWrite1.close

os.system('echo > /home/ipms/mybin/OrigTypeFileNum/OrigTypename.txt')
FileWrite2 = open('/home/ipms/mybin/OrigTypeFileNum/OrigTypename.txt','w')
FileWrite2.write(str(msgtxtvalue))
FileWrite2.close


#send msg
ShellThing = '/home/ipms/mybin/monitordisk/senddisksms.pl'
phone = '18721274720,18301804086,18818228528,13918528245,13816700194'
cmd = '/%s %s %s'%(ShellThing,msg,phone)
os.system(cmd)
