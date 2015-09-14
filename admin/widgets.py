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
sys.path.append(workingdir+"/../")
sys.setdefaultencoding('utf-8')
import cgi
from modules import common
from modules import colors

def widgets():
	count = common.getwidgets()
	out = ""
	for item in count:
		typ = common.getwidgTYPfromID(item)
		if typ == "Adminlink":
			out += u"""\
					<li>
						<div class="collapsible-header active">"""+unicode(item)+""". Admin-Link</div>
						<div class="collapsible-body">
							<div class="container" style="min-width: 100%; padding-top: 5%;">
								<input type="checkbox" name="AKTIV-Adminlink-"""+unicode(item)+"""\" id="AKTIV-Adminlink-"""+unicode(item)+"""\" """+common.widgaktiv("Adminlink", item)+"""/>
								<label for="AKTIV-Adminlink-"""+unicode(item)+"""\">Adminlink aktiviert</label>
								<input type="hidden" value="0" name="HIDDEN.AKTIV-Adminlink-"""+unicode(item)+"""\">
								<div class="row">
									<div class="col s6">
										<select name="valign-Adminlink-"""+unicode(item)+"""\">"""+common.valign("Adminlink", item, "valign")+"""
										</select>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Adminlink", item, "align")+"""\' name="align-Adminlink-"""+unicode(item)+"""\" id="align-Adminlink-"""+unicode(item)+"""\" type="text"/>
												<label for="align-Adminlink-"""+unicode(item)+"""\">Vertikaler Abstand</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<select name="vmargin-Adminlink-"""+unicode(item)+"""\">"""+common.valign("Adminlink", item, "vmargin")+"""
										</select>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Adminlink", item, "margin")+"""\' name="margin-Adminlink-"""+unicode(item)+"""\" id="margin-Adminlink-"""+unicode(item)+"""\" type="text"/>
												<label for="margin-Adminlink-"""+unicode(item)+"""\">Horizontaler Abstand</label>
											</div>
										</div>
									</div>
								</div>
							</div>"""

		elif typ == "Logo":
				out += """\
					<li>
						<div class="collapsible-header">"""+unicode(item)+""". Logo</div>
						<div class="collapsible-body">
							<div class="container" style="min-width: 100%; padding-top: 5%;">
								<input type="checkbox" name="AKTIV-Logo-"""+unicode(item)+"""\" id="AKTIV-Logo-"""+unicode(item)+"""\" """+common.widgaktiv("Logo", item)+"""/>
								<label for="AKTIV-Logo-"""+unicode(item)+"""\">Logo aktiviert</label>
								<input type="hidden" value="0" name="HIDDEN.AKTIV-Logo-"""+unicode(item)+"""\">
								<div class="row">
									<div class="input-field col s12">
										<input value=\""""+common.getwidgetinfo("Logo", item, "URL")+"""\" name="URL-Logo-"""+unicode(item)+"""\" id="URL-Logo-"""+unicode(item)+"""\" type="text"/>
										<label for="URL-Logo-"""+unicode(item)+"""\">Logo-URL</label>
									</div>
								</div>
								<div class="row">
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Logo", item, "height")+"""\' name="height-Logo-"""+unicode(item)+"""\" id="height-Logo-"""+unicode(item)+"""\" type="text"/>
												<label for="height-Logo-"""+unicode(item)+"""\">Logo-H&ouml;he</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Logo", item, "width")+"""\' name="width-Logo-"""+unicode(item)+"""\" id="width-Logo-"""+unicode(item)+"""\" type="text"/>
												<label for="width-Logo-"""+unicode(item)+"""\">Logo-Breite</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<select name="valign-Logo-"""+unicode(item)+"""\">"""+common.valign("Logo", item, "valign")+"""
										</select>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Logo", item, "align")+"""\' name="align-Logo-"""+unicode(item)+"""\" id="align-Logo-"""+unicode(item)+"""\" type="text"/>
												<label for="align-Logo-"""+unicode(item)+"""\">Vertikaler Abstand</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<select name="vmargin-Logo-"""+unicode(item)+"""\">"""+common.valign("Logo", item, "vmargin")+"""
										</select>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Logo", item, "margin")+"""\' name="margin-Logo-"""+unicode(item)+"""\" id="margin-Logo-"""+unicode(item)+"""\" type="text"/>
												<label for="margin-Logo-"""+unicode(item)+"""\">Horizontaler Abstand</label>
											</div>
										</div>
									</div>
								</div>
							</div>"""

		elif typ == "Freies_Widget":
			out += """\
					<li>
						<div class="collapsible-header">"""+unicode(item)+""". Freies Widget</div>
						<div class="collapsible-body">
							<div class="container" style="min-width: 100%; padding-top: 5%;">
								<input type="checkbox" name="AKTIV-Freies_Widget-"""+unicode(item)+"""\" id="AKTIV-Freies_Widget-"""+unicode(item)+"""\" """+common.widgaktiv("Freies_Widget", item)+"""/>
								<label for="AKTIV-Freies_Widget-"""+unicode(item)+"""\">Widget aktiviert</label>
								<input type="hidden" value="0" name="HIDDEN.AKTIV-Freies_Widget-"""+unicode(item)+"""\">
								<div class="row">
									<div class="input-field col s12">
										<textarea style="color:black;" name="URL-Freies_Widget-"""+unicode(item)+"""\" id="URL-Freies_Widget-"""+unicode(item)+"""\" class="materialize-textarea">"""+cgi.escape(common.getwidgetinfo("Freies_Widget", item, "URL"))+"""</textarea>
										<label for="URL-Freies_Widget-"""+unicode(item)+"""\">Widget-URL</label>
									</div>
								</div>
								<div class="row">
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Freies_Widget", item, "height")+"""\' name="height-Freies_Widget-"""+unicode(item)+"""\" id="height-Freies_Widget-"""+unicode(item)+"""\" type="text"/>
												<label for="height-Freies_Widget-"""+unicode(item)+"""\">Widget-H&ouml;he</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Freies_Widget", item, "width")+"""\' name="width-Freies_Widget-"""+unicode(item)+"""\" id="width-Freies_Widget-"""+unicode(item)+"""\" type="text"/>
												<label for="width-Freies_Widget-"""+unicode(item)+"""\">Widget-Breite</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<select name="valign-Freies_Widget-"""+unicode(item)+"""\">"""+common.valign("Freies_Widget", item, "valign")+"""
										</select>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Freies_Widget", item, "align")+"""\' name="align-Freies_Widget-"""+unicode(item)+"""\" id="align-Freies_Widget-"""+unicode(item)+"""\" type="text"/>
												<label for="align-Freies_Widget-"""+unicode(item)+"""\">Vertikaler Abstand</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<select name="vmargin-Freies_Widget-"""+unicode(item)+"""\">"""+common.valign("Freies_Widget", item, "vmargin")+"""
										</select>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input value=\'"""+common.getwidgetinfo("Freies_Widget", item, "margin")+"""\' name="margin-Freies_Widget-"""+unicode(item)+"""\" id="margin-Freies_Widget-"""+unicode(item)+"""\" type="text"/>
												<label for="margin-Freies_Widget-"""+unicode(item)+"""\">Horizontaler Abstand</label>
											</div>
										</div>
									</div>
								</div>
							</div>"""
		
		if typ != "Adminlink":																									
			out += """
							<center><a class="waves-effect waves-light btn" href="setn.py?referer=delwidget&delnum="""+unicode(item)+"""\">Widget l&ouml;schen</a></center>"""
		out += """
						</div>
					</li>\n"""
	return out

try:
	if common.authentication:
		from modules import auth
		auth.me()

	print u"Content-Type: text/html\n"
	print u"""\
<!DOCTYPE html>
<html lang="de">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no"/>
	<link href="../bin/css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	<title>MonitorNjus Admin-Panel Widgets</title>
	<!-- MonitorNjus -->
	<!-- Copyright (c) """+unicode(common.datum.year)+""" Steffen Deusch -->
	<!-- https://github.com/SteffenDE/MonitorNjus -->"""
	print colors.adminstyles
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
			<div class="col s6">
				<form class="col s12" action="setn.py" method="post">
					<input type="hidden" name="referer" value="widgets" />
					<ul class="collapsible" data-collapsible="accordion">"""
	print widgets()
	print u"""\
					</ul>
					<button class="btn waves-effect waves-light" type="submit">Abschicken<i class="mdi-content-send right"></i></button>
				</form>
			</div>
			<div class="col s6">
				<form class="col s12" action="setn.py" method="post">
					<div class="card-panel">
						<div class="row">
							<input type="hidden" name="referer" value="newwidget" />
							<div class="input-field col s12">
								<select name="art">
									<option value="" disabled selected>Widgetart wählen</option>
									<option value="Logo">Logo</option>
									<option value="Freies_Widget">Freies Widget</option>
								</select>
								<label>Materialize Select</label>
							</div>
						</div>
					</div>
					<button class="btn waves-effect waves-light" type="submit">Widget hinzufügen.</button>
				</form>
			</div>
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
	</row>
</footer>
<!--  Scripts-->
<script src="../bin/js/init.js"></script>
</body>"""
	import sys
	sys.stdout.write(u"</html>")
	del sys

except Exception as e:
	common.debug(e)