#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 31.03.2015 (Version 0.7)

try:
	import common
	import read_values

	if int(read_values.read_refreshmonenabled) == 1:
	    refresh = "    <META HTTP-EQUIV=\"refresh\" CONTENT=\""+str(read_values.read_refreshmon)+"\" >"
	else:
	    refresh = ""

	disp = """
	<iframe src="show.py" style="position:absolute; height:100%; width:100%; right:0px; border-style:none; overflow:hidden" scrolling="no"></iframe>"""

	print "Content-Type: text/html"
	print
	print """<!DOCTYPE html>
<html lang="de">
<head>
	<title>MonitorNjus</title>
	<meta charset="utf-8">
	<link href="css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	<link href="css/mnews.css" type="text/css" rel="stylesheet" media="screen,projection"/>"""
	print refresh
	print """
</head>
<body>"""
	print disp
	if read_values.read_uhraktiv == 1:
		if read_values.read_uhrvmargin == "center":
			uhr = """
	<div id="uhr" style="height:"""+str(read_values.read_uhrheight)+""";width:"""+str(read_values.read_uhrwidth)+""";"""+read_values.read_uhrvalign+""":"""+str(read_values.read_uhralign)+""";position:absolute;left:0;right:0;margin-left:auto;margin-right:auto;">
		<embed src="""+read_values.read_uhrlink+""" quality="high" wmode="transparent" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer" menu="false" height="100%" width="100%">
	</div>"""
		elif read_values.read_uhrvmargin == "left":
			uhr = """
	<div id="uhr" style="position: fixed; height:"""+str(read_values.read_uhrheight)+""";width:"""+str(read_values.read_uhrwidth)+""";"""+read_values.read_uhrvalign+""":"""+str(read_values.read_uhralign)+""";"""+read_values.read_uhrvmargin+""":"""+str(read_values.read_uhrmargin)+""";">
		<embed src="""+read_values.read_uhrlink+""" quality="high" wmode="transparent" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer" menu="false" height="100%" width="100%">
	</div>"""
		else: 
			uhr = """
	<div id="uhr" style="height:"""+str(read_values.read_uhrheight)+""";width:"""+str(read_values.read_uhrwidth)+""";"""+read_values.read_uhrvalign+""":"""+str(read_values.read_uhralign)+""";"""+read_values.read_uhrvmargin+""":"""+str(read_values.read_uhrmargin)+""";">
		<embed src="""+read_values.read_uhrlink+""" quality="high" wmode="transparent" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer" menu="false" height="100%" width="100%">
	</div>"""
		print uhr
	if read_values.read_logoaktiv == 1:
		if read_values.read_logovmargin == "left":
			marginx = "margin-left:"+str(read_values.read_logomargin)+";"
		elif read_values.read_logovmargin == "right":
			marginx = "margin-right"+str(read_values.read_logomargin)+";"
		else:
			marginx = ""
		print """
	<div id="logo" style="""+read_values.read_logovalign+""":"""+str(read_values.read_logoalign)+""";>
		<a href="../" target="_parent"><img align="""+read_values.read_logovmargin+""" style="border:0px; """+marginx+"""" src=\""""+read_values.read_logolink+"""\" alt=""></a>
	</div>"""
	if read_values.read_adminlinkaktiv == 1:
		if read_values.read_adminlinkvmargin == "center":
			print """
		<div id="admin_link" style="position: fixed; background:none; """+read_values.read_adminlinkvalign+""":"""+str(read_values.read_adminlinkalign)+""";position:absolute;left:0;right:0;margin-left:auto;margin-right:auto;">
			<small>"""+str(common.datum)+"""</small><br>
			<a style="text-decoration: none;" href="../admin/">monitor<b>njus</b>"""+common.version+""" </a>&copy; Steffen Deusch
		</div>"""
		else:
			print """
		<div id="admin_link" style="position: fixed; width: auto; background:none; """+read_values.read_adminlinkvalign+""":"""+str(read_values.read_adminlinkalign)+"""; """+read_values.read_adminlinkvmargin+""":"""+str(read_values.read_adminlinkmargin)+""";">
			<small>"""+str(common.datum)+"""</small><br>
			<a style="text-decoration: none;" href="../admin/">monitor<b>njus</b>"""+common.version+""" </a>&copy; Steffen Deusch
		</div>"""
	elif read_values.read_adminlinkaktiv == 0:
		print ""
	else:
		print"""
	<div id="admin_link" style="background:none; bottom:0px;">
		<small>KONFIGURATIONSFEHLER</small><br>
	</div>"""

	if read_values.read_widgetaktiv == 1:
		if read_values.read_widgetvmargin == "center":
			print """
	<div id="widget" style="height:"""+str(read_values.read_widgetheight)+""";width:"""+str(read_values.read_widgetwidth)+""";"""+read_values.read_widgetvalign+""":"""+str(read_values.read_widgetalign)+""";position:absolute;left:0;right:0;margin-left:auto;margin-right:auto;">"""
			print read_values.read_widgetlink
			print "</div>"
		else:
			print """
	<div id="widget" style="height:"""+str(read_values.read_widgetheight)+""";width:"""+str(read_values.read_widgetwidth)+""";"""+read_values.read_widgetvalign+""":"""+str(read_values.read_widgetalign)+""";"""+read_values.read_widgetvmargin+""":"""+str(read_values.read_widgetmargin)+""";">"""
		print read_values.read_widgetlink
		print "</div>"
	print """</body>
</html>"""

except Exception, e:
	print "Content-Type: text/html"
	print
	print """<!DOCTYPE html>
<html lang="de">
<head>
	<meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no" />
    <link href="css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection" />
    <link href="css/mnews.css" type="text/css" rel="stylesheet" media="screen,projection" />
    <META HTTP-EQUIV="refresh" CONTENT="10" />
</head>
<body>
	<h1>Es ist ein Fehler aufgetreten (index.py)! Seite wird in 10 Sekunden neu geladen.</h1>
	<h3>Details:<br>"""
	print e
	print """
	</h3>
</body>
</html>"""