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
	import read_values

	if int(read_values.read_refreshmonenabled) == 1:
		refresh = "	<META HTTP-EQUIV=\"refresh\" CONTENT=\""+str(read_values.read_refreshmon)+"\" >"
	else:
		refresh = ""

	uhraktiv = read_values.read_uhraktiv
	logoaktiv = read_values.read_logoaktiv
	widgetaktiv = read_values.read_widgetaktiv
	adminlinkaktiv = read_values.read_adminlinkaktiv

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
	<iframe src="show.py" style="position:absolute; height:100%; width:100%; right:0px; border-style:none; overflow:hidden" scrolling="no"></iframe>"""

	##########################

	if uhraktiv:
		uhrheight = common.addpx(read_values.read_uhrheight)
		uhrwidth = common.addpx(read_values.read_uhrwidth)
		uhrvalign = read_values.read_uhrvalign
		uhralign = common.addpx(read_values.read_uhralign)
		uhrlink = read_values.read_uhrlink
		uhrvmargin = read_values.read_uhrvmargin
		uhrmargin = common.addpx(read_values.read_uhrmargin)

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
		logovmargin = read_values.read_logovmargin
		logomargin = common.addpx(read_values.read_logomargin)
		logovalign = read_values.read_logovalign
		logoalign = common.addpx(read_values.read_logoalign)
		logolink = read_values.read_logolink

		if logovmargin == "left":
			marginx = "margin-left:"+logomargin+";"
		elif logovmargin == "right":
			marginx = "margin-right"+logomargin+";"
		else:
			marginx = ""
		print """\
	<div id="logo" style="""+logovalign+""":"""+logoalign+""";>
		<a href="../" target="_parent"><img align="""+logovmargin+""" style=\""""+marginx+"""\" src=\""""+logolink+"""\" alt=""></a>
	</div>"""

	##########################

	if widgetaktiv:
		widgetcontent = read_values.read_widgetlink
		widgetheight = common.addpx(read_values.read_widgetheight)
		widgetwidth = common.addpx(read_values.read_widgetwidth)
		widgetvalign = read_values.read_widgetvalign
		widgetalign = common.addpx(read_values.read_widgetalign)
		widgetvmargin = read_values.read_widgetvmargin
		widgetmargin = common.addpx(read_values.read_widgetmargin)

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
		adminlinkvmargin = read_values.read_adminlinkvmargin
		adminlinkmargin = common.addpx(read_values.read_adminlinkmargin)
		adminlinkvalign = read_values.read_adminlinkvalign
		adminlinkalign = common.addpx(read_values.read_adminlinkalign)

		if adminlinkvmargin == "center":
			print """\
	<div id="admin_link" style="position: fixed; background:none; """+adminlinkvalign+""":"""+adminlinkalign+""";">
		<small>"""+str(common.datum)+"""</small><br>
		<a style="text-decoration: none;" href="../admin/">monitor<b>njus</b>"""+common.version+""" </a>&copy; Steffen Deusch
	</div>"""
		else:
			print """\
	<div id="admin_link" style="position: fixed; width: auto; background:none; """+adminlinkvalign+""":"""+adminlinkalign+"""; """+adminlinkvmargin+""":"""+adminlinkmargin+""";">
		<small>"""+str(common.datum)+"""</small><br>
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