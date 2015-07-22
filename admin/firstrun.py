#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 22.07.2015 (Version 0.8.4)

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import imp
workingdir = os.path.dirname(os.path.realpath(__file__))
common = imp.load_source('common', workingdir+"/../common.py")

try:
	rfr = open(workingdir+"/firstrun", "r")
	read_firstrun = rfr.read()
	rfr.close()
	conn = common.sqlite3.connect(workingdir+'/MonitorNjus.db')

	if unicode(1) in read_firstrun:
		conn.execute('''CREATE TABLE DISPLAYSETS
			(ID INT PRIMARY KEY,
				SEITE			TEXT,
				NUMMER			INT,
				URL				TEXT,
				AKTIV			INT,
				REFRESH 		INT,
				REFRESHAKTIV 	INT,
				VONBIS			TEXT,
				MARGINLEFT		TEXT,
				MARGINRIGHT		TEXT,
				MARGINTOP		TEXT,
				MARGINBOTTOM	TEXT);''')
		conn.execute('''CREATE TABLE WIDGETS
			(ID INT PRIMARY KEY,
				NAME			TEXT,
				AKTIV			INT,
				URL				TEXT,
				valign			TEXT,
				align			TEXT,
				vmargin 		TEXT,
				margin			TEXT,
				width			TEXT,
				height			TEXT);''')
		conn.execute('''CREATE TABLE SETTINGS
			(ID INT PRIMARY KEY,
				NAME			TEXT,
				VALUE			TEXT);''')

		def widgets(NAME, AKTIV, URLw, valign, align, vmargin, margin, width, height):
			conn.execute("INSERT INTO WIDGETS (NAME,AKTIV,URL,valign,align,vmargin,margin,width,height) values (\'"+NAME+"\',"+unicode(AKTIV)+",\'"+URLw+"\',\'"+valign+"\',\'"+unicode(align)+"\',\'"+vmargin+"\',\'"+unicode(margin)+"\',\'"+unicode(width)+"\',\'"+unicode(height)+"\')");

		common.write("Links", 1, "placeholder.html", 1, 1, 60, "*|*|*|*", "0px", "0px", "0px", "0px")
		common.write("Rechts", 1, "placeholder.html", 1, 1, 60, "*|*|*|*", "0px", "0px", "0px", "0px")
		common.write("globalmon", 0, "placeholder.html", 1, 0, 600, "*|*|*|*", "0px", "0px", "0px", "0px")
		common.write("global", 0, "placeholder.html", 1, 0, 300, "*|*|*|*", "0px", "0px", "0px", "0px")

		common.writesettings("TEILUNG", "50")

		widgets("Admin-Link", 1, "placeholder", "bottom", "0px", "center", "0px", "0", "0")
		widgets("Uhr", 0, "resources/uhr1.swf", "bottom", "0px", "center", "0px", "auto", "96px")
		widgets("Logo", 0, "placeholder", "bottom", "0px", "left", "0px", "100%", "100%")
		widgets("Freies-Widget", 0, """<iframe name="flipe" scrolling="no" src="http://www.daswetter.com/getwid/ef3e15e299d279eec78fbfc75d5190f6" id="ef3e15e299d279eec78fbfc75d5190f6" style="width: 250px; color: rgb(128, 128, 128); height: 142px;" frameborder="0"></iframe>""", "bottom", "-90px", "right", "145px", "100px", "200px")

		conn.commit()
		conn.close()

		os.remove(workingdir+'/firstrun')
		f = open(workingdir+'/firstrun','w')
		f.write("0")
		f.close()
	else:
		pass

except Exception as e:
	common.debug(e)