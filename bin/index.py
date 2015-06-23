#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 22.06.2015 (Version 0.7.6)

import os
import imp
workingdir = os.getcwd()
if "bin" in workingdir:
	common = imp.load_source('common', workingdir+"/../common.py")
else:
	common = imp.load_source('common', workingdir+"/common.py")

try:
	if int(common.getinfo("REFRESHAKTIV", "globalmon", 0)) == 1:
		refresh = "	<META HTTP-EQUIV=\"refresh\" CONTENT=\""+str(common.getinfo("REFRESH", "globalmon", 0))+"\" >"
	else:
		refresh = ""

	uhraktiv = common.getwidgetinfo("Uhr", "AKTIV")
	logoaktiv = common.getwidgetinfo("Logo", "AKTIV")
	widgetaktiv = common.getwidgetinfo("Freies-Widget", "AKTIV")
	adminlinkaktiv = common.getwidgetinfo("Admin-Link", "AKTIV")

	print "Content-Type: text/html"
	print
	print """<!DOCTYPE html>
<html style="overflow: hidden;" lang="de">
<head>
	<title>MonitorNjus</title>
	<meta charset="utf-8">
	<link href="css/mnews.css" type="text/css" rel="stylesheet" media="screen,projection"/>"""
	print refresh
	print """\
</head>
<body>
	<iframe src="show.py" style="position:absolute; height:100%; width:100%; top: 0px; right:0px; border-style:none; overflow:hidden" scrolling="no"></iframe>"""

	##########################

	if uhraktiv:
		uhrheight = common.addpx(common.getwidgetinfo("Uhr", "height"))
		uhrwidth = common.addpx(common.getwidgetinfo("Uhr", "width"))
		uhrvalign = common.getwidgetinfo("Uhr", "vmargin")
		uhralign = common.addpx(common.getwidgetinfo("Uhr", "valign"))
		uhrlink = common.getwidgetinfo("Uhr", "URL")
		uhrvmargin = common.getwidgetinfo("Uhr", "vmargin")
		uhrmargin = common.addpx(common.getwidgetinfo("Uhr", "margin"))

		if uhrvmargin == "center":
			uhr = """\
	<div id="uhr" style="height:"""+uhrheight+""";width:"""+uhrwidth+""";"""+uhrvalign+""":"""+uhralign+"""; left:0; right:0;">
		<embed src="""+uhrlink+""" quality="high" wmode="transparent" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer" menu="false" height="100%" width="100%">
	</div>"""
		elif uhrvmargin == "left":
			uhr = """\
	<div id="uhr" style="position: fixed; height:"""+uhrheight+""";width:"""+uhrwidth+""";"""+uhrvalign+""":"""+uhralign+""";"""+uhrvmargin+""":"""+uhrmargin+""";">
		<embed src="""+uhrlink+""" quality="high" wmode="transparent" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer" menu="false" height="100%" width="100%">
	</div>"""
		else: 
			uhr = """\
	<div id="uhr" style="height:"""+uhrheight+""";width:"""+uhrwidth+""";"""+uhrvalign+""":"""+uhralign+""";"""+uhrvmargin+""":"""+uhrmargin+""";">
		<embed src="""+uhrlink+""" quality="high" wmode="transparent" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer" menu="false" height="100%" width="100%">
	</div>"""
		print uhr

	##########################

	if logoaktiv:
		logovmargin = common.getwidgetinfo("Logo", "vmargin")
		logomargin = common.addpx(common.getwidgetinfo("Logo", "margin"))
		logovalign = common.getwidgetinfo("Logo", "valign")
		logoalign = common.addpx(common.getwidgetinfo("Logo", "align"))
		logolink = common.getwidgetinfo("Logo", "URL")
		logowidth = common.addpx(common.getwidgetinfo("Logo", "width"))
		logoheight = common.addpx(common.getwidgetinfo("Logo", "height"))

		if logovmargin == "left":
			marginx = "margin-left:"+logomargin+";"
		elif logovmargin == "right":
			marginx = "margin-right"+logomargin+";"
		else:
			marginx = ""
		print """\
	<div id="logo" style="""+logovalign+""":"""+logoalign+""";>
		<img align="""+logovmargin+""" style=\""""+marginx+""" width="""+logowidth+"""; height="""+logoheight+"""\" src=\""""+logolink+"""\">
	</div>"""

	##########################

	if widgetaktiv:
		widgetcontent = common.getwidgetinfo("Freies-Widget", "URL")
		widgetheight = common.addpx(common.getwidgetinfo("Freies-Widget", "height"))
		widgetwidth = common.addpx(common.getwidgetinfo("Freies-Widget", "width"))
		widgetvalign = common.getwidgetinfo("Freies-Widget", "valign")
		widgetalign = common.addpx(common.getwidgetinfo("Freies-Widget", "align"))
		widgetvmargin = common.getwidgetinfo("Freies-Widget", "vmargin")
		widgetmargin = common.addpx(common.getwidgetinfo("Freies-Widget", "margin"))

		if widgetvmargin == "center":
			print """	<div id="widget" style="height:"""+widgetheight+"""; width:"""+widgetwidth+"""; """+widgetvalign+""":"""+widgetalign+"""; position:absolute; left:0; right:0; margin-left:auto; margin-right:auto;">"""
			print "	"+widgetcontent
			print "</div>"
		else:
			print """	<div id="widget" style="height:"""+widgetheight+"""; width:"""+widgetwidth+"""; """+widgetvalign+""":"""+widgetalign+"""; """+widgetvmargin+""":"""+widgetmargin+""";">"""
			print "	"+widgetcontent
			print "	</div>"

	##########################

	if adminlinkaktiv:
		adminlinkvmargin = common.getwidgetinfo("Admin-Link", "vmargin")
		adminlinkmargin = common.addpx(common.getwidgetinfo("Admin-Link", "margin"))
		adminlinkvalign = common.getwidgetinfo("Admin-Link", "valign")
		adminlinkalign = common.addpx(common.getwidgetinfo("Admin-Link", "align"))

		if adminlinkvmargin == "center":
			print """\
	<div id="admin_link" style="position: fixed; background:none; """+adminlinkvalign+""":"""+adminlinkalign+""";">
		<small>"""+common.datum.strftime("%d.%m.%Y %H:%M:%S")+"""</small><br>
		<a style="text-decoration: none;" href="../admin/">monitor<b>njus</b>"""+common.version+""" </a>&copy; Steffen Deusch
	</div>"""
		else:
			print """\
	<div id="admin_link" style="position: fixed; width: auto; background:none; """+adminlinkvalign+""":"""+adminlinkalign+"""; """+adminlinkvmargin+""":"""+adminlinkmargin+""";">
		<small>"""+common.datum.strftime("%d.%m.%Y %H:%M:%S")+"""</small><br>
		<a style="text-decoration: none;" href="../admin/">monitor<b>njus</b>"""+common.version+""" </a>&copy; Steffen Deusch
	</div>"""
	else:
		print """\
	<div id="admin_link" style="background:none; bottom:0px;">
		<small>KONFIGURATIONSFEHLER</small><br>
	</div>"""

	##########################

	print """\
</body>
</html>"""

except Exception as e:
	common.debug(e)