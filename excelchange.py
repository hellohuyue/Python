#!/usr/bin/python
# coding=gbk

	
import  openpyxl
wb = openpyxl.load_workbook('F:1.xlsx')
menuName = wb.get_sheet_names()[0]
sheet = wb.get_sheet_by_name(menuName)
n = 2
while n <= len(wb.get_sheet_names()):
	sheet_Cn = sheet['C' + str(n)].value.split('"')[3]
	sheet_zhongwen = sheet['F'+str(n)].value
	sheet_yinwen = sheet['G'+str(n)].value
	sheet2 = wb.get_sheet_by_name(sheet_Cn)
	sheet2['A2'].value = sheet_zhongwen
	sheet2['B2'].value = sheet_yinwen
	n = n + 1		

wb.save('f:1.xlsx')
	
