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

def widgets():
	count = common.getwidgets()
	out = ""
	for item in count:
		typ = common.getwidgTYPfromID(item)
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
		<img align="""+logovmargin+""" style=\""""+marginx+""";\" width="""+logowidth+""" height="""+logoheight+""" src=\""""+logolink+"""\">
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
				out += """	<div id="widget" style="z-index: -10; height:"""+widgetheight+"""; width:"""+widgetwidth+"""; """+widgetvalign+""":"""+widgetalign+"""; position:absolute; left:0; right:0; margin-left:auto; margin-right:auto;">\n"""
				out += "		"+widgetcontent+"\n"
				out += "	</div>\n"
			else:
				out += """	<div id="widget" style="z-index: -10; height:"""+widgetheight+"""; width:"""+widgetwidth+"""; """+widgetvalign+""":"""+widgetalign+"""; """+widgetvmargin+""":"""+widgetmargin+""";">\n"""
				out += "		"+widgetcontent+"\n"
				out += "	</div>\n"

		elif typ == "Adminlink" and common.getwidgetinfo("Adminlink", item, "AKTIV"):
			adminlinkvmargin = common.getwidgetinfo("Adminlink", item, "vmargin")
			adminlinkmargin = common.addpx(common.getwidgetinfo("Adminlink", item, "margin"))
			adminlinkvalign = common.getwidgetinfo("Adminlink", item, "valign")
			adminlinkalign = common.addpx(common.getwidgetinfo("Adminlink", item, "align"))

			if adminlinkvmargin == "center":
				adml = """\
	<div id="admin_link" style="z-index: 100; position: fixed; background:none; """+adminlinkvalign+""":"""+adminlinkalign+""";">\n"""
				if adminlinkvalign == "top":
					adml += """\
		<a style="text-decoration: none;" href="../admin/">monitor<b>njus</b>"""+common.version+""" </a>&copy; Steffen Deusch<br>
		<small>"""+common.datum.strftime("%d.%m.%Y %H:%M:%S")+"""</small>"""
				else:
					adml += """\
		<small>"""+common.datum.strftime("%d.%m.%Y %H:%M:%S")+"""</small><br>
		<a style="text-decoration: none;" href="../admin/">monitor<b>njus</b>"""+common.version+""" </a>&copy; Steffen Deusch
	</div>\n"""
			else:
				adml = """\
	<div id="admin_link" style="z-index: 100; position: fixed; width: auto; background:none; """+adminlinkvalign+""":"""+adminlinkalign+"""; """+adminlinkvmargin+""":"""+adminlinkmargin+""";">\n"""
				if adminlinkvalign == "top":
					adml += """\
		<a style="text-decoration: none;" href="../admin/">monitor<b>njus</b>"""+common.version+""" </a>&copy; Steffen Deusch<br>
		<small style=float:"""+adminlinkvmargin+""";>"""+common.datum.strftime("%d.%m.%Y %H:%M:%S")+"""</small>"""
				else:
					adml += """\
		<small style=float:"""+adminlinkvmargin+""";>"""+common.datum.strftime("%d.%m.%Y %H:%M:%S")+"""</small><br>
		<a style="text-decoration: none;" href="../admin/">monitor<b>njus</b>"""+common.version+""" </a>&copy; Steffen Deusch
	</div>\n"""
			out += adml

	return out


try:
	if int(common.getinfo("REFRESHAKTIV", "globalmon", 0)) == 1:
		refresh = "	<meta http-equiv=\"refresh\" content=\""+unicode(common.getinfo("REFRESH", "globalmon", 0))+"\">\n"
	else:
		refresh = ""

	out = u"Content-Type: text/html;charset=utf-8\n"
	out += u"""
<!DOCTYPE html>
<html style="overflow: hidden;" lang="de">
<head>
	<meta charset="UTF-8">
	<link href="css/mnews.css" type="text/css" rel="stylesheet" media="screen,projection"/>"""
	out += unicode(refresh)
	out += u"""
	<title>MonitorNjus</title>
	<!-- MonitorNjus -->
	<!-- Copyright (c) """+unicode(common.datum.year)+""" Steffen Deusch -->
	<!-- https://github.com/SteffenDE/MonitorNjus -->
</head>
<body>
	<iframe src="show.py" style="z-index: -1000; position:absolute; height:100%; width:100%; top: 0px; right:0px; border-style:none; overflow:hidden" scrolling="no"></iframe>"""
	out += unicode(widgets())
	if common.triggerrefresh:
		out += u"""
	<script>
	setTimeout(function() {
		if(typeof(EventSource) !== "undefined") {
			var source = new EventSource("triggerrefresh.py");
			source.onmessage = function(event) {
				if (event.data == "reload") {
					var meta = document.createElement('meta');
					meta.httpEquiv = "refresh";
					meta.content = "2";
					document.getElementsByTagName('head')[0].appendChild(meta);
				}
			};
		}
	}, 3000);
	</script>"""

	out += u"""
</body>
</html>"""
	
	########### Ausgabe ###########
	print(unicode(out))

except Exception as e:
	common.debug(e)