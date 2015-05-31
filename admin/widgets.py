#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 07.05.2015 (Version 0.7.1)

try:
	import colors
	import os
	import imp
	workingdir = os.getcwd()
	if "admin" in workingdir:
	    common = imp.load_source('common', workingdir+"/../common.py")
	else:
	    common = imp.load_source('common', workingdir+"/common.py")
	import checkvalues

	common.authenticated()

	print "Content-Type: text/html"
	print
	print """
<!DOCTYPE html>
<html lang="de">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no"/>
	<link href="../bin/css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	<title>MonitorNjus Admin-Panel</title>
	<style type="text/css">
	.input-field label { opacity: 0; }

	.secondary-content, .input-field .prefix.active, .input-field input[type=text]:focus + label, .input-field input[type=password]:focus + label, .input-field input[type=email]:focus + label, .input-field input[type=url]:focus + label, .input-field input[type=date]:focus + label, .input-field input[type=tel]:focus + label, .input-field input[type=number]:focus + label, .input-field input[type=search]:focus + label, .input-field textarea:focus.materialize-textarea + label, .dropdown-content li > a, .dropdown-content li > span { 
		color: """+colors.hexa+"""; opacity: 1; 
	}

	.switch label input[type=checkbox]:first-child:checked + .lever { 
		background-color: """+colors.hexa+"""; opacity: 1; 
	}

	input[type=text]:focus, input[type=password]:focus, input[type=email]:focus, input[type=url]:focus, input[type=date]:focus, input[type=tel]:focus, input[type=number]:focus, input[type=search]:focus, textarea:focus.materialize-textarea { 
		border-bottom: 1px solid """+colors.hexa+""";
		-webkit-box-shadow: 0 1px 0 0 """+colors.hexa+""";
		-moz-box-shadow: 0 1px 0 0 """+colors.hexa+""";
		box-shadow: 0 1px 0 0 """+colors.hexa+"""; 
	}

	[type="checkbox"]:checked + label:before {
		border-right: 2px solid """+colors.hexa+""";
		border-bottom: 2px solid """+colors.hexa+"""; 
	}

	.btn:hover, .btn-large:hover { 
		background-color: """+colors.hexa+"""; opacity: 1; 
	}
	.btn, .btn-large, .btn-floating { 
		background-color: """+colors.hexa+"""; opacity: 0.8; 
	}

	</style>
</head>
<body>
	<script type="text/javascript" src="../bin/js/jquery-2.1.3.min.js"></script>
	<script type="text/javascript" src="../bin/js/materialize.min.js"></script>
	<nav class=\""""+colors.color+"""\"="navigation">
		<div class="container">
			<div class="nav-wrapper"><a id="logo-container" href="#" class="brand-logo">MonitorNjus Admin Panel</a>
				<ul class="right">
					<li><a href="index.py">Haupteinstellungen</a></li>
					<li><a href="../bin/">Zum Frontend</a></li>
				</ul>
				<a href="#" data-activates="nav-mobile" class="button-collapse"><i class="mdi-navigation-menu"></i></a>
			</div>
		</div>
	</nav>
	<h3 class="header center """+colors.color+"""-text">Widgets</h3>
	<div class="container">
		<div class="row">
			<form class="col s12" action="setn.py?referer=widgets" method="post">
				<div class="row">
					<div class="col s6">
						<div class="card white darken-1">
							<div class="card-content white-text">
								<span class="card-title """+colors.color+"""-text text-darken-2">Admin-Link</span><br><br>
								<input type="checkbox" name="adminlinkaktiv" id="adminlinkaktiv" """+checkvalues.adminlinkaktiv+"""/>
								<label for="adminlinkaktiv">Admin-Link aktiviert</label>
								<div class="row">
									<div class="col s6">
										<select name="dropdown_adminlink_valign">"""+checkvalues.adminlinkvalign+"""
										</select>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input style="color:black;" placeholder=\'"""+str(common.getwidgetinfo("Admin-Link", "align"))+"""\' name="adminlinkalign" id="adminlinkalign" type="text"/>
												<label for="adminlinkalign">Vertikaler Abstand</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<select name="dropdown_adminlink_vmargin">"""+checkvalues.adminlinkvmargin+"""
										</select>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input style="color:black;" placeholder=\'"""+str(common.getwidgetinfo("Admin-Link", "margin"))+"""\' name="adminlinkmargin" id="adminlinkmargin" type="text"/>
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
								<input type="checkbox" name="uhraktiv" id="uhraktiv" """+checkvalues.uhraktiv+"""/>
								<label for="uhraktiv">Uhr aktiviert</label>
								<div class="row">
									<div class="input-field col s12">
										<input style="color:black;" placeholder=\""""+checkvalues.uhrlink+"""\" name="uhrlink" id="uhrlink" type="text"/>
										<label for="uhrlink">Uhr-URL</label>
									</div>
								</div>
								<div class="row">
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input style="color:black;" placeholder=\'"""+str(common.getwidgetinfo("Uhr", "height"))+"""\' name="uhrheight" id="uhrheight" type="text"/>
												<label for="uhrheight">Uhr-H&ouml;he</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input style="color:black;" placeholder=\'"""+str(common.getwidgetinfo("Uhr", "width"))+"""\' name="uhrwidth" id="uhrwidth" type="text"/>
												<label for="uhrwidth">Uhr-Breite</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<select name="dropdown_uhr_valign">"""+checkvalues.uhrvalign+"""
										</select>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input style="color:black;" placeholder=\'"""+str(common.getwidgetinfo("Uhr", "align"))+"""\' name="uhralign" id="uhralign" type="text"/>
												<label for="uhralign">Vertikaler Abstand</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<select name="dropdown_uhr_vmargin">"""+checkvalues.uhrvmargin+"""
										</select>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input style="color:black;" placeholder=\'"""+str(common.getwidgetinfo("Uhr", "margin"))+"""\' name="uhrmargin" id="uhrmargin" type="text"/>
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
								<input type="checkbox" name="widgetaktiv" id="widgetaktiv" """+checkvalues.widgetaktiv+"""/>
								<label for="widgetaktiv">Widget aktiviert</label>
								<div class="row">
									<div class="input-field col s12">
										<input style="color:black;" placeholder=\'"""+checkvalues.widgetlink+"""\' name="widgetlink" id="widgetlink" type="text"/>
										<label for="widgetlink">Widget-URL</label>
									</div>
								</div>
								<div class="row">
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input style="color:black;" placeholder=\'"""+str(common.getwidgetinfo("Freies-Widget", "height"))+"""\' name="widgetheight" id="widgetheight" type="text"/>
												<label for="widgetheight">Widget-H&ouml;he</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input style="color:black;" placeholder=\'"""+str(common.getwidgetinfo("Freies-Widget", "width"))+"""\' name="widgetwidth" id="widgetwidth" type="text"/>
												<label for="widgetwidth">Widget-Breite</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<select name="dropdown_widget_valign">"""+checkvalues.widgetvalign+"""
										</select>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input style="color:black;" placeholder=\'"""+str(common.getwidgetinfo("Freies-Widget", "align"))+"""\' name="widgetalign" id="widgetalign" type="text"/>
												<label for="widgetalign">Vertikaler Abstand</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<select name="dropdown_widget_vmargin">"""+checkvalues.widgetvmargin+"""
										</select>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input style="color:black;" placeholder=\'"""+str(common.getwidgetinfo("Freies-Widget", "margin"))+"""\' name="widgetmargin" id="widgetmargin" type="text"/>
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
								<input type="checkbox" name="logoaktiv" id="logoaktiv" """+checkvalues.logoaktiv+"""/>
								<label for="logoaktiv">Logo aktiviert</label>
								<div class="row">
									<div class="input-field col s12">
										<input style="color:black;" placeholder=\""""+checkvalues.logolink+"""\" name="logolink" id="logolink" type="text"/>
										<label for="logolink">logo-URL</label>
									</div>
								</div>
								<div class="row">
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input style="color:black;" placeholder=\'"""+checkvalues.logoheight+"""\' name="logoheight" id="logoheight" type="text"/>
												<label for="logoheight">Logo-H&ouml;he</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input style="color:black;" placeholder=\'"""+checkvalues.logowidth+"""\' name="logowidth" id="logowidth" type="text"/>
												<label for="logowidth">Logo-Breite</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<select name="dropdown_logo_valign">"""+checkvalues.logovalign+"""
										</select>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input style="color:black;" placeholder=\'"""+checkvalues.logoalign+"""\' name="logoalign" id="logoalign" type="text"/>
												<label for="logoalign">Vertikaler Abstand</label>
											</div>
										</div>
									</div>
									<div class="col s6">
										<select name="dropdown_logo_vmargin">"""+checkvalues.logovmargin+"""
										</select>
									</div>
									<div class="col s6">
										<div class="row">
											<div class="input-field col s12">
												<input style="color:black;" placeholder=\'"""+checkvalues.logomargin+"""\' name="logomargin" id="logomargin" type="text"/>
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
</body>
</html>
	""" % (common.datum.year)

except Exception as e:
    common.debug(e)