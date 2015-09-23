#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 14.09.2015 (Version 0.9.3)

import os
workingdir = os.path.dirname(os.path.realpath(__file__))
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import imp
modulesdir = workingdir+"/../modules"
common = imp.load_source("common", modulesdir+"/common.py")
checktime = imp.load_source("checktime", modulesdir+"/checktime.py")

try:
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
		disp = u"""
<frameset frameborder="0" rows="*,0">
	<frameset frameborder="0" cols="""+str(teilung)+""","""+str(100-teilung)+""">
		<frame scrolling="no" src="contentset.py?seite=1" name="links" />
		<frame scrolling="no" src="contentset.py?seite=2" name="rechts" />
	</frameset> 
</frameset>"""
	elif (linksgeteilt and not rechtsgeteilt and timeL) or (linksgeteilt and rechtsgeteilt and timeL and not timeR):
		disp = u"""
<frameset frameborder="0" rows="*,0">
	<frame scrolling="no" src="contentset.py?seite=1" name="links" />
</frameset>"""
	elif (rechtsgeteilt and not linksgeteilt and timeR) or (rechtsgeteilt and linksgeteilt and timeR and not timeL):
		disp = u"""
<frameset frameborder="0" rows="*,0">
	<frame scrolling="no" src="contentset.py?seite=2" name="rechts" />
</frameset>"""
	else:
		raise Warning("Keine Seite aktiv")

	if common.getinfo("REFRESHAKTIV", "global", 0) == 1:
		refresh = u"	<meta http-equiv=\"refresh\" content=\""+unicode(common.getinfo("REFRESH", "global", 0))+"\">"
	else:
		refresh = u""

	out = u"Content-Type: text/html;charset=utf-8\n"
	out += u"""
<!DOCTYPE html>
<html lang="de">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no"/>
	<link href="css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>"""
	out += unicode(refresh)
	out += u"""
	<title>MonitorNjus</title>
	<!-- MonitorNjus -->
	<!-- Copyright (c) """+unicode(common.datum.year)+""" Steffen Deusch -->
	<!-- https://github.com/SteffenDE/MonitorNjus -->
</head>"""
	####     # = debug     ####
	# out += timeL
	# out += timeR
	# out += geteilt
	out += unicode(disp)
	out += """
</html>"""
	
	########### Ausgabe ###########
	print(unicode(out))

except Exception as e:
	common.debug(e)