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
	import cgi

	common.authenticated()

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
					<li><a href="index.py">Haupteinstellungen</a></li>
					<li><a href="../bin/">Zum Frontend</a></li>
				</ul>
				<ul class="side-nav" id="mobile">
					<li><a href="index.py">Haupteinstellungen</a></li>
					<li><a href="../bin/">Zum Frontend</a></li>
				</ul>
			</div>
		</div>
	</nav>
	<h3 class="header center """+colors.color+"""-text">Widgets</h3>
	<div class="container">
		<div class="row">
			<form class="col s12" action="setn.py" method="post">
				<input type="hidden" name="referer" value="widgets" />
				<div class="row">
					<div class="col s6">
						<div class="card white darken-1">
							<div class="card-content white-text">
								<span class="card-title """+colors.color+"""-text text-darken-2">Admin-Link</span><br><br>
								<input type="checkbox" name="adminlinkaktiv" id="adminlinkaktiv" """+common.widgaktiv("Admin-Link")+"""/>
								<label for="adminlinkaktiv">Admin-Link aktiviert</label>
								<div class="row">
									<div class="col s6">
										<select name="dropdown_adminlink_valign">"""+common.valign("Admin-Link", "valign")+"""
										</select>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Admin-Link", "align")+"""\' name="adminlinkalign" id="adminlinkalign" type="text"/>
												<label for="adminlinkalign">Vertikaler Abstand</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<select name="dropdown_adminlink_vmargin">"""+common.valign("Admin-Link", "vmargin")+"""
										</select>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Admin-Link", "margin")+"""\' name="adminlinkmargin" id="adminlinkmargin" type="text"/>
												<label for="adminlinkmargin">Horizontaler Abstand</label>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
					<div class="col s6">
						<div class="card white darken-1">
							<div class="card-content white-text">
								<span class="card-title """+colors.color+"""-text text-darken-2">Uhr</span><br><br>
								<input type="checkbox" name="uhraktiv" id="uhraktiv" """+common.widgaktiv("Uhr")+"""/>
								<label for="uhraktiv">Uhr aktiviert</label>
								<div class="row">
									<div class="input-field col s12">
										<input value=\""""+common.getwidgetinfo("Uhr", "URL")+"""\" name="uhrlink" id="uhrlink" type="text"/>
										<label for="uhrlink">Uhr-URL</label>
									</div>
								</div>
								<div class="row">
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Uhr", "height")+"""\' name="uhrheight" id="uhrheight" type="text"/>
												<label for="uhrheight">Uhr-H&ouml;he</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Uhr", "width")+"""\' name="uhrwidth" id="uhrwidth" type="text"/>
												<label for="uhrwidth">Uhr-Breite</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<select name="dropdown_uhr_valign">"""+common.valign("Uhr", "valign")+"""
										</select>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Uhr", "align")+"""\' name="uhralign" id="uhralign" type="text"/>
												<label for="uhralign">Vertikaler Abstand</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<select name="dropdown_uhr_vmargin">"""+common.valign("Uhr", "vmargin")+"""
										</select>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Uhr", "margin")+"""\' name="uhrmargin" id="uhrmargin" type="text"/>
												<label for="uhrmargin">Horizontaler Abstand</label>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
					<div class="col s6">
						<div class="card white darken-1">
							<div class="card-content white-text">
								<span class="card-title """+colors.color+"""-text text-darken-2">Freies Widget</span><br><br>
								<input type="checkbox" name="widgetaktiv" id="widgetaktiv" """+common.widgaktiv("Freies-Widget")+"""/>
								<label for="widgetaktiv">Widget aktiviert</label>
								<div class="row">
									<div class="input-field col s12">
										<textarea style="color:black;" name="widgetlink" id="widgetlink" class="materialize-textarea">"""+cgi.escape(common.getwidgetinfo("Freies-Widget", "URL"))+"""</textarea>
										<label for="widgetlink">Widget-URL</label>
									</div>
								</div>
								<div class="row">
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Freies-Widget", "height")+"""\' name="widgetheight" id="widgetheight" type="text"/>
												<label for="widgetheight">Widget-H&ouml;he</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Freies-Widget", "width")+"""\' name="widgetwidth" id="widgetwidth" type="text"/>
												<label for="widgetwidth">Widget-Breite</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<select name="dropdown_widget_valign">"""+common.valign("Freies-Widget", "valign")+"""
										</select>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Freies-Widget", "align")+"""\' name="widgetalign" id="widgetalign" type="text"/>
												<label for="widgetalign">Vertikaler Abstand</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<select name="dropdown_widget_vmargin">"""+common.valign("Freies-Widget", "vmargin")+"""
										</select>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Freies-Widget", "margin")+"""\' name="widgetmargin" id="widgetmargin" type="text"/>
												<label for="widgetmargin">Horizontaler Abstand</label>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
					<div class="col s6">
						<div class="card white darken-1">
							<div class="card-content white-text">
								<span class="card-title """+colors.color+"""-text text-darken-2">Logo</span><br><br>
								<input type="checkbox" name="logoaktiv" id="logoaktiv" """+common.widgaktiv("Logo")+"""/>
								<label for="logoaktiv">Logo aktiviert</label>
								<div class="row">
									<div class="input-field col s12">
										<input value=\""""+common.getwidgetinfo("Logo", "URL")+"""\" name="logolink" id="logolink" type="text"/>
										<label for="logolink">Logo-URL</label>
									</div>
								</div>
								<div class="row">
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Logo", "height")+"""\' name="logoheight" id="logoheight" type="text"/>
												<label for="logoheight">Logo-H&ouml;he</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Logo", "width")+"""\' name="logowidth" id="logowidth" type="text"/>
												<label for="logowidth">Logo-Breite</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<select name="dropdown_logo_valign">"""+common.valign("Logo", "valign")+"""
										</select>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Logo", "align")+"""\' name="logoalign" id="logoalign" type="text"/>
												<label for="logoalign">Vertikaler Abstand</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<select name="dropdown_logo_vmargin">"""+common.valign("Logo", "vmargin")+"""
										</select>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Logo", "margin")+"""\' name="logomargin" id="logomargin" type="text"/>
												<label for="logomargin">Horizontaler Abstand</label>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
				<button class="btn waves-effect waves-light" type="submit">Abschicken<i class="mdi-content-send right"></i></button>
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
				&copy; Steffen Deusch %d
			</div>
		</div>
	</row>
</footer>
<!--  Scripts-->
<script src="../bin/js/init.js"></script>
</body>""" % (common.datum.year)
	import sys
	sys.stdout.write("</html>")
	del sys

except Exception as e:
	common.debug(e)