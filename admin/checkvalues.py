#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 22.06.2015 (Version 0.7.6)

import os
import imp
workingdir = os.getcwd()
if "admin" in workingdir:
	common = imp.load_source('common', workingdir+"/../common.py")
else:
	common = imp.load_source('common', workingdir+"/common.py")

def testexist(GETNAME, Seite, Nummer):										# Daten aus der Datenbank lesen
	try:
		if common.getinfo(GETNAME, Seite, Nummer):
			return common.getinfo(GETNAME, Seite, Nummer)
	except:
		return "Keine Daten"

def aktiv(GETNAME, Seite, Nummer):											# Überprüft, ob eine Checkbox aktiviert ist
	try:
		if common.getinfo(GETNAME, Seite, Nummer) == 1:
			return "checked=\"checked\""
		else:
			return ""
	except:
		return ""

def testexistwidg(GETNAME, widgname):										# Widget Daten aus der Datenbank lesen
	try:
		if common.getwidgetinfo(widgname, GETNAME) is not None:
			if str(common.getwidgetinfo(widgname, GETNAME)).isdigit():
				return int(common.getwidgetinfo(widgname, GETNAME))
			else: 
				return str(common.getwidgetinfo(widgname, GETNAME))
	except:
		return "Fehler in checkvalues.testexistwidg"

def widgaktiv(widgname):													# Dasselbe wie testexist(), nur für Widgets
	try:
		if common.getwidgetinfo(widgname, "Aktiv") == 1:
			return "checked=\"checked\""
		else:
			return ""
	except:
		return ""

def valign(widgname, typ):													# Wichtig für die Dropdown Auswahl der Lage von Widgets
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

def getdate(value, Seite, Nummer):											# Splittet die Daten in der Datenbank mit Anordnung nach (*|*|*|*)
	timespan = common.getinfo("VONBIS", Seite, Nummer).split("|")			# in einzelne Werte für Uhrzeit, Wochentag, usw auf, um im Interface
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