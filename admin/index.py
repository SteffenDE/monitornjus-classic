#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 22.07.2015 (Version 0.8.4)

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import imp
workingdir = os.path.dirname(os.path.realpath(__file__))
common = imp.load_source('common', workingdir+"/../common.py")

try:
	import colors
	import firstrun

	common.authenticated()

	rows = int(common.getrows())
	rowsone = rows + 1

	import cgi

	def displaysets():
		x = 1
		while x <= rows:
			if unicode(x) in common.getallrows():
				print """\
				<div class="col s12">
					<h5 class="header center """+colors.color+"""-text">Displayset """+unicode(x)+"""</h5>
					<div class="row">
						<div class="col s6">
							<div class="card white darken-1">
								<div class="card-content white-text">
									<span class="card-title """+colors.color+"""-text text-darken-2">Linke Seite</span><br>
									<div class="row">
										<div class="input-field col s6">
											<input value=\""""+cgi.escape(unicode(common.testexist("URL", "Links", x)))+"""\" name="url1-"""+unicode(x)+"""" id="url1-"""+unicode(x)+"""" type="text">
											<label for="url1-"""+unicode(x)+"""">URL Links</label>
										</div>
										<div class="input-field col s6">
											<input value=\""""+cgi.escape(unicode(common.testexist("REFRESH", "Links", x)))+"""\" name="refresh1-"""+unicode(x)+"""" id="refresh1-"""+unicode(x)+"""" type="number">
											<label for="refresh1-"""+unicode(x)+"""">Refresh Links</label>
										</div>
									</div>
									<div>
										<input type="checkbox" name="leftenabled-"""+unicode(x)+"""" id="leftenabled-"""+unicode(x)+"""" """+common.aktiv("AKTIV", "Links", x)+"""/>
										<label for="leftenabled-"""+unicode(x)+"""">Links aktiviert</label>&nbsp;&nbsp;&nbsp;&nbsp;
										<input type="checkbox" name="refreshleftenabled-"""+unicode(x)+"""" id="refreshleftenabled-"""+unicode(x)+"""" """+common.aktiv("REFRESHAKTIV", "Links", x)+"""/>
										<label for="refreshleftenabled-"""+unicode(x)+"""">Links neu laden</label>
									</div>
									<div class="row">
										<div class="input-field col s4">
											<input value=\""""+cgi.escape(unicode(common.getdate("uhrzeit", "Links", x)))+"""\" name="uhrzeit-Links-"""+unicode(x)+"""" id="uhrzeit-Links-"""+unicode(x)+"""" type="text">
											<label for="uhrzeit-Links-"""+unicode(x)+"""">Uhrzeit</label>
										</div>
										<div class="input-field col s4">
											<input value=\""""+cgi.escape(unicode(common.getdate("wochentag", "Links", x)))+"""\" name="wochentag-Links-"""+unicode(x)+"""" id="wochentag-Links-"""+unicode(x)+"""" type="text">
											<label for="wochentag-Links-"""+unicode(x)+"""">Wochentag</label>
										</div>
										<div class="input-field col s2">
											<input value=\""""+cgi.escape(unicode(common.getdate("tag", "Links", x)))+"""\" name="tag-Links-"""+unicode(x)+"""" id="tag-Links-"""+unicode(x)+"""" type="text">
											<label for="tag-Links-"""+unicode(x)+"""">Tag</label>
										</div>
										<div class="input-field col s2">
											<input value=\""""+cgi.escape(unicode(common.getdate("monat", "Links", x)))+"""\" name="monat-Links-"""+unicode(x)+"""" id="monat-Links-"""+unicode(x)+"""" type="text">
											<label for="monat-Links-"""+unicode(x)+"""">Monat</label>
										</div>
									</div>
									<div class="row">
										<div class="input-field col s3">
											<input value=\""""+cgi.escape(unicode(common.getinfo("MARGINLEFT","Links",x)))+"""\" name="marginleft-Links-"""+unicode(x)+"""" id="marginleft-Links-"""+unicode(x)+"""" type="text">
											<label for="marginleft-Links-"""+unicode(x)+"""">Rand-Links</label>
										</div>
										<div class="input-field col s3">
											<input value=\""""+cgi.escape(unicode(common.getinfo("MARGINRIGHT","Links",x)))+"""\" name="marginright-Links-"""+unicode(x)+"""" id="marginright-Links-"""+unicode(x)+"""" type="text">
											<label for="marginright-Links-"""+unicode(x)+"""">Rand-Rechts</label>
										</div>
										<div class="input-field col s3">
											<input value=\""""+cgi.escape(unicode(common.getinfo("MARGINTOP","Links",x)))+"""\" name="margintop-Links-"""+unicode(x)+"""" id="margintop-Links-"""+unicode(x)+"""" type="text">
											<label for="margintop-Links-"""+unicode(x)+"""">Rand-Oben</label>
										</div>
										<div class="input-field col s3">
											<input value=\""""+cgi.escape(unicode(common.getinfo("MARGINBOTTOM","Links",x)))+"""\" name="marginbottom-Links-"""+unicode(x)+"""" id="marginbottom-Links-"""+unicode(x)+"""" type="text">
											<label for="marginbottom-Links-"""+unicode(x)+"""">Rand-Unten</label>
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
											<input value=\""""+cgi.escape(unicode(common.testexist("URL", "Rechts", x)))+"""\" name="url2-"""+unicode(x)+"""" id="url2-"""+unicode(x)+"""" type="text">
											<label for="url2-"""+unicode(x)+"""">URL Rechts</label>
										</div>
										<div class="input-field col s6">
											<input value=\""""+cgi.escape(unicode(common.testexist("REFRESH", "Rechts", x)))+"""\" name="refresh2-"""+unicode(x)+"""" id="refresh2-"""+unicode(x)+"""" type="number">
											<label for="refresh2-"""+unicode(x)+"""">Refresh Rechts</label>
										</div>
									</div>
									<div>
										<input type="checkbox" name="rightenabled-"""+unicode(x)+"""" id="rightenabled-"""+unicode(x)+"""" """+common.aktiv("AKTIV", "Rechts", x)+"""/>
										<label for="rightenabled-"""+unicode(x)+"""">Rechts aktiviert</label>&nbsp;&nbsp;&nbsp;&nbsp;
										<input type="checkbox" name="refreshrightenabled-"""+unicode(x)+"""" id="refreshrightenabled-"""+unicode(x)+"""" """+common.aktiv("REFRESHAKTIV", "Rechts", x)+"""/>
										<label for="refreshrightenabled-"""+unicode(x)+"""">Rechts neu laden</label>
									</div>
									<div class="row">
										<div class="input-field col s4">
											<input value=\""""+cgi.escape(unicode(common.getdate("uhrzeit", "Rechts", x)))+"""\" name="uhrzeit-Rechts-"""+unicode(x)+"""" id="uhrzeit-Rechts-"""+unicode(x)+"""" type="text">
											<label for="uhrzeit-Rechts-"""+unicode(x)+"""">Uhrzeit</label>
										</div>
										<div class="input-field col s4">
											<input value=\""""+cgi.escape(unicode(common.getdate("wochentag", "Rechts", x)))+"""\" name="wochentag-Rechts-"""+unicode(x)+"""" id="wochentag-Rechts-"""+unicode(x)+"""" type="text">
											<label for="wochentag-Rechts-"""+unicode(x)+"""">Wochentag</label>
										</div>
										<div class="input-field col s2">
											<input value=\""""+cgi.escape(unicode(common.getdate("tag", "Rechts", x)))+"""\" name="tag-Rechts-"""+unicode(x)+"""" id="tag-Rechts-"""+unicode(x)+"""" type="text">
											<label for="tag-Rechts-"""+unicode(x)+"""">Tag</label>
										</div>
										<div class="input-field col s2">
											<input value=\""""+cgi.escape(unicode(common.getdate("monat", "Rechts", x)))+"""\" name="monat-Rechts-"""+unicode(x)+"""" id="monat-Rechts-"""+unicode(x)+"""" type="text">
											<label for="monat-Rechts-"""+unicode(x)+"""">Monat</label>
										</div>
									</div>
									<div class="row">
										<div class="input-field col s3">
											<input value=\""""+cgi.escape(unicode(common.getinfo("MARGINLEFT","Rechts",x)))+"""\" name="marginleft-Rechts-"""+unicode(x)+"""" id="marginleft-Rechts-"""+unicode(x)+"""" type="text">
											<label for="marginleft-Rechts-"""+unicode(x)+"""">Rand-Links</label>
										</div>
										<div class="input-field col s3">
											<input value=\""""+cgi.escape(unicode(common.getinfo("MARGINRIGHT","Rechts",x)))+"""\" name="marginright-Rechts-"""+unicode(x)+"""" id="marginright-Rechts-"""+unicode(x)+"""" type="text">
											<label for="marginright-Rechts-"""+unicode(x)+"""">Rand-Rechts</label>
										</div>
										<div class="input-field col s3">
											<input value=\""""+cgi.escape(unicode(common.getinfo("MARGINTOP","Rechts",x)))+"""\" name="margintop-Rechts-"""+unicode(x)+"""" id="margintop-Rechts-"""+unicode(x)+"""" type="text">
											<label for="margintop-Rechts-"""+unicode(x)+"""">Rand-Oben</label>
										</div>
										<div class="input-field col s3">
											<input value=\""""+cgi.escape(unicode(common.getinfo("MARGINBOTTOM","Rechts",x)))+"""\" name="marginbottom-Rechts-"""+unicode(x)+"""" id="marginbottom-Rechts-"""+unicode(x)+"""" type="text">
											<label for="marginbottom-Rechts-"""+unicode(x)+"""">Rand-Unten</label>
										</div>
									</div>
								</div>
							</div>
						</div>"""
				if rows != 1:
					print """<center><a class="waves-effect waves-light btn" href="setn.py?referer=row&delnum="""+unicode(x)+"""">Displayset l&ouml;schen</a></center>"""
				print """\
					</div>
				</div>"""
			x = x + 1

	print "Content-Type: text/html\n"
	print """\
<!DOCTYPE html>
<html lang="de">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no"/>
	<link href="../bin/css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	<title>MonitorNjus Admin-Panel</title>"""
	print colors.adminstyles
	print """\
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
	print """\
					<div class="col s12">
						<center><a class="btn waves-effect waves-light """+colors.color+"""" href=setn.py?referer=row&createnum="""+unicode(rowsone)+"""><i class="mdi-content-add"></i></a></center>
						<p class="range-field"><input type="range" id="teilung" name="teilung" min="1" max="99" value=\""""+unicode(common.readsettings("TEILUNG"))+"""\" /></p>
						<div class="row">
							<div class="col s6">
								<div class="card white darken-1">
									<div class="card-content white-text">
										<span class="card-title """+colors.color+"""-text text-darken-2">Alle Seiten</span><br>
										<div class="row">
											<div class="input-field col s12">
												<input value=\""""+cgi.escape(unicode(common.testexist("REFRESH", "global", 0)))+"""\" name="refreshall" id="refreshall" type="text">
												<label for="refreshall">Alle Seiten neu laden</label>
											</div>
										</div>
										<div>
											<input type="checkbox" name="refreshallenabled" id="refreshallenabled" """+common.aktiv("REFRESHAKTIV", "global", 0)+"""/>
											<label for="refreshallenabled">Globales neu laden aktiviert</label>
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
												<input value=\""""+cgi.escape(unicode(common.testexist("REFRESH", "globalmon", 0)))+"""\" name="refreshmon" id="refreshmon" type="text">
												<label for="refreshmon">Monitornjus Frontend neu laden</label>
											</div>
										</div>
										<div>
											<input type="checkbox" name="refreshmonenabled" id="refreshmonenabled" """+common.aktiv("REFRESHAKTIV", "globalmon", 0)+"""/>
											<label for="refreshmonenabled">Monitornjus neu laden</label>
										</div>
									</div>
								</div>
							</div>
						</div>
						<button class="btn waves-effect waves-light" type="submit">Abschicken<i class="mdi-content-send right"></i></button>
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
	sys.stdout.write("</html>")
	del sys

except Exception as e:
	common.debug(e)