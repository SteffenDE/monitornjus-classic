#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 05.08.2015 (Version 0.9.1)

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import imp
import cgi
workingdir = os.path.dirname(os.path.realpath(__file__))
common = imp.load_source('common', workingdir+"/../common.py")

try:
	import colors
	import firstrun

	if common.authentication:
		auth = imp.load_source("auth", workingdir+"/../auth.py")
		auth.me()

	rows = int(common.getrows())
	rowsone = rows + 1

	def displaysets():
		x = 1
		while x <= rows:
			if unicode(x) in common.getallrows():
				print u"""\
					<div class="col s12">
						<h5 class="header center """+colors.color+"""-text">Displayset """+unicode(x)+"""</h5>
						<div class="row">
							<div class="col s6">
								<div class="card white darken-1">
									<div class="card-content white-text">
										<span class="card-title """+colors.color+"""-text text-darken-2">Linke Seite</span><br>
										<div class="row">
											<div class="input-field col s6">
												<input value=\""""+cgi.escape(unicode(common.testexist("URL", "Links", x)))+"""\" name="URL-Links-"""+unicode(x)+"""\" id="URL-Links-"""+unicode(x)+"""\" type="text">
												<label for="URL-Links-"""+unicode(x)+"""\">URL Links</label>
											</div>
											<div class="input-field col s6">
												<input value=\""""+cgi.escape(unicode(common.testexist("REFRESH", "Links", x)))+"""\" name="REFRESH-Links-"""+unicode(x)+"""\" id="REFRESH-Links-"""+unicode(x)+"""\" type="number">
												<label for="REFRESH-Links-"""+unicode(x)+"""\">Refresh Links</label>
											</div>
										</div>
										<div>
											<input type="checkbox" name="AKTIV-Links-"""+unicode(x)+"""\" id="AKTIV-Links-"""+unicode(x)+"""\" """+common.aktiv("AKTIV", "Links", x)+"""/>
											<label for="AKTIV-Links-"""+unicode(x)+"""\">Links aktiviert</label>&nbsp;&nbsp;&nbsp;&nbsp;
											<input type="hidden" value="0" name="HIDDEN.AKTIV-Links-"""+unicode(x)+"""\">
											<input type="checkbox" name="REFRESHAKTIV-Links-"""+unicode(x)+"""\" id="REFRESHAKTIV-Links-"""+unicode(x)+"""\" """+common.aktiv("REFRESHAKTIV", "Links", x)+"""/>
											<label for="REFRESHAKTIV-Links-"""+unicode(x)+"""\">Links neu laden</label>
											<input type="hidden" value="0" name="HIDDEN.REFRESHAKTIV-Links-"""+unicode(x)+"""\">
										</div>
										<div class="row">
											<div class="input-field col s4">
												<input value=\""""+cgi.escape(unicode(common.getdate("uhrzeit", "Links", x)))+"""\" name="uhrzeit-Links-"""+unicode(x)+"""\" id="uhrzeit-Links-"""+unicode(x)+"""\" type="text">
												<label for="uhrzeit-Links-"""+unicode(x)+"""\">Uhrzeit</label>
											</div>
											<div class="input-field col s4">
												<input value=\""""+cgi.escape(unicode(common.getdate("wochentag", "Links", x)))+"""\" name="wochentag-Links-"""+unicode(x)+"""\" id="wochentag-Links-"""+unicode(x)+"""\" type="text">
												<label for="wochentag-Links-"""+unicode(x)+"""\">Wochentag</label>
											</div>
											<div class="input-field col s2">
												<input value=\""""+cgi.escape(unicode(common.getdate("tag", "Links", x)))+"""\" name="tag-Links-"""+unicode(x)+"""\" id="tag-Links-"""+unicode(x)+"""\" type="text">
												<label for="tag-Links-"""+unicode(x)+"""\">Tag</label>
											</div>
											<div class="input-field col s2">
												<input value=\""""+cgi.escape(unicode(common.getdate("monat", "Links", x)))+"""\" name="monat-Links-"""+unicode(x)+"""\" id="monat-Links-"""+unicode(x)+"""\" type="text">
												<label for="monat-Links-"""+unicode(x)+"""\">Monat</label>
											</div>
										</div>
										<div class="row">
											<div class="input-field col s3">
												<input value=\""""+cgi.escape(unicode(common.getinfo("MARGINLEFT","Links",x)))+"""\" name="MARGINLEFT-Links-"""+unicode(x)+"""\" id="MARGINLEFT-Links-"""+unicode(x)+"""\" type="text">
												<label for="MARGINLEFT-Links-"""+unicode(x)+"""\">Rand-Links</label>
											</div>
											<div class="input-field col s3">
												<input value=\""""+cgi.escape(unicode(common.getinfo("MARGINRIGHT","Links",x)))+"""\" name="MARGINRIGHT-Links-"""+unicode(x)+"""\" id="MARGINRIGHT-Links-"""+unicode(x)+"""\" type="text">
												<label for="MARGINRIGHT-Links-"""+unicode(x)+"""\">Rand-Rechts</label>
											</div>
											<div class="input-field col s3">
												<input value=\""""+cgi.escape(unicode(common.getinfo("MARGINTOP","Links",x)))+"""\" name="MARGINTOP-Links-"""+unicode(x)+"""\" id="MARGINTOP-Links-"""+unicode(x)+"""\" type="text">
												<label for="MARGINTOP-Links-"""+unicode(x)+"""\">Rand-Oben</label>
											</div>
											<div class="input-field col s3">
												<input value=\""""+cgi.escape(unicode(common.getinfo("MARGINBOTTOM","Links",x)))+"""\" name="MARGINBOTTOM-Links-"""+unicode(x)+"""\" id="MARGINBOTTOM-Links-"""+unicode(x)+"""\" type="text">
												<label for="MARGINBOTTOM-Links-"""+unicode(x)+"""\">Rand-Unten</label>
											</div>
										</div>
									</div>
								</div>
							</div>
							<div class="col s6">
								<div class="card white darken-1">
									<div class="card-content white-text">
										<span class="card-title """+colors.color+"""-text text-darken-2">Rechte Seite</span><br>
										<div class="row">
											<div class="input-field col s6">
												<input value=\""""+cgi.escape(unicode(common.testexist("URL", "Rechts", x)))+"""\" name="URL-Rechts-"""+unicode(x)+"""\" id="URL-Rechts-"""+unicode(x)+"""\" type="text">
												<label for="URL-Rechts-"""+unicode(x)+"""\">URL Rechts</label>
											</div>
											<div class="input-field col s6">
												<input value=\""""+cgi.escape(unicode(common.testexist("REFRESH", "Rechts", x)))+"""\" name="REFRESH-Rechts-"""+unicode(x)+"""\" id="REFRESH-Rechts-"""+unicode(x)+"""\" type="number">
												<label for="REFRESH-Rechts-"""+unicode(x)+"""\">Refresh Rechts</label>
											</div>
										</div>
										<div>
											<input type="checkbox" name="AKTIV-Rechts-"""+unicode(x)+"""\" id="AKTIV-Rechts-"""+unicode(x)+"""\" """+common.aktiv("AKTIV", "Rechts", x)+"""/>
											<label for="AKTIV-Rechts-"""+unicode(x)+"""\">Rechts aktiviert</label>&nbsp;&nbsp;&nbsp;&nbsp;
											<input type="hidden" value="0" name="HIDDEN.AKTIV-Rechts-"""+unicode(x)+"""\">
											<input type="checkbox" name="REFRESHAKTIV-Rechts-"""+unicode(x)+"""\" id="REFRESHAKTIV-Rechts-"""+unicode(x)+"""\" """+common.aktiv("REFRESHAKTIV", "Rechts", x)+"""/>
											<label for="REFRESHAKTIV-Rechts-"""+unicode(x)+"""\">Rechts neu laden</label>
											<input type="hidden" value="0" name="HIDDEN.REFRESHAKTIV-Rechts-"""+unicode(x)+"""\">
										</div>
										<div class="row">
											<div class="input-field col s4">
												<input value=\""""+cgi.escape(unicode(common.getdate("uhrzeit", "Rechts", x)))+"""\" name="uhrzeit-Rechts-"""+unicode(x)+"""\" id="uhrzeit-Rechts-"""+unicode(x)+"""\" type="text">
												<label for="uhrzeit-Rechts-"""+unicode(x)+"""\">Uhrzeit</label>
											</div>
											<div class="input-field col s4">
												<input value=\""""+cgi.escape(unicode(common.getdate("wochentag", "Rechts", x)))+"""\" name="wochentag-Rechts-"""+unicode(x)+"""\" id="wochentag-Rechts-"""+unicode(x)+"""\" type="text">
												<label for="wochentag-Rechts-"""+unicode(x)+"""\">Wochentag</label>
											</div>
											<div class="input-field col s2">
												<input value=\""""+cgi.escape(unicode(common.getdate("tag", "Rechts", x)))+"""\" name="tag-Rechts-"""+unicode(x)+"""\" id="tag-Rechts-"""+unicode(x)+"""\" type="text">
												<label for="tag-Rechts-"""+unicode(x)+"""\">Tag</label>
											</div>
											<div class="input-field col s2">
												<input value=\""""+cgi.escape(unicode(common.getdate("monat", "Rechts", x)))+"""\" name="monat-Rechts-"""+unicode(x)+"""\" id="monat-Rechts-"""+unicode(x)+"""\" type="text">
												<label for="monat-Rechts-"""+unicode(x)+"""\">Monat</label>
											</div>
										</div>
										<div class="row">
											<div class="input-field col s3">
												<input value=\""""+cgi.escape(unicode(common.getinfo("MARGINLEFT","Rechts",x)))+"""\" name="MARGINLEFT-Rechts-"""+unicode(x)+"""\" id="MARGINLEFT-Rechts-"""+unicode(x)+"""\" type="text">
												<label for="MARGINLEFT-Rechts-"""+unicode(x)+"""\">Rand-Links</label>
											</div>
											<div class="input-field col s3">
												<input value=\""""+cgi.escape(unicode(common.getinfo("MARGINRIGHT","Rechts",x)))+"""\" name="MARGINRIGHT-Rechts-"""+unicode(x)+"""\" id="MARGINRIGHT-Rechts-"""+unicode(x)+"""\" type="text">
												<label for="MARGINRIGHT-Rechts-"""+unicode(x)+"""\">Rand-Rechts</label>
											</div>
											<div class="input-field col s3">
												<input value=\""""+cgi.escape(unicode(common.getinfo("MARGINTOP","Rechts",x)))+"""\" name="MARGINTOP-Rechts-"""+unicode(x)+"""\" id="MARGINTOP-Rechts-"""+unicode(x)+"""\" type="text">
												<label for="MARGINTOP-Rechts-"""+unicode(x)+"""\">Rand-Oben</label>
											</div>
											<div class="input-field col s3">
												<input value=\""""+cgi.escape(unicode(common.getinfo("MARGINBOTTOM","Rechts",x)))+"""\" name="MARGINBOTTOM-Rechts-"""+unicode(x)+"""\" id="MARGINBOTTOM-Rechts-"""+unicode(x)+"""\" type="text">
												<label for="MARGINBOTTOM-Rechts-"""+unicode(x)+"""\">Rand-Unten</label>
											</div>
										</div>
									</div>
								</div>
							</div>"""
				if rows != 1:
					print u"""<center><a class="waves-effect waves-light btn" href="setn.py?referer=row&delnum="""+unicode(x)+"""\">Displayset l&ouml;schen</a></center>"""
				print u"""\
						</div>
					</div>"""
			x = x + 1

	print u"Content-Type: text/html\n"
	print u"""\
<!DOCTYPE html>
<html lang="de">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no"/>
	<link href="../bin/css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	<title>MonitorNjus Admin-Panel</title>"""
	print unicode(colors.adminstyles)
	print u"""\
</head>
<body>
	<script type="text/javascript" src="../bin/js/jquery-2.1.4.min.js"></script>
	<script type="text/javascript" src="../bin/js/materialize.min.js"></script>
	<nav class=\""""+colors.color+"""\"="navigation">
		<div class="container">
			<div class="nav-wrapper">
				<a id="logo-container" href="#" class="brand-logo">MonitorNjus Admin Panel</a>
				<a href="#" data-activates="mobile" class="button-collapse"><i class="mdi-navigation-menu"></i></a>
				<ul id="nav-mobile" class="right hide-on-med-and-down">
					<li><a href="widgets.py">Widgets</a></li>
					<li><a href="../bin/">Zum Frontend</a></li>
				</ul>
				<ul class="side-nav" id="mobile">
					<li><a href="widgets.py">Widgets</a></li>
					<li><a href="../bin/">Zum Frontend</a></li>
				</ul>
			</div>
		</div>
	</nav>
	<h3 class="header center """+colors.color+"""-text">Haupteinstellungen</h3>
	<div class="container">
		<div class="row">
			<form class="col s12" action="setn.py" method="post">
				<input type="hidden" name="referer" value="index" />
				<div class="row">"""
	displaysets()
	print u"""\
					<div class="col s12">
						<center><a class="btn waves-effect waves-light """+colors.color+"""\" href=setn.py?referer=row&createnum="""+unicode(rowsone)+"""><i class="mdi-content-add"></i></a></center>
						<p class="range-field"><input type="range" id="teilung" name="teilung" min="1" max="99" value=\""""+unicode(common.readsettings("TEILUNG"))+"""\" /></p>
						<div class="row">
							<div class="col s6">
								<div class="card white darken-1">
									<div class="card-content white-text">
										<span class="card-title """+colors.color+"""-text text-darken-2">Alle Seiten</span><br>
										<div class="row">
											<div class="input-field col s12">
												<input value=\""""+cgi.escape(unicode(common.testexist("REFRESH", "global", 0)))+"""\" name="REFRESH-global-0" id="REFRESH-global-0" type="text">
												<label for="REFRESH-global-0">Alle Seiten neu laden</label>
											</div>
										</div>
										<div>
											<input type="checkbox" name="REFRESHAKTIV-global-0" id="REFRESHAKTIV-global-0" """+common.aktiv("REFRESHAKTIV", "global", 0)+"""/>
											<label for="REFRESHAKTIV-global-0">Globales neu laden aktiviert</label>
											<input type="hidden" value="0" name="HIDDEN.REFRESHAKTIV-global-0">
										</div>
									</div>
								</div>
							</div>
							<div class="col s6">
								<div class="card white darken-1">
									<div class="card-content white-text">
										<span class="card-title """+colors.color+"""-text text-darken-2">Monitornjus Frontend</span><br>
										<div class="row">
											<div class="input-field col s12">
												<input value=\""""+cgi.escape(unicode(common.testexist("REFRESH", "globalmon", 0)))+"""\" name="REFRESH-globalmon-0" id="REFRESH-globalmon-0" type="text">
												<label for="REFRESH-globalmon-0">Monitornjus Frontend neu laden</label>
											</div>
										</div>
										<div>
											<input type="checkbox" name="REFRESHAKTIV-globalmon-0" id="REFRESHAKTIV-globalmon-0" """+common.aktiv("REFRESHAKTIV", "globalmon", 0)+"""/>
											<label for="REFRESHAKTIV-globalmon-0">Monitornjus neu laden</label>
											<input type="hidden" value="0" name="HIDDEN.REFRESHAKTIV-globalmon-0">
										</div>
									</div>
								</div>
							</div>
						</div>
						<button class="btn waves-effect waves-light" type="submit">Abschicken<i class="mdi-content-send right"></i></button>"""
	if common.triggerrefresh:
		print u"""\
						<a class="waves-effect waves-light btn right" href="setn.py?referer=triggerrefresh">Neuladen auslösen</a>"""
	print u"""\
					</div>
				</div>
			</form>
		</div>
	</div>
	<footer class="page-footer """+colors.color+"""\">
		<div class="container">
			<div class="row">
				<div class="col l6 s12">
					<h5 class="white-text">MonitorNjus f&uuml;r das JVG-Ehingen</h5>
				</div>
			</div>
		</div>
		<div class="footer-copyright">
			<div class="container">
				&copy; Steffen Deusch """+str(common.datum.year)+"""
				<a class="grey-text text-lighten-4 right" href="https://github.com/SteffenDE/monitornjus">"""+common.version+"""</a>
			</div>
		</div>
	</footer>
	<!-- Scripts -->
	<script src="../bin/js/init.js"></script>
</body>"""
	import sys
	sys.stdout.write(u"</html>")
	del sys

except Exception as e:
	common.debug(e)