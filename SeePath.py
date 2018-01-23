#!/usr/bin/python
#-*-coding:utf-8-*-


import os
PID = []

for i in PID:
        f = os.popen('pwdx' +' ' + i)
        p = os.popen('ps' + ' ' + '-ef|grep' + ' ' + i)
        data1 = p.readlines()
        middledata = str(data1).split('-')
        for y in middledata:
                if 'Diname' in y:
                        aimdata = y
        data2 = f.readline()
        print data2
        print aimdata
