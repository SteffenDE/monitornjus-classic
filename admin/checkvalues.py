#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 25.03.2015 (Version 0.6.1)

import common

def testexist(GETNAME, Seite, Nummer):
	try:
		if common.getinfo(GETNAME, Seite, Nummer):
			return common.getinfo(GETNAME, Seite, Nummer)
	except:
		return "Keine Daten"

def aktiv(GETNAME, Seite, Nummer):
	try:
		if common.getinfo(GETNAME, Seite, Nummer) == 1:
			return "checked=\"checked\""
		else:
			return ""
	except:
		return ""

def testexistwidg(GETNAME, widgname):
	try:
		if common.getwidgetinfo(widgname, GETNAME) is not None:
			if str(common.getwidgetinfo(widgname, GETNAME)).isdigit():
				return int(common.getwidgetinfo(widgname, GETNAME))
			else: 
				return str(common.getwidgetinfo(widgname, GETNAME))
	except:
		return "Fehler in checkvalues.testexistwidg"

def widgaktiv(widgname):
	try:
		if common.getwidgetinfo(widgname, "Aktiv") == 1:
			return "checked=\"checked\""
		else:
			return ""
	except:
		return ""

def valign(widgname, typ):
	if typ == "valign":
		try:
			if common.getwidgetinfo(widgname, "valign") == "top":
				return """
										<option value="" disabled selected>top</option>
										<option value="bottom">bottom</option>"""
			elif common.getwidgetinfo(widgname, "valign") == "bottom":
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
			if "left" in common.getwidgetinfo(widgname, "vmargin"):
				return """
												<option value="" disabled selected>left</option>
												<option value="center">center</option>
												<option value="right">right</option>"""
			elif "center" in common.getwidgetinfo(widgname, "vmargin"):
				return """
												<option value="" disabled selected>center</option>
												<option value="left">left</option>
												<option value="right">right</option>"""
			elif "right" in common.getwidgetinfo(widgname, "vmargin"):
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

def getdate(value, Seite, Nummer):
	timespan = common.getinfo("VONBIS", Seite, Nummer).split("|")
	if value == "uhrzeit":
		return timespan[0]
	elif value == "wochentag":
		return timespan[1]
	elif value == "tag":
		return timespan[2]
	elif value == "monat":
		return timespan[3]
	else:
		return "Fehler"

url1 = testexist("URL", "Links", 1)
url2 = testexist("URL", "Rechts", 1)
url1_2 = testexist("URL", "Links", 2)
url2_2 = testexist("URL", "Rechts", 2)
refresh1 = testexist("REFRESH", "Links", 1)
refresh2 = testexist("REFRESH", "Rechts", 1)
refresh1_2 = testexist("REFRESH", "Links", 2)
refresh2_2 = testexist("REFRESH", "Rechts", 2)
refreshmon = testexist("REFRESH", "globalmon", 0)
refreshall = testexist("REFRESH", "global", 0)

leftenabled = aktiv("AKTIV", "Links", 1)
rightenabled = aktiv("AKTIV", "Rechts", 1)
leftenabled_2 = aktiv("AKTIV", "Links", 2)
rightenabled_2 = aktiv("AKTIV", "Rechts", 2)
refreshleftenabled = aktiv("REFRESHAKTIV", "Links", 1)
refreshrightenabled = aktiv("REFRESHAKTIV", "Rechts", 1)
refreshleftenabled_2 = aktiv("REFRESHAKTIV", "Links", 2)
refreshrightenabled_2 = aktiv("REFRESHAKTIV", "Rechts", 2)
refreshmonenabled = aktiv("REFRESHAKTIV", "globalmon", 0)
refreshallenabled = aktiv("REFRESHAKTIV", "global", 0)

adminlinkaktiv = widgaktiv("Admin-Link")
uhraktiv = widgaktiv("Uhr")
logoaktiv = widgaktiv("Logo")
widgetaktiv = widgaktiv("Freies-Widget")

adminlinkvalign = valign("Admin-Link", "valign")
adminlinkvmargin = valign("Admin-Link", "vmargin")
uhrvalign = valign("Uhr", "valign")
uhrvmargin = valign("Uhr", "vmargin")
logovalign = valign("Logo", "valign")
logovmargin = valign("Logo", "vmargin")
widgetvalign = valign("Freies-Widget", "valign")
widgetvmargin = valign("Freies-Widget", "vmargin")

adminlinkalign = str(testexistwidg("align", "Admin-Link"))
adminlinkmargin = str(testexistwidg("margin", "Admin-Link"))
uhralign = str(testexistwidg("align", "Uhr"))
uhrmargin = str(testexistwidg("margin", "Uhr"))
logoalign = str(testexistwidg("align", "Logo"))
logomargin = str(testexistwidg("margin", "Logo"))
widgetalign = str(testexistwidg("align", "Freies-Widget"))
widgetmargin = str(testexistwidg("margin", "Freies-Widget"))

uhrlink = testexistwidg("URL", "Uhr")
logolink = testexistwidg("URL", "Logo")
widgetlink = testexistwidg("URL", "Freies-Widget")

uhrwidth = str(testexistwidg("width", "Uhr"))
uhrheight = str(testexistwidg("height", "Uhr"))
logowidth = str(testexistwidg("width", "Logo"))
logoheight = str(testexistwidg("height", "Logo"))
widgetwidth = str(testexistwidg("width", "Freies-Widget"))
widgetheight = str(testexistwidg("height", "Freies-Widget"))