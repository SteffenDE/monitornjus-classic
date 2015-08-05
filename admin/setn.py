#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 27.07.2015 (Version 0.9)

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import imp
workingdir = os.path.dirname(os.path.realpath(__file__))
common = imp.load_source('common', workingdir+"/../common.py")

def updateurl_refresh(Name, GETNAME, Seite, Nummer, widgname):
	if "index" in referer:
		gval = form.getfirst(Name, None)
		if gval is not None:
			val = gval
		else:
			val = None
		if val is not None:
			if val == common.getinfo(GETNAME, Seite, Nummer):
				pass
			else:
				common.writeinfo(Seite, Nummer, GETNAME, unicode(val))
	elif "widgets" in referer:
		gval = form.getfirst(Name, None)
		if gval is not None:
			val = gval
		else:
			val = None
		if val is not None:
			if val == common.getwidgetinfo(widgname, Nummer, GETNAME):
				pass
			else:
				common.writewidgetinfo(widgname, Nummer, GETNAME, unicode(val))
	else:
		raise Warning("Function updateurl_refresh: This referer does not exist.")

def updateaktiv(Name, GETNAME, Seite, Nummer, widgname, hidden):
	if hidden is None:
		val_flag = 1
	else:
		val_flag = 0

	if "index" in referer:
		if val_flag == common.getinfo(GETNAME, Seite, Nummer):
			pass
		else:
			common.writeinfo(Seite, Nummer, GETNAME, unicode(val_flag))
	elif "widgets" in referer:
		if val_flag == common.getwidgetinfo(widgname, ID, GETNAME):
			pass
		else:
			common.writewidgetinfo(widgname, Nummer, GETNAME, unicode(val_flag))
	else:
		raise Warning("Function updateaktiv: This referer does not exist.")

def update_align(Name, GETNAME, widgname, ID):
	if "widgets" in referer:
		if form.getfirst(Name, None):
			val = form.getfirst(Name, None)
		else:
			val = None
		if val is not None:
			if unicode(val) == common.getwidgetinfo(widgname, ID, GETNAME):
				pass
			else:
				common.writewidgetinfo(widgname, ID, GETNAME, unicode(val))
	else:
		raise Warning("Function update_align: This referer is not allowed.")

def updatetime(Seite, Nummer):
	if "index" in referer:
		uhrzeit = form.getfirst("uhrzeit-"+Seite+"-"+unicode(Nummer), None)
		wochentag = form.getfirst("wochentag-"+Seite+"-"+unicode(Nummer), None)
		tag = form.getfirst("tag-"+Seite+"-"+unicode(Nummer), None)
		monat = form.getfirst("monat-"+Seite+"-"+unicode(Nummer), None)
		if uhrzeit is None and wochentag is None and tag is None and monat is None:
			pass
		else:
			if uhrzeit is None:
				uhrzeit = "*"
			if wochentag is None:
				wochentag = "*"
			if tag is None:
				tag = "*"
			if monat is None:
				monat = "*"
			common.writeinfo(Seite, Nummer, "VONBIS", uhrzeit+"|"+wochentag+"|"+tag+"|"+monat)
	else:
		raise Warning("Function updatetime: This referer is not allowed.")

def updateteilung():
	if "index" in referer:
		teilung = form.getfirst("teilung", None)
		if teilung is not None:
			if teilung == common.readsettings("TEILUNG"):
				pass
			else:
				common.updatesettings("TEILUNG", teilung)
	else:
		raise Warning("Function updateteilung: This referer is not allowed.")

try:
	import cgi, cgitb
	#import cgitb; cgitb.enable()
	
	if common.authentication:
		auth = imp.load_source("auth", workingdir+"/../auth.py")
		auth.me()

	form = cgi.FieldStorage()
	referer = form.getfirst('referer', None)

	if "index" in referer:
		refresh = "<meta http-equiv=\"refresh\" content=\"0; URL=../admin/index.py\">"

		for item in form:
			if not "teilung" in item and not "referer" in item:
				splitteditem = item.split("-")
				name = splitteditem[0]
				seite = splitteditem[1]
				nummer = splitteditem[2]
				if not "uhrzeit" in item and not "wochentag" in item and not "tag" in item and not "monat" in item:
					if not "aktiv" in name.lower():
						updateurl_refresh(item, name, seite, nummer, "")
					else:
						if "hidden." in item.lower() and not item[7:] in form:
							hidden = 0
							updateaktiv(item[7:], name[7:], seite, nummer, "", hidden)
						elif "hidden." in item.lower() and item[7:] in form:
							pass
						else:
							hidden = None
							updateaktiv(item, name, seite, nummer, "", hidden)
				else:
					updatetime(seite, nummer)
			else:
				updateteilung()

	elif "widgets" in referer:
		refresh = "<meta http-equiv=\"refresh\" content=\"0; URL=../admin/widgets.py\">"

		for item in form:
			if not "referer" in item:
				splitteditem = item.split("-")
				art = splitteditem[0]
				typ = splitteditem[1]
				ID = splitteditem[2]
				if not "aktiv" in art.lower():
					if not "url" in art.lower():
						update_align(item, art, typ, ID)
					else:
						updateurl_refresh(item, art, "", ID, typ)
				else:
					if "hidden." in item.lower() and not item[7:] in form:
						hidden = 0
						updateaktiv(item[7:], art[7:], "", ID, typ, hidden)
					elif "hidden." in item.lower() and item[7:] in form:
						pass
					else:
						hidden = None
						updateaktiv(item, art, "", ID, typ, hidden)

	elif "row" in referer:
		refresh = "<meta http-equiv=\"refresh\" content=\"0; URL=../admin/index.py\">"
		cnum = form.getfirst("createnum", None)
		dnum = form.getfirst("delnum", None)
		if cnum is not None and cnum.isdigit():
			num = int(cnum)
			if num == int(common.getrows())+1:
				common.createrow(num)
			else:
				raise Warning("Neues Displayset - falsche Zahl: "+str(num))
		elif dnum is not None and dnum.isdigit():
			num = int(dnum)
			if num <= int(common.getrows()):
				common.delrow(num)
			else:
				raise Warning("Displayset löschen - falsche Zahl: "+str(num))

	elif "newwidget" in referer:
		refresh = "<meta http-equiv=\"refresh\" content=\"0; URL=../admin/widgets.py\">"
		if form.getfirst("art", None):
			val = form.getfirst("art", None)
		else:
			val = None
		if val is not None:
			if val == "Logo" or val == "Freies_Widget":
				count = list(common.getwidgets())
				ID = int(common.maxid())+1
				common.newwidget(ID, val, val, 0, "placeholder", "bottom", "0px", "center", "0px", "100%", "100%")
			else:
				raise Warning("Falsches Widget: "+val)

	elif "delwidget" in referer:
		refresh = "<meta http-equiv=\"refresh\" content=\"0; URL=../admin/widgets.py\">"
		num = form.getfirst("delnum", None)
		if num is not None:
			common.removewidget(unicode(num))

	elif "triggerrefresh" in referer:
		refresh = "<meta http-equiv=\"refresh\" content=\"0; URL=../admin/index.py\">"

	else:
		refresh = ""

	print """\
Content-Type: text/html\n
<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">"""
	#for item in form:
		#print item+": "+form[item].value
	print refresh
	print """\
</head>
<body>
</body>"""
	import sys
	sys.stdout.write("</html>")
	del sys

	if common.triggerrefresh:
		datei = open(workingdir+"/../bin/refresh", "w")
		datei.write("1")
		datei.close()

except Exception as e:
	common.debug(e)