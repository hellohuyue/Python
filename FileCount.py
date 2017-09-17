#!/usr/bin/python

import os
import os.path
import sys

def file_extension(path): 
  return os.path.splitext(path)[1];

if len(sys.argv) != 3:
    print 'usage : python.exe <dirPath> <fileClass>'
    exit()
else:
	print sys.argv
	
fileDir = sys.argv[1]
fileClass = sys.argv[2]
print fileDir
print fileClass
fileNum = 0
fileList=os.listdir(fileDir)
print fileList
f = open('huyue.txt','w')
f.write(fileList)
f.close
for file in fileList:
  if file_extension(fileDir+"\\"+file) == fileClass:
		print fileDir+"\\"+file
		fileNum=fileNum+1

print "in " + fileDir +" already have " + str(fileNum) + " files"
