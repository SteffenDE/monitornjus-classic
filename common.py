#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 18.06.2015 (Version 0.7.5)

import os
import datetime
import sqlite3

datum = datetime.datetime.now()
version = "0.7.5&beta;"
workingdir = os.getcwd()

############################## Settings ##############################

debugv = 2		  		# Verbosity: 0,1,2 (0 = off, 1 = basic, 2 = high)

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
			raise Exception("listauth und groupauth können nicht gleichzeitig aktiv sein.")
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
				aduser = ad.find_user ()
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
		else:
			pass

##########################################################################################

if "admin" in workingdir:
	conn = sqlite3.connect(workingdir+'/MonitorNjus.db')
elif "bin" in workingdir:
	conn = sqlite3.connect(workingdir+'/../admin/MonitorNjus.db')
else:
	conn = sqlite3.connect(workingdir+'/admin/MonitorNjus.db')

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

def write(Seite, Nummer, URL, Aktiv, Refreshaktiv, Refresh, vonbis, marginleft, marginright, margintop, marginbottom):
	conn.execute("DELETE FROM DISPLAYSETS where SEITE=\'"+Seite+"\' AND NUMMER="+str(Nummer)+"");
	conn.execute("INSERT INTO DISPLAYSETS (SEITE,NUMMER,URL,AKTIV,REFRESHAKTIV,REFRESH,VONBIS,MARGINLEFT,MARGINRIGHT,MARGINTOP,MARGINBOTTOM) values (\'"+Seite+"\',"+str(Nummer)+",\'"+URL+"\',"+str(Aktiv)+","+str(Refreshaktiv)+","+str(Refresh)+",\'"+vonbis+"\',"+str(marginleft)+","+str(marginright)+","+str(margintop)+","+str(marginbottom)+")");
	conn.commit()

def createrow(Nummer):
	write("Links", Nummer, "placeholder.html", 1, 1, 60, "*|*|*|*", 0, 0, 0, 0)
	write("Rechts", Nummer, "placeholder.html", 1, 1, 60, "*|*|*|*", 0, 0, 0, 0)

def delrow(Nummer):
	rows = getrows()
	if Nummer is not rows:
		conn.execute("DELETE FROM DISPLAYSETS where NUMMER="+str(Nummer)+"");
		x = rows
		diff = rows - Nummer
		z = 0
		while z < diff:
			conn.execute("UPDATE DISPLAYSETS SET NUMMER = "+str(Nummer+z)+" where NUMMER="+str(Nummer+z+1)+"");
			conn.commit()
			z = z + 1
	elif Nummer == rows:
		conn.execute("DELETE FROM DISPLAYSETS where NUMMER="+str(Nummer)+"");
		conn.commit()
	else:
		pass

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
	if "px" in string:
		return string
	elif "auto" in string:
		return string
	else:
		return string+"px"

def isfirstrun():
	import os
	workingdir = os.getcwd()
	import imp
	if "admin" in workingdir:
		rfr = open(workingdir+"/firstrun", "r")
		read_firstrun = rfr.read()
		rfr.close()
	elif "bin" in workingdir:
		rfr = open(workingdir+"/../admin/firstrun", "r")
		read_firstrun = rfr.read()
		rfr.close()
	else:
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

def debug(e):
	import os
	if "bin/index.py" in os.environ["SCRIPT_NAME"]:
		isfirstrun()
	else:
		pass
	if "bin" in workingdir:
		css = "css/"
	elif "admin" in workingdir:
		css = "../bin/css/"
	else:
		if "bin" in os.environ["SCRIPT_NAME"]:
			css = "css/"
		elif "admin" in os.environ["SCRIPT_NAME"]:
			css = "../bin/css/"
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
	<div class="container">"""
	if debugv >= 2:
		import traceback
		print """\
	<h3>Es ist ein Fehler aufgetreten!</h3>
	<h4>Details:</h4>
	<pre><code>"""
		print traceback.format_exc().replace(">","&gt;").replace("<",'&lt;').replace("\"",'&quot;')
		print "	</code></pre>"
	elif debugv == 1:
		print """\
	<h3>Es ist ein Fehler aufgetreten!</h3>
	<h4>Details:<br>"""
		print e
		print "	</h4>"
	else:
		print """<h3>Es ist ein Fehler aufgetreten.<br>Weitere Informationen über "debug" in common.py!</h3>"""
	print """\
	<small>Seite wird in 30 Sekunden neu geladen.</small><br>
	<small>Script: """+os.environ["SCRIPT_NAME"]+"""</small>
	</div>
</body>
</html>"""
