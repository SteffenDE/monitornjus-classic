#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 04.07.2015 (Version 0.8.1)

import os
import datetime
import sqlite3

datum = datetime.datetime.now()
version = "0.8.1&beta;"
workingdir = os.path.dirname(os.path.realpath(__file__))

############################## Settings ##############################

debugv = 2				# Verbosity: 0,1,2 (0 = off, 1 = basic, 2 = mit Anmerkungen, 3 = Traceback)

###### Windows-Authentifizierung ######
### Art ###

listauth = False     	# Wenn True, Benutzer in "userliste" eintragen. Benutzer benötigen Schreibrechte im ADMIN Verzeichnis!
groupauth = False     	# Wenn True, muss pywin32 installiert sein! Gruppe für die Authentifizierung unter group = "xy" festlegen!

### Userliste ###

userliste = [
"administrator",
"groi",
"peter.praker"
]

### Windows-Domäne ###

domain = "SCHULE"

### Gruppe ###

group = "G_Projekt_MonitorNjus"

######################################################################

###### Authentifizierungsfunktion ######

def authenticated():
		if groupauth and listauth:
			raise Exception("listauth und groupauth können (noch) nicht gleichzeitig aktiv sein.")
		if listauth:
				import os
				user = os.environ["REMOTE_USER"]
				if user.lower().replace(domain.lower()+"\\", "") in userliste:
						pass
				else:
						print "Content-Type: text/html"
						print
						print """\
<!DOCTYPE html>
<html>
<body>
<h1>Du (%s) hast hier nichts verloren!</h1>
</body>
</html>""" % user
						exit(0)
		elif groupauth:
				import sys
				reload(sys)
				sys.setdefaultencoding('utf-8')
				import ad
				import os
				user = os.environ["REMOTE_USER"]
				aduser = ad.find_user()
				if group.lower() in str(aduser.memberOf).lower() or "administrator" in user.lower():
						pass
				else:
						print "Content-Type: text/html"
						print
						print """\
<!DOCTYPE html>
<html>
<body>
<h1>Du (%s) hast hier nichts verloren!</h1>
</body>
</html>""" % user
						exit(0)
				del sys
		else:
			pass

##########################################################################################

conn = sqlite3.connect(workingdir+'/admin/MonitorNjus.db')

######################### basics #########################

def getinfo(Info, Seite, Nummer):
	cursor = conn.execute("SELECT "+Info+" FROM DISPLAYSETS WHERE SEITE=\'"+Seite+"\' AND NUMMER="+str(Nummer)+";");
	return cursor.fetchone()[0]

def writeinfo(Seite, Nummer, Info, value):
	if str(value).isdigit():
		conn.execute("UPDATE DISPLAYSETS SET "+Info+"="+str(value)+" WHERE SEITE=\'"+Seite+"\' AND NUMMER="+str(Nummer)+";");
	else:
		conn.execute("UPDATE DISPLAYSETS SET "+Info+"=\'"+value+"\' WHERE SEITE=\'"+Seite+"\' AND NUMMER="+str(Nummer)+";");
	conn.commit()

def getwidgetinfo(NAME, Info):
	cursor = conn.execute("SELECT "+Info+" FROM WIDGETS WHERE NAME=\'"+str(NAME)+"\';");
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

######################### rows #########################

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

######################### firstrun #########################

def write(Seite, Nummer, URL, Aktiv, Refreshaktiv, Refresh, vonbis, marginleft, marginright, margintop, marginbottom):
	conn.execute("DELETE FROM DISPLAYSETS where SEITE=\'"+Seite+"\' AND NUMMER="+str(Nummer)+";");
	conn.execute("INSERT INTO DISPLAYSETS (SEITE,NUMMER,URL,AKTIV,REFRESHAKTIV,REFRESH,VONBIS,MARGINLEFT,MARGINRIGHT,MARGINTOP,MARGINBOTTOM) values (\'"+Seite+"\',"+str(Nummer)+",\'"+URL+"\',"+str(Aktiv)+","+str(Refreshaktiv)+","+str(Refresh)+",\'"+vonbis+"\',\'"+str(marginleft)+"\',\'"+str(marginright)+"\',\'"+str(margintop)+"\',\'"+str(marginbottom)+"\');");
	conn.commit()

def createrow(Nummer):
	write("Links", Nummer, "placeholder.html", 1, 1, 60, "*|*|*|*", "0px", "0px", "0px", "0px")
	write("Rechts", Nummer, "placeholder.html", 1, 1, 60, "*|*|*|*", "0px", "0px", "0px", "0px")

def delrow(Nummer):
	rows = getrows()
	if Nummer is not rows:
		conn.execute("DELETE FROM DISPLAYSETS where NUMMER="+str(Nummer)+";");
		x = rows
		diff = rows - Nummer
		z = 0
		while z < diff:
			conn.execute("UPDATE DISPLAYSETS SET NUMMER = "+str(Nummer+z)+" where NUMMER="+str(Nummer+z+1)+";");
			conn.commit()
			z = z + 1
	elif Nummer == rows:
		conn.execute("DELETE FROM DISPLAYSETS where NUMMER="+str(Nummer)+";");
		conn.commit()
	else:
		pass

def writesettings(NAME, VAL):
	conn.execute("DELETE FROM SETTINGS where NAME=\'"+NAME+"\';");
	conn.execute("INSERT INTO SETTINGS (NAME,VALUE) values (\'"+NAME+"\',\'"+VAL+"\');");
	conn.commit()

def updatesettings(NAME, VAL):
	conn.execute("UPDATE SETTINGS SET VALUE=\'"+VAL+"\' where NAME=\'"+NAME+"\';");
	conn.commit()

def readsettings(NAME):
	cursor = conn.execute("SELECT VALUE FROM SETTINGS WHERE NAME=\'"+NAME+"\';");
	return cursor.fetchone()[0]

######################### other functions #########################

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

def addpx(string):
	if "px" in str(string):
		return str(string)
	elif "auto" in str(string):
		return str(string)
	elif "%" in str(string):
		return str(string)
	else:
		return str(string)+"px"

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
		if getinfo(GETNAME, Seite, Nummer):
			return getinfo(GETNAME, Seite, Nummer)
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

def testexistwidg(GETNAME, widgname):										# Widget Daten aus der Datenbank lesen
	try:
		if getwidgetinfo(widgname, GETNAME) is not None:
			if str(getwidgetinfo(widgname, GETNAME)).isdigit():
				return int(getwidgetinfo(widgname, GETNAME))
			else: 
				return str(getwidgetinfo(widgname, GETNAME))
	except:
		return "Fehler in checkvalues.testexistwidg"

def widgaktiv(widgname):													# Dasselbe wie testexist(), nur für Widgets
	try:
		if getwidgetinfo(widgname, "Aktiv") == 1:
			return "checked=\"checked\""
		else:
			return ""
	except:
		return ""

def valign(widgname, typ):													# Wichtig für die Dropdown Auswahl der Lage von Widgets
	if typ == "valign":
		try:
			if getwidgetinfo(widgname, "valign") == "top":
				return """
										<option value="" disabled selected>top</option>
										<option value="bottom">bottom</option>"""
			elif getwidgetinfo(widgname, "valign") == "bottom":
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
			if "left" in getwidgetinfo(widgname, "vmargin"):
				return """
												<option value="" disabled selected>left</option>
												<option value="center">center</option>
												<option value="right">right</option>"""
			elif "center" in getwidgetinfo(widgname, "vmargin"):
				return """
												<option value="" disabled selected>center</option>
												<option value="left">left</option>
												<option value="right">right</option>"""
			elif "right" in getwidgetinfo(widgname, "vmargin"):
				return """
												<option value="" disabled selected>right</option>
												<option value="center">center</option>
												<option value="left">left</option>"""
		except:
			return """
												<option value="" disabled selected>valign w&aumlhlen...</option>
												<option value="left">left</option>
												<option value="center">center</option>
												<option value="right">right</option>"""
	else:
		pass

def getdate(value, Seite, Nummer):											# Splittet die Daten in der Datenbank mit Anordnung nach (*|*|*|*)
	timespan = getinfo("VONBIS", Seite, Nummer).split("|")			# in einzelne Werte für Uhrzeit, Wochentag, usw auf, um im Interface
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
	scrname = os.environ["SCRIPT_NAME"]
	#import cgitb; cgitb.enable()
	import traceback
	if "bin/index.py" in scrname:
		isfirstrun()
	else:
		pass
	if "bin" and not "rollen" in scrname:
		css = "css/"
	elif "admin" in scrname:
		css = "../bin/css/"
	elif "rollen" in scrname:
		css = "../../bin/css/"
	else:
		css = "bin/css/"
	print "Content-Type: text/html"
	print
	print """<!DOCTYPE html>
<html lang="de">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no"/>
	<link href=\""""+css+"""materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	<META HTTP-EQUIV="refresh" CONTENT="30">
</head>
<body>
	<div class="container">
		<h3>Es ist ein Fehler aufgetreten!</h3>"""
	trace = traceback.format_exc()
	if "OperationalError" in trace:
		print """\
	<center style="color: #ffffff; background: #a60c0d; border: 2px solid black; margin-top: 3%; padding-bottom: 3%;">
		<h1>Hier stimmt was nicht!</h1>
		Manuell an der Datenbank gespielt, was?
	</center>"""
	if debugv >= 2:
		import cgi
		if debugv == 2:
			if "No such file or directory" and "vertretung.py" in str(trace):
				print "<h4>Die Vertretungsdatei existiert nicht...</h4>"
			elif "OperationalError" in trace:
				print """\
	<center style="color: #ffffff; background: #a60c0d; border: 2px solid black; margin-top: 3%; padding-bottom: 3%;">
		<h1>Hier stimmt was nicht!</h1>
		Manuell an der Datenbank gespielt, was?
	</center>"""
		print """\
	<h4>Details:</h4>
	<pre><code>"""
		sys.stdout.write(cgi.escape(trace))
		print "	</code></pre>"
	elif debugv == 1:
		print """\
	<h3>Es ist ein Fehler aufgetreten!</h3>
	<h4>Details:<br><h5>"""
		print str(e)
		print "	</h5></h4>"
	else:
		print """<br>Weitere Informationen über "debug" in common.py!</h3>"""
	print """\
	<small>Seite wird in 30 Sekunden neu geladen.</small><br>
	<small>Script: """+scrname+"""</small><br>
	<small>"""+datum.strftime("%d.%m.%Y %H:%M:%S")+"""</small>
	</div>
</body>"""
	sys.stdout.write("</html>")
	del sys
	exit(1)