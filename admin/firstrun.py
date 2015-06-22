#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 22.06.2015 (Version 0.7.6)

try:
	import os
	workingdir = os.getcwd()
	import imp
	if "admin" in workingdir:
		common = imp.load_source('common', workingdir+"/../common.py")
		rfr = open(workingdir+"/firstrun", "r")
		read_firstrun = rfr.read()
		rfr.close()
		conn = common.sqlite3.connect(workingdir+'/MonitorNjus.db')
	else:
		common = imp.load_source('common', workingdir+"/common.py")
		rfr = open(workingdir+"/admin/firstrun", "r")
		read_firstrun = rfr.read()
		rfr.close()
		conn = common.sqlite3.connect(workingdir+'/admin/MonitorNjus.db')

	if str(1) in read_firstrun:
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

		def widgets(NAME, AKTIV, URLw, valign, align, vmargin, margin, width, height):
			conn.execute("INSERT INTO WIDGETS (NAME,AKTIV,URL,valign,align,vmargin,margin,width,height) values (\'"+NAME+"\',"+str(AKTIV)+",\'"+URLw+"\',\'"+valign+"\',\'"+str(align)+"\',\'"+vmargin+"\',\'"+str(margin)+"\',\'"+str(width)+"\',\'"+str(height)+"\')");

		common.write("Links", 1, "placeholder.html", 1, 1, 60, "*|*|*|*", "0px", "0px", "0px", "0px")
		common.write("Rechts", 1, "placeholder.html", 1, 1, 60, "*|*|*|*", "0px", "0px", "0px", "0px")
		common.write("globalmon", 0, "placeholder.html", 1, 0, 600, "*|*|*|*", "0px", "0px", "0px", "0px")
		common.write("global", 0, "placeholder.html", 1, 0, 300, "*|*|*|*", "0px", "0px", "0px", "0px")

		widgets("Admin-Link", 1, "placeholder", "bottom", "0px", "center", "0px", "0", "0")
		widgets("Uhr", 0, "resources/uhr1.swf", "bottom", "0px", "center", "0px", "auto", "96px")
		widgets("Logo", 0, "placeholder", "bottom", "0px", "left", "0px", "100%", "100%")
		widgets("Freies-Widget", 0, """<iframe name="flipe" scrolling="no" src="http://www.daswetter.com/getwid/ef3e15e299d279eec78fbfc75d5190f6" id="ef3e15e299d279eec78fbfc75d5190f6" style="width: 250px; color: rgb(128, 128, 128); height: 142px;" frameborder="0"></iframe>""", "bottom", "-90px", "right", "145px", "100px", "200px")

		conn.commit()
		conn.close()

		if "admin" in workingdir:
			os.remove(workingdir+'/firstrun')
			f = open(workingdir+'/firstrun','w')
			f.write("0")
			f.close()
		else:
			os.remove(workingdir+'/admin/firstrun')
			f = open(workingdir+'/admin/firstrun','w')
			f.write("0")
			f.close()
	else:
		pass

except Exception as e:
	common.debug(e)