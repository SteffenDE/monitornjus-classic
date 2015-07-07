#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 04.07.2015 (Version 0.8.1)

import os
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
		disp = """\
	<iframe scrolling="no" frameborder="0" src="contentset.py?seite=1" name="links" style="float: left; position:static; width: """+str(teilung)+"""%;" ></iframe>
	<iframe scrolling="no" frameborder="0" src="contentset.py?seite=2" name="rechts" style="float: right; position:static; width: """+str(100-teilung)+"""%;" ></iframe>"""
	elif (linksgeteilt and not rechtsgeteilt and timeL) or (linksgeteilt and rechtsgeteilt and timeL and not timeR):
		disp = """\
	<iframe scrolling="no" frameborder="0" src="contentset.py?seite=1" name="links" style="position:static; width: 100%;" ></iframe>"""
	elif (rechtsgeteilt and not linksgeteilt and timeR) or (rechtsgeteilt and linksgeteilt and timeR and not timeL):
		disp = """\
	<iframe scrolling="no" frameborder="0" src="contentset.py?seite=2" name="rechts" style="position:static; width: 100%;" ></iframe>"""
	else:
		disp = """\
	<div class="row">
		<div class="col s12">
			<h1>Konfigurationsfehler.</h1>
		</div>
	</div>"""

	if common.getinfo("REFRESHAKTIV", "global", 0) == 1:
		refresh = "	<META HTTP-EQUIV=\"refresh\" CONTENT=\""+str(common.getinfo("REFRESH", "global", 0))+"\">"
	else:
		refresh = ""

	print "Content-Type: text/html\n"
	print """\
<!DOCTYPE html>
<html lang="de">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no"/>
	<link href="css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>"""
	print refresh
	print """\
	<title>MonitorNjus</title>
	<style>
	html, body, iframe { height: 100%; }
	</style>
</head>
<body>"""
	####     # = debug     ####
	#print timeL
	#print timeR
	#print geteilt
	print disp
	print "</body>"
	import sys
	sys.stdout.write("</html>")
	del sys

except Exception as e:
	common.debug(e)