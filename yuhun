#!/usr/bin/python

 
import time
import win32api,win32gui,win32con
from ctypes import *

#left click
def clickLeftCur():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP, 0, 0)
	
#move
def moveCurPos(x,y):
    windll.user32.SetCursorPos(x, y)

#pos	
def getCurPos():
    return win32gui.GetCursorPos()

#win handle
def get_win_handle(pos):   
	return win32gui.WindowFromPoint(pos)
	
#get current win_handle
getCurPos()
pos = getCurPos()
fore = get_win_handle(pos)
print pos,fore

win32gui.SetForegroundWindow(657494)
time.sleep(1)

while True:
#tiaozhan
	moveCurPos(604,2)
	clickLeftCur()
	time.sleep(5)

#zhunbei
	moveCurPos(604,2)
	clickLeftCur()
	time.sleep(5)

#jiangli
	moveCurPos(604,2)
	clickLeftCur()
	time.sleep(5)
