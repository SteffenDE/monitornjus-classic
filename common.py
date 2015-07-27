#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 22.07.2015 (Version 0.8.4)

import os
import datetime
import sqlite3

datum = datetime.datetime.now()
version = "0.9&beta;"
workingdir = os.path.dirname(os.path.realpath(__file__))

############################## Settings ##############################

debugv = 2				# Verbosity: 0,1,2 (0 = off, 1 = basic, 2 = mit Anmerkungen, 3 = Traceback, 707 = Easter Egg)

##########################################################################################

def authenticated():
	pass

conn = sqlite3.connect(workingdir+'/admin/MonitorNjus.db')

######################### basics #########################

def getinfo(Info, Seite, Nummer):
	cursor = conn.execute("SELECT "+Info+" FROM DISPLAYSETS WHERE SEITE=? AND NUMMER=?", [unicode(Seite), unicode(Nummer)]);
	return cursor.fetchone()[0]

def writeinfo(Seite, Nummer, Info, value):
	conn.execute("UPDATE DISPLAYSETS SET "+Info+"= ? WHERE SEITE=? AND NUMMER=?", [unicode(value), unicode(Seite), unicode(Nummer)]);
	conn.commit()

def getwidgetinfo(NAME, ID, Info):
	cursor = conn.execute("SELECT "+Info+" FROM WIDGETS WHERE NAME=? and ID=?", [unicode(NAME), unicode(ID)]);
	widgetinfo = cursor.fetchone()[0]
	return widgetinfo

def writewidgetinfo(Name, ID, Info, value):
	conn.execute("UPDATE WIDGETS SET "+Info+" = ? WHERE NAME=? and ID=?", [unicode(value), unicode(Name), unicode(ID)]);
	conn.commit()

def getgeteilt(Seite):
	cursor = conn.execute("SELECT AKTIV FROM DISPLAYSETS WHERE SEITE=\'"+Seite+"\';");
	val = unicode(cursor.fetchall())
	liste = " ".join(val)
	return liste

def minaktiv(Seite):
	cursor = conn.execute("SELECT NUMMER FROM DISPLAYSETS WHERE AKTIV=1 and SEITE=?", [unicode(Seite)]);
	val = cursor.fetchall()
	minval = min(val)
	y = unicode(minval).replace('(','').replace(')','').replace(',','')
	return y

def allaktiv(Seite):
	cursor = conn.execute("SELECT NUMMER FROM DISPLAYSETS WHERE AKTIV=1 and SEITE=?", [unicode(Seite)]);
	val = cursor.fetchall()
	return val

######################### rows #########################

def getrows():
	cursor = conn.execute("SELECT NUMMER FROM DISPLAYSETS WHERE SEITE=\"Links\";");
	val = cursor.fetchall()
	maxval = max(val)
	return maxval[0]

def getallrows():
	cursor = conn.execute("SELECT NUMMER FROM DISPLAYSETS WHERE SEITE=\"Links\";");
	val = unicode(cursor.fetchall())
	liste = " ".join(val)
	return liste

######################### firstrun #########################

def write(Seite, Nummer, URL, Aktiv, Refreshaktiv, Refresh, vonbis, marginleft, marginright, margintop, marginbottom):
	conn.execute("DELETE FROM DISPLAYSETS where SEITE=\'"+Seite+"\' AND NUMMER="+unicode(Nummer)+";");
	conn.execute("INSERT INTO DISPLAYSETS (SEITE,NUMMER,URL,AKTIV,REFRESHAKTIV,REFRESH,VONBIS,MARGINLEFT,MARGINRIGHT,MARGINTOP,MARGINBOTTOM) values (?,?,?,?,?,?,?,?,?,?,?)", \
	[unicode(Seite), unicode(Nummer), unicode(URL), unicode(Aktiv), unicode(Refreshaktiv), unicode(Refresh), unicode(vonbis), unicode(marginleft), unicode(marginright), unicode(margintop), unicode(marginbottom)]);
	conn.commit()

######################### Displaysets #########################

def createrow(Nummer):
	write("Links", Nummer, "placeholder.html", 1, 1, 60, "*|*|*|*", "0px", "0px", "0px", "0px")
	write("Rechts", Nummer, "placeholder.html", 1, 1, 60, "*|*|*|*", "0px", "0px", "0px", "0px")

def delrow(Nummer):
	rows = getrows()
	if Nummer is not rows:
		conn.execute("DELETE FROM DISPLAYSETS where NUMMER=?", unicode(Nummer));
		x = rows
		diff = rows - Nummer
		z = 0
		while z < diff:
			conn.execute("UPDATE DISPLAYSETS SET NUMMER = ? where NUMMER= ?", [unicode(Nummer+z), unicode(Nummer+z+1)]);
			conn.commit()
			z = z + 1
	elif Nummer == rows:
		conn.execute("DELETE FROM DISPLAYSETS where NUMMER=?", [unicode(Nummer)]);
		conn.commit()
	else:
		pass

def writesettings(NAME, VAL):
	conn.execute("DELETE FROM SETTINGS where NAME=?", [unicode(NAME)]);
	conn.execute("INSERT INTO SETTINGS (NAME,VALUE) values (\'"+NAME+"\',\'"+VAL+"\');");
	conn.commit()

def updatesettings(NAME, VAL):
	conn.execute("UPDATE SETTINGS SET VALUE=? where NAME=?;", [unicode(VAL), unicode(NAME)]);
	conn.commit()

def readsettings(NAME):
	cursor = conn.execute("SELECT VALUE FROM SETTINGS WHERE NAME=\'"+NAME+"\';");
	return cursor.fetchone()[0]

######################### other functions #########################

def getwidgets():
	cursor = conn.execute("SELECT ID FROM WIDGETS;");
	erg = cursor.fetchall()
	out = []
	for item in range(0,len(erg)):
		out.append(erg[item][0])
	return out

def getwidgTYPfromID(ID):
	cursor = conn.execute("SELECT TYP FROM WIDGETS WHERE ID=?", [unicode(ID)]);
	return cursor.fetchone()[0]

def maxid():
	cursor = conn.execute("SELECT MAX(ID) FROM WIDGETS;");
	return cursor.fetchone()[0]

def newwidget(ID, NAME, TYP, AKTIV, URLw, valign, align, vmargin, margin, width, height):
	conn.execute("DELETE FROM WIDGETS WHERE ID=?", [unicode(ID)]);
	conn.execute("INSERT INTO WIDGETS (ID,NAME,TYP,AKTIV,URL,valign,align,vmargin,margin,width,height) values ("+str(ID)+",\'"+NAME+"\',\'"+TYP+"\',"+unicode(AKTIV)+",\'"+URLw+"\',\'"+valign+"\',\'"+unicode(align)+"\',\'"+vmargin+"\',\'"+unicode(margin)+"\',\'"+unicode(width)+"\',\'"+unicode(height)+"\')");
	conn.commit()

def removewidget(ID):
	anz = int(maxid())
	ID = int(ID)
	if ID is not anz:
		conn.execute("DELETE FROM WIDGETS where ID = ?", [unicode(ID)]);
		x = anz
		diff = anz - ID
		z = 0
		while z < diff:
			conn.execute("UPDATE WIDGETS SET ID = ? where ID = ?", [unicode(ID+z), unicode(ID+z+1)]);
			conn.commit()
			z = z + 1
	elif ID == anz:
		conn.execute("DELETE FROM WIDGETS where ID = ?", [unicode(ID)]);
		conn.commit()
	else:
		pass

######################### other functions #########################

def checkfiletype(datei):
	if ".png" in datei or ".jpg" in datei or ".gif" in datei or ".bmp" in datei or ".jpeg" in datei:
		return "image"
	elif ".mp4" in datei or ".wmv" in datei:
		return "video"
	elif ".pdf" in datei:
		return "pdf"
	elif "youtube" and "watch?v=" in datei:
		return "youtube"
	else:
		return "unknown"

def addpx(string):
	if "px" in unicode(string):
		return unicode(string)
	elif "auto" in unicode(string):
		return unicode(string)
	elif "%" in unicode(string):
		return unicode(string)
	else:
		return unicode(string)+"px"

def isfirstrun():
	import os
	workingdir = os.path.dirname(os.path.realpath(__file__))
	rfr = open(workingdir+"/admin/firstrun", "r")
	read_firstrun = rfr.read()
	rfr.close()
	if int(read_firstrun) == 1:
		print """\
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Redirecting...</title>
	<meta http-equiv="refresh" content="0;url=../admin/index.py">
</head>
<body>
</body>
</html>"""
		exit(0)
	else:
		pass

######################### checkvalues #########################

def testexist(GETNAME, Seite, Nummer):										# Daten aus der Datenbank lesen
	try:
		if getinfo(GETNAME, Seite, Nummer) is not None:
			return getinfo(GETNAME, Seite, Nummer)
		else:
			return "Keine Daten für "+GETNAME
	except:
		return "Keine Daten"

def aktiv(GETNAME, Seite, Nummer):											# Überprüft, ob eine Checkbox aktiviert ist
	try:
		if getinfo(GETNAME, Seite, Nummer) == 1:
			return "checked=\"checked\""
		else:
			return ""
	except:
		return ""

def widgaktiv(widgname, ID):												# Dasselbe wie testexist(), nur für Widgets
	try:
		if getwidgetinfo(widgname, ID, "Aktiv") == 1:
			return "checked=\"checked\""
		else:
			return ""
	except:
		return ""

def valign(widgname, ID, typ):												# Wichtig für die Dropdown Auswahl der Lage von Widgets
	if typ == "valign":
		try:
			if getwidgetinfo(widgname, ID, "valign") == "top":
				return """
										<option value="" disabled selected>top</option>
										<option value="bottom">bottom</option>"""
			elif getwidgetinfo(widgname, ID, "valign") == "bottom":
				return """
										<option value="" disabled selected>bottom</option>
										<option value="top">top</option>"""
		except:
			return """
										<option value="" disabled selected>valign wählen...</option>
										<option value="top">top</option>
										<option value="bottom">bottom</option>"""
	elif typ == "vmargin":
		try:
			if "left" in getwidgetinfo(widgname, ID, "vmargin"):
				return """
												<option value="" disabled selected>left</option>
												<option value="center">center</option>
												<option value="right">right</option>"""
			elif "center" in getwidgetinfo(widgname, ID, "vmargin"):
				return """
												<option value="" disabled selected>center</option>
												<option value="left">left</option>
												<option value="right">right</option>"""
			elif "right" in getwidgetinfo(widgname, ID, "vmargin"):
				return """
												<option value="" disabled selected>right</option>
												<option value="center">center</option>
												<option value="left">left</option>"""
		except:
			return """
												<option value="" disabled selected>Ausrichtung w&aumlhlen...</option>
												<option value="left">left</option>
												<option value="center">center</option>
												<option value="right">right</option>"""
	else:
		pass

def getdate(value, Seite, Nummer):											# Splittet die Daten in der Datenbank mit Anordnung nach (*|*|*|*)
	timespan = getinfo("VONBIS", Seite, Nummer).split("|")					# in einzelne Werte für Uhrzeit, Wochentag, usw auf, um im Interface
	if value == "uhrzeit":													# getrennt angezeigt zu werden
		return timespan[0]
	elif value == "wochentag":
		return timespan[1]
	elif value == "tag":
		return timespan[2]
	elif value == "monat":
		return timespan[3]
	else:
		return "Fehler"

######################### debug #########################

def debug(e):
	import os
	import sys
	import traceback
	import cgi
	scrname = os.environ["SCRIPT_NAME"]
	trace = traceback.format_exc()

	#####################################################

	if "bin/index.py" in scrname:
		isfirstrun()

	if "admin" in scrname:
		css = "../bin/css/materialize.css"
	elif "bin" and not "rollen" in scrname:
		css = "css/materialize.css"
	elif "rollen" in scrname:
		css = "../../bin/css/materialize.css"
	else:
		css = ""

	#####################################################

	if (debugv == 2 or debugv == 707)\
	and (("No such file or directory" and "subst_" in trace)\
	or ("OperationalError" in trace)\
	or ("Warning" in trace)):
		anmerkung = True
	else:
		anmerkung = False

	#####################################################

	print("""\
Content-Type: text/html

<!DOCTYPE html>
<html lang="de">
<head>
	<meta charset="UTF-8">
	<link href=\""""+css+"""\" type="text/css" rel="stylesheet" media="screen,projection"/>
	<meta http-equiv="refresh" content="30">""")

	#####################################################

	if debugv == 707 and not anmerkung:
		print("""
	<style>
	html, body {
		height: 100%;
		overflow: hidden;
	}
	body {
		background-image: url("""+css+"""../resources/error.jpg);
		background-size: auto 40%;
		background-position: right bottom;
		background-repeat: no-repeat;
	}
	</style>""")

	#####################################################

	print("""
</head>
<body>
	<div class="container">""")

	#####################################################

	if debugv == 707 and not anmerkung:
		print("""
		<h3>Oh nein! :(</h3>
		<h4>Ein hochqualifizierter Techniker arbeitet bereits mit Hochdruck an dem Problem!</h4>""")
	else:
		print("""
		<h3>Es ist ein Fehler aufgetreten!</h3>""")

	#####################################################

	if debugv >= 2:

		#################################################

		if anmerkung:
			if "No such file or directory" in trace and "subst_" in trace:
				print("<h4>Die Vertretungsdatei existiert nicht...</h4>")

			elif "OperationalError" in trace:
				print("""\
	<center style="color: #ffffff; background: #a60c0d; border: 2px solid black; margin-top: 3%; padding-bottom: 3%;">
		<h1>Hier stimmt was nicht!</h1>
		Manuell an der Datenbank gespielt, was?
	</center>""")

			elif "Warning" in trace:
				print("""
		<h4>Warnung: """+unicode(e)+"""</h4>""")

		#################################################

		print("""
		<h5>Details:</h5>
		<pre><code>""")
		print(cgi.escape(trace))
		print("		</code></pre>")

	elif debugv == 1:
		print("""
		<h4>Details:<br><h5>""")
		print(unicode(e))
		print("	</h5></h4>")

	else:
		print("""Weitere Informationen über "debug" in common.py!</h3><br><br>""")

	#####################################################

	print("""
		<small>Seite wird in 30 Sekunden neu geladen.</small><br>
		<small>Script: """+scrname+"""</small><br>
		<small>"""+datum.strftime("%d.%m.%Y %H:%M:%S")+"""</small>
	</div>
</body>
</html>""")
	exit(1)