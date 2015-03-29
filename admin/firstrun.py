#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use, copy,
# modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Beilage zu MonitorNjus, 25.03.2015 (Version 0.6.1)

import os
import sqlite3
import common

rfr = open("firstrun", "r")
read_firstrun = rfr.read()

if str(1) in read_firstrun:
	conn = sqlite3.connect('MonitorNjus.db')
	conn.execute('''CREATE TABLE DISPLAYSETS
		(ID INT PRIMARY KEY,
			SEITE			TEXT,
			NUMMER			INT,
			URL				TEXT,
			AKTIV			INT,
			REFRESH 		INT,
			REFRESHAKTIV 	INT,
			VONBIS			TEXT,
			VONBISAKTIV		INT);''')
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

	def write(Seite, Nummer, URL, Aktiv, Refreshaktiv, Refresh, vonbis, vonbiskaktiv):
		conn.execute("DELETE FROM DISPLAYSETS where SEITE=\'"+Seite+"\' AND NUMMER="+str(Nummer)+"");
		conn.execute("INSERT INTO DISPLAYSETS (SEITE,NUMMER,URL,AKTIV,REFRESHAKTIV,REFRESH,VONBIS,VONBISAKTIV) values (\'"+Seite+"\',"+str(Nummer)+",\'"+URL+"\',"+str(Aktiv)+","+str(Refreshaktiv)+","+str(Refresh)+",\'"+vonbis+"\',"+str(vonbiskaktiv)+")");
	def widgets(NAME, AKTIV, URLw, valign, align, vmargin, margin, width, height):
		conn.execute("INSERT INTO WIDGETS (NAME,AKTIV,URL,valign,align,vmargin,margin,width,height) values (\'"+NAME+"\',"+str(AKTIV)+",\'"+URLw+"\',\'"+valign+"\',"+str(align)+",\'"+vmargin+"\',"+str(margin)+",\'"+str(width)+"\',\'"+str(height)+"\')");

	write("Links", 1, "placeholder.html", 0, 0, 60, "*|*|*|*", 0)
	write("Rechts", 1, "placeholder.html", 0, 0, 60, "*|*|*|*", 0)
	write("globalmon", 0, "placeholder.html", 0, 0, 600, "*|*|*|*", 0)
	write("global", 0, "placeholder.html", 0, 0, 300, "*|*|*|*", 0)

	widgets("Admin-Link", 1, "placeholder", "bottom", 0, "center", 0, "0", "0" )
	widgets("Uhr", 1, "resources/uhr1.swf", "bottom", 0, "center", 0, "", "96px" )
	widgets("Logo", 0, "placeholder", "bottom", 0, "center", 0, "100%", "100%" )
	widgets("Freies-Widget", 0, "placeholder", "bottom", 0, "center", 0, "0px", "0px" )

	conn.commit()
	conn.close()
	os.remove('firstrun')
	f = open('firstrun','w')
	f.write("0")

else:
	pass
