#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 18.06.2015 (Version 0.7.5)

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
				MARGINLEFT		INT,
				MARGINRIGHT		INT,
				MARGINTOP		INT,
				MARGINBOTTOM	INT);''')
		conn.execute('''CREATE TABLE WIDGETS
			(ID INT PRIMARY KEY,
				NAME			TEXT,
				AKTIV			INT,
				URL				TEXT,
				valign			TEXT,
				align			INT,
				vmargin 		TEXT,
				margin			INT,
				width			TEXT,
				height			TEXT);''')

		def widgets(NAME, AKTIV, URLw, valign, align, vmargin, margin, width, height):
			conn.execute("INSERT INTO WIDGETS (NAME,AKTIV,URL,valign,align,vmargin,margin,width,height) values (\'"+NAME+"\',"+str(AKTIV)+",\'"+URLw+"\',\'"+valign+"\',"+str(align)+",\'"+vmargin+"\',"+str(margin)+",\'"+str(width)+"\',\'"+str(height)+"\')");

		common.write("Links", 1, "placeholder.html", 1, 1, 60, "*|*|*|*", 0, 0, 0, 0)
		common.write("Rechts", 1, "placeholder.html", 1, 1, 60, "*|*|*|*", 0, 0, 0, 0)
		common.write("globalmon", 1, "placeholder.html", 1, 0, 600, "*|*|*|*", 0, 0, 0, 0)
		common.write("global", 1, "placeholder.html", 1, 0, 300, "*|*|*|*", 0, 0, 0, 0)

		widgets("Admin-Link", 1, "placeholder", "bottom", 0, "center", 0, "0", "0")
		widgets("Uhr", 0, "resources/uhr1.swf", "bottom", 0, "center", 0, "", "96px")
		widgets("Logo", 0, "placeholder", "bottom", 0, "center", 0, "100%", "100%")
		widgets("Freies-Widget", 0, "placeholder", "bottom", 0, "center", 0, "0px", "0px")

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