import requests
import re
import json
import random
from bs4 import BeautifulSoup
import sqlite3
import time
def writeCMD(cmd,content):
	f = open('cmdList.txt', 'a+', encoding = 'UTF-8')
	cmdContent=cmd+","+content+"\n"
	f.write(cmdContent)
	
#def deleteCMD(cmdName):

	#print (x)			
#deleteCMD("!Test2")







#conn = sqlite3.connect('cmdList.db')


#print ("Opened database successfully");
#c = conn.cursor()
#c.execute('''CREATE TABLE CMDLIST
#       (
#       CMDNAME           TEXT    NOT NULL,
#       CMDCONTENT           TEXT     NOT NULL);''')
#print ("Table created successfully");
#conn.commit()
#conn.close()







def addCMD(cmdName,cmdContent):
	check=cmdList()
	if cmdName not in check:
		conn = sqlite3.connect('/app/cmdList.db')
		c = conn.cursor()
		c.execute("INSERT INTO CMDLIST (CMDNAME,CMDCONTENT)  VALUES (?,?)",(cmdName,cmdContent));
		conn.commit()
		conn.close()
		alert="指令加入成功"
		return alert
	else:
		alert="指令已存在"
		return alert



def deleteCMD(cmdName):
	check=cmdList()
	if cmdName in check:
		conn = sqlite3.connect('/app/cmdList.db')
		c = conn.cursor()
		#print ("Opened database successfully")
		c.execute("DELETE from CMDLIST where CMDNAME=(?)",(cmdName,))
		conn.commit()
		alert="指令已刪除"
		return alert
		#print ("Total number of rows deleted :", conn.total_changes)
	else:
		alert="查無此指令"
		return alert

def updateCMD(cmdName,cmdContent):
	check=cmdList()
	if cmdName in check:
		conn = sqlite3.connect('/app/cmdList.db')
		c = conn.cursor()
		c.execute("UPDATE CMDLIST set CMDCONTENT=? where CMDNAME=?",(cmdContent,cmdName))
		conn.commit()
		alert="指令已修改"
		return alert
	else:
		return 

def cmdList():
	list=""
	conn = sqlite3.connect('/app/cmdList.db')
	#print ("Opened database successfully");
	c = conn.cursor()
	cursor = c.execute("SELECT CMDNAME, CMDCONTENT from CMDLIST")
	for row in cursor:
		list=list+"  "+str(row[0])
	
	#print ("CMDCONTENT = ", row[1], "\n")
	conn.close()
	return list
	
def showContent(cmdName):
	check=cmdList()
	if cmdName in check:
		conn = sqlite3.connect('/app/cmdList.db')
		c = conn.cursor()
		cursor = c.execute("SELECT CMDCONTENT, CMDCONTENT from CMDLIST WHERE CMDNAME=(?)",(cmdName,))	
		for row in cursor:
			return str(row[1])
		conn.close()
	else:
		return 
	
		
		
	
	
#addCMD("!Test4","測試新增指令")
if __name__ == "__main__":
	#addCMD("!Test6","第五次測試新增指令功能")
	#deleteCMD("!Test2")
	#print(showContent("!Tes"))
	#updateCMD("!Test4","1123")
	print()