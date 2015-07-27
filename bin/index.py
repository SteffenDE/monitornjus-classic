#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 22.07.2015 (Version 0.8.4)

import os
import imp
workingdir = os.path.dirname(os.path.realpath(__file__))
common = imp.load_source('common', workingdir+"/../common.py")

def widgets():
	count = common.getwidgets()
	out = ""
	for item in count:
		typ = common.getwidgTYPfromID(item)
		# if typ == "Flash_Uhr" and common.getwidgetinfo("Flash_Uhr", item, "AKTIV"):
		# 	uhrheight = common.addpx(common.getwidgetinfo("Flash_Uhr", item, "height"))
		# 	uhrwidth = common.addpx(common.getwidgetinfo("Flash_Uhr", item, "width"))
		# 	uhrvalign = common.getwidgetinfo("Flash_Uhr", item, "valign")
		# 	uhralign = common.addpx(common.getwidgetinfo("Flash_Uhr", item, "align"))
		# 	uhrlink = common.getwidgetinfo("Flash_Uhr", item, "URL")
		# 	uhrvmargin = common.getwidgetinfo("Flash_Uhr", item, "vmargin")
		# 	uhrmargin = common.addpx(common.getwidgetinfo("Flash_Uhr", item, "margin"))

		# 	if uhrvmargin == "center":
		# 		uhr = """\
		# <div id="uhr" style="height:"""+uhrheight+""";width:"""+uhrwidth+""";"""+uhrvalign+""":"""+uhralign+"""; left:0; right:0;">
		# 	<embed src="""+uhrlink+""" quality="high" wmode="transparent" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer" menu="false" height="100%" width="100%">
		# </div>"""
		# 	elif uhrvmargin == "left":
		# 		uhr = """\
		# <div id="uhr" style="position: fixed; height:"""+uhrheight+""";width:"""+uhrwidth+""";"""+uhrvalign+""":"""+uhralign+""";"""+uhrvmargin+""":"""+uhrmargin+""";">
		# 	<embed src="""+uhrlink+""" quality="high" wmode="transparent" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer" menu="false" height="100%" width="100%">
		# </div>"""
		# 	else: 
		# 		uhr = """\
		# <div id="uhr" style="height:"""+uhrheight+""";width:"""+uhrwidth+""";"""+uhrvalign+""":"""+uhralign+""";"""+uhrvmargin+""":"""+uhrmargin+""";">
		# 	<embed src="""+uhrlink+""" quality="high" wmode="transparent" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer" menu="false" height="100%" width="100%">
		# </div>"""
		# 	out += uhr
		if typ == "Logo" and common.getwidgetinfo("Logo", item, "AKTIV"):
			logovmargin = common.getwidgetinfo("Logo", item, "vmargin")
			logomargin = common.addpx(common.getwidgetinfo("Logo", item, "margin"))
			logovalign = common.getwidgetinfo("Logo", item, "valign")
			logoalign = common.addpx(common.getwidgetinfo("Logo", item, "align"))
			logolink = common.getwidgetinfo("Logo", item, "URL")
			logowidth = common.addpx(common.getwidgetinfo("Logo", item, "width"))
			logoheight = common.addpx(common.getwidgetinfo("Logo", item, "height"))

			if logovmargin == "left":
				marginx = "margin-left:"+logomargin+";"
			elif logovmargin == "right":
				marginx = "margin-right"+logomargin+";"
			else:
				marginx = ""
			out += """\
		<div id="logo" style="""+logovalign+""":"""+logoalign+""";>
			<img align="""+logovmargin+""" style=\""""+marginx+""" width="""+logowidth+"""; height="""+logoheight+"""\" src=\""""+logolink+"""\">
		</div>"""

		elif typ == "Freies_Widget" and common.getwidgetinfo("Freies_Widget", item, "AKTIV"):
			widgetcontent = common.getwidgetinfo("Freies_Widget", item, "URL")
			widgetheight = common.addpx(common.getwidgetinfo("Freies_Widget", item, "height"))
			widgetwidth = common.addpx(common.getwidgetinfo("Freies_Widget", item, "width"))
			widgetvalign = common.getwidgetinfo("Freies_Widget", item, "valign")
			widgetalign = common.addpx(common.getwidgetinfo("Freies_Widget", item, "align"))
			widgetvmargin = common.getwidgetinfo("Freies_Widget", item, "vmargin")
			widgetmargin = common.addpx(common.getwidgetinfo("Freies_Widget", item, "margin"))

			if widgetvmargin == "center":
				out += """	<div id="widget" style="z-index: -10; height:"""+widgetheight+"""; width:"""+widgetwidth+"""; """+widgetvalign+""":"""+widgetalign+"""; position:absolute; left:0; right:0; margin-left:auto; margin-right:auto;">"""
				out += "	"+widgetcontent
				out += "</div>"
			else:
				out += """	<div id="widget" style="z-index: -10; height:"""+widgetheight+"""; width:"""+widgetwidth+"""; """+widgetvalign+""":"""+widgetalign+"""; """+widgetvmargin+""":"""+widgetmargin+""";">"""
				out += "	"+widgetcontent
				out += "	</div>"

		elif typ == "Adminlink" and common.getwidgetinfo("Adminlink", item, "AKTIV"):
			adminlinkvmargin = common.getwidgetinfo("Adminlink", item, "vmargin")
			adminlinkmargin = common.addpx(common.getwidgetinfo("Adminlink", item, "margin"))
			adminlinkvalign = common.getwidgetinfo("Adminlink", item, "valign")
			adminlinkalign = common.addpx(common.getwidgetinfo("Adminlink", item, "align"))

			if adminlinkvmargin == "center":
				adml = """\
		<div id="admin_link" style="z-index: 100; position: fixed; background:none; """+adminlinkvalign+""":"""+adminlinkalign+""";">"""
				if adminlinkvalign == "top":
					adml += """\
				<a style="text-decoration: none;" href="../admin/">monitor<b>njus</b>"""+common.version+""" </a>&copy; Steffen Deusch<br>
				<small>"""+common.datum.strftime("%d.%m.%Y %H:%M:%S")+"""</small>"""
				else:
					adml += """\
				<small>"""+common.datum.strftime("%d.%m.%Y %H:%M:%S")+"""</small><br>
				<a style="text-decoration: none;" href="../admin/">monitor<b>njus</b>"""+common.version+""" </a>&copy; Steffen Deusch
		</div>"""
			else:
				adml = """\
		<div id="admin_link" style="z-index: 100; position: fixed; width: auto; background:none; """+adminlinkvalign+""":"""+adminlinkalign+"""; """+adminlinkvmargin+""":"""+adminlinkmargin+""";">"""
				if adminlinkvalign == "top":
					adml += """\
			<a style="text-decoration: none;" href="../admin/">monitor<b>njus</b>"""+common.version+""" </a>&copy; Steffen Deusch<br>
			<small style=float:"""+adminlinkvmargin+""";>"""+common.datum.strftime("%d.%m.%Y %H:%M:%S")+"""</small>"""
				else:
					adml += """\
			<small style=float:"""+adminlinkvmargin+""";>"""+common.datum.strftime("%d.%m.%Y %H:%M:%S")+"""</small><br>
			<a style="text-decoration: none;" href="../admin/">monitor<b>njus</b>"""+common.version+""" </a>&copy; Steffen Deusch
		</div>"""
			out += adml

	return out


try:
	if int(common.getinfo("REFRESHAKTIV", "globalmon", 0)) == 1:
		refresh = "	<META HTTP-EQUIV=\"refresh\" CONTENT=\""+unicode(common.getinfo("REFRESH", "globalmon", 0))+"\" >"
	else:
		refresh = ""

	print "Content-Type: text/html\n"
	print """\
<!DOCTYPE html>
<html style="overflow: hidden;" lang="de">
<head>
	<title>MonitorNjus</title>
	<meta charset="UTF-8">
	<link href="css/mnews.css" type="text/css" rel="stylesheet" media="screen,projection"/>"""
	print refresh
	print """\
</head>
<body>
	<iframe src="show.py" style="z-index: -1000; position:absolute; height:100%; width:100%; top: 0px; right:0px; border-style:none; overflow:hidden" scrolling="no"></iframe>"""

	print widgets()

	print "</body>"
	import sys
	sys.stdout.write("</html>")
	del sys

except Exception as e:
	common.debug(e)