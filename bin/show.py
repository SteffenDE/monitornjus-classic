#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 05.08.2015 (Version 0.9.1)

import os
import sys
import imp
workingdir = os.path.dirname(os.path.realpath(__file__))
common = imp.load_source('common', workingdir+"/../common.py")

try:
	checktime = imp.load_source('checktime', workingdir+"/../admin/checktime.py")

	rows = common.getrows()
	teilung = int(common.readsettings("TEILUNG"))

	timeL = False
	timeR = False
	geteilt = False
	linksgeteilt = common.getgeteilt("Links")
	rechtsgeteilt = common.getgeteilt("Rechts")

	x = 1
	while x <= rows:
		if checktime.match(common.getinfo("VONBIS", "Links", x),common.datum.now()) and common.getinfo("AKTIV", "Links", x):
			timeL = True
		if checktime.match(common.getinfo("VONBIS", "Rechts", x),common.datum.now()) and common.getinfo("AKTIV", "Rechts", x):
			timeR = True
		if timeL and timeR:
			break
		x = x + 1

	if linksgeteilt and rechtsgeteilt and timeL and timeR:
		geteilt = True

	if geteilt:
		disp = u"""\
<frameset frameborder="0" rows="*,0">
	<frameset frameborder="0" cols="""+str(teilung)+""","""+str(100-teilung)+""">
		<frame scrolling="no" src="contentset.py?seite=1" name="links" />
		<frame scrolling="no" src="contentset.py?seite=2" name="rechts" />
	</frameset> 
</frameset>"""
	elif (linksgeteilt and not rechtsgeteilt and timeL) or (linksgeteilt and rechtsgeteilt and timeL and not timeR):
		disp = u"""\
<frameset frameborder="0" rows="*,0">
	<frame scrolling="no" src="contentset.py?seite=1" name="links" />
</frameset>"""
	elif (rechtsgeteilt and not linksgeteilt and timeR) or (rechtsgeteilt and linksgeteilt and timeR and not timeL):
		disp = u"""\
<frameset frameborder="0" rows="*,0">
	<frame scrolling="no" src="contentset.py?seite=2" name="rechts" />
</frameset>"""
	else:
		raise Warning("Keine Seite aktiv")

	if common.getinfo("REFRESHAKTIV", "global", 0) == 1:
		refresh = u"	<META HTTP-EQUIV=\"refresh\" CONTENT=\""+unicode(common.getinfo("REFRESH", "global", 0))+"\">"
	else:
		refresh = u""

	print u"Content-Type: text/html;charset=utf-8\n"
	print u"""\
<!DOCTYPE html>
<html lang="de">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no"/>
	<link href="css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>"""
	print unicode(refresh)
	print u"""\
	<title>MonitorNjus</title>
	<!-- MonitorNjus -->
	<!-- Copyright (c) """+unicode(common.datum.year)+""" Steffen Deusch -->
	<!-- https://github.com/SteffenDE/MonitorNjus -->
</head>"""
	####     # = debug     ####
	#print timeL
	#print timeR
	#print geteilt
	print unicode(disp)
	sys.stdout.write(u"</html>")

except Exception as e:
	common.debug(e)