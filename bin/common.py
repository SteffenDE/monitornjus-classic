#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Copyright (c) 2015 Steffen Deusch

import datetime
import sqlite3

datum = datetime.datetime.now()
version = "0.6.1&beta;"

##########################################################################################

conn = sqlite3.connect('../admin/MonitorNjus.db')

def getinfo(Info, Seite, Nummer):
	cursor = conn.execute("SELECT "+Info+" FROM DISPLAYSETS WHERE SEITE=\'"+Seite+"\' AND NUMMER="+str(Nummer)+";");
	return cursor.fetchone()[0]

def writeinfo(Seite, Nummer, Info, value):
	if str(value).isdigit():
		conn.execute("UPDATE DISPLAYSETS SET "+Info+"="+str(value)+" WHERE SEITE=\'"+Seite+"\' AND NUMMER="+str(Nummer)+";");
	else:
		conn.execute("UPDATE DISPLAYSETS SET "+Info+"=\'"+value+"\' WHERE SEITE=\'"+Seite+"\' AND NUMMER="+str(Nummer)+";");
	conn.commit()

def getwidgetinfo(Name, Info):
	cursor = conn.execute("SELECT "+Info+" FROM WIDGETS WHERE NAME=\'"+Name+"\';");
	widgetinfo = cursor.fetchone()[0]
	return widgetinfo

def writewidgetinfo(Name, Info, value):
	if str(value).isdigit():
		conn.execute("UPDATE WIDGETS SET "+Info+" = "+str(value)+" WHERE NAME=\'"+Name+"\';");
	else:
		conn.execute("UPDATE WIDGETS SET "+Info+" = \'"+value+"\' WHERE NAME=\'"+Name+"\';");
	conn.commit()

def getgeteilt(Seite):
	cursor = conn.execute("SELECT AKTIV FROM DISPLAYSETS WHERE SEITE=\'"+Seite+"\';");
	val = str(cursor.fetchall())
	liste = " ".join(val)
	return liste

def minaktiv(Seite):
	cursor = conn.execute("SELECT NUMMER FROM DISPLAYSETS WHERE AKTIV=1 and SEITE=\'"+Seite+"\';");
	val = cursor.fetchall()
	minval = min(val)
	y = str(minval).replace('(','').replace(')','').replace(',','')
	return y

def allaktiv(Seite):
	cursor = conn.execute("SELECT NUMMER FROM DISPLAYSETS WHERE AKTIV=1 and SEITE=\'"+Seite+"\';");
	val = cursor.fetchall()
	return val

##########################################################################################

def getrows():
	cursor = conn.execute("SELECT NUMMER FROM DISPLAYSETS WHERE SEITE=\"Links\";");
	val = cursor.fetchall()
	maxval = max(val)
	return maxval[0]

def getallrows():
	cursor = conn.execute("SELECT NUMMER FROM DISPLAYSETS WHERE SEITE=\"Links\";");
	val = str(cursor.fetchall())
	liste = " ".join(val)
	return liste

def write(Seite, Nummer, URL, Aktiv, Refreshaktiv, Refresh):
	conn.execute("DELETE FROM DISPLAYSETS where SEITE=\'"+Seite+"\' AND NUMMER="+str(Nummer)+"");
	conn.execute("INSERT INTO DISPLAYSETS (SEITE,NUMMER,URL,AKTIV,REFRESHAKTIV,REFRESH) values (\'"+Seite+"\',"+str(Nummer)+",\'"+URL+"\',"+str(Aktiv)+","+str(Refreshaktiv)+","+str(Refresh)+")");
	conn.commit()

def createrow(Nummer):
	write("Links", Nummer, "placeholder.html", 1, 0, 60)
	write("Rechts", Nummer, "placeholder.html", 1, 0, 60)

def delrow(Nummer):
	conn.execute("DELETE FROM DISPLAYSETS where NUMMER="+str(Nummer)+"");
	conn.commit()

def checkfiletype(datei):
	if ".png" in datei or ".jpg" in datei or ".gif" in datei or ".bmp" in datei:
		return "image"
	elif ".mp4" in datei or ".wmv" in datei:
		return "video"
	elif ".pdf" in datei:
		return "pdf"
	elif "youtube" and "watch?v=" in datei:
		return "youtube"
	else:
		return "unknown"