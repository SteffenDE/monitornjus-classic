#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 18.06.2015 (Version 0.7.5)

try:
	import colors
	import os
	import firstrun
	import checkvalues
	import imp
	
	workingdir = os.getcwd()
	if "admin" in workingdir:
		common = imp.load_source('common', workingdir+"/../common.py")
	else:
		common = imp.load_source('common', workingdir+"/common.py")

	common.authenticated()

	rows = int(common.getrows())
	rowsone = rows + 1

	def displaysets():
		x = 1
		while x <= rows:
			if str(x) in common.getallrows():
				print """
						<div class="col s12">
							<h5 class="header center """+colors.color+"""-text">Displayset """+str(x)+"""</h5>
							<div class="row">
								<div class="col s6">
									<div class="card white darken-1">
										<div class="card-content white-text">
											<span class="card-title """+colors.color+"""-text text-darken-2">Linke Seite</span><br>
											<div class="row">
												<div class="input-field col s6">
													<input style="color:black;" placeholder=\""""+checkvalues.testexist("URL", "Links", x)+"""\" name="url1-"""+str(x)+"""" id="url1-"""+str(x)+"""" type="text">
													<label for="url1-"""+str(x)+"""">URL Links</label>
												</div>
												<div class="input-field col s6">
													<input style="color:black;" placeholder=\""""+str(checkvalues.testexist("REFRESH", "Links", x))+"""\" name="refresh1-"""+str(x)+"""" id="refresh1-"""+str(x)+"""" type="text">
													<label for="refresh1-"""+str(x)+"""">Refresh Links</label>
												</div>
											</div>
											<div>
												<input type="checkbox" name="leftenabled-"""+str(x)+"""" id="leftenabled-"""+str(x)+"""" """+checkvalues.aktiv("AKTIV", "Links", x)+"""/>
												<label for="leftenabled-"""+str(x)+"""">Links aktiviert</label>&nbsp;&nbsp;&nbsp;&nbsp;
												<input type="checkbox" name="refreshleftenabled-"""+str(x)+"""" id="refreshleftenabled-"""+str(x)+"""" """+checkvalues.aktiv("REFRESHAKTIV", "Links", x)+"""/>
												<label for="refreshleftenabled-"""+str(x)+"""">Links neuladen</label>
											</div>
											<!--<div>
												<input type="checkbox" name="vonbisaktivl-"""+str(x)+"""" id="vonbisaktivl-"""+str(x)+"""" """+checkvalues.aktiv("VONBISAKTIV", "Links", x)+"""/>
												<label for="vonbisaktivl-"""+str(x)+"""">Zeitangabe</label>
											</div>-->
											<div class="row">
												<div class="input-field col s4">
													<input style="color:black;" placeholder=\""""+checkvalues.getdate("uhrzeit", "Links", x)+"""\" name="uhrzeit-Links-"""+str(x)+"""" id="uhrzeit-Links-"""+str(x)+"""" type="text">
													<label for="uhrzeit-Links-"""+str(x)+"""">Uhrzeit</label>
												</div>
												<div class="input-field col s4">
													<input style="color:black;" placeholder=\""""+checkvalues.getdate("wochentag", "Links", x)+"""\" name="wochentag-Links-"""+str(x)+"""" id="wochentag-Links-"""+str(x)+"""" type="text">
													<label for="wochentag-Links-"""+str(x)+"""">Wochentag</label>
												</div>
												<div class="input-field col s2">
													<input style="color:black;" placeholder=\""""+checkvalues.getdate("tag", "Links", x)+"""\" name="tag-Links-"""+str(x)+"""" id="tag-Links-"""+str(x)+"""" type="text">
													<label for="tag-Links-"""+str(x)+"""">Tag</label>
												</div>
												<div class="input-field col s2">
													<input style="color:black;" placeholder=\""""+checkvalues.getdate("monat", "Links", x)+"""\" name="monat-Links-"""+str(x)+"""" id="monat-Links-"""+str(x)+"""" type="text">
													<label for="monat-Links-"""+str(x)+"""">Monat</label>
												</div>
											</div>
											<div class="row">
												<div class="input-field col s3">
													<input style="color:black;" placeholder=\""""+str(common.getinfo("MARGINLEFT","Links",x))+"""\" name="marginleft-Links-"""+str(x)+"""" id="marginleft-Links-"""+str(x)+"""" type="text">
													<label for="marginleft-Links-"""+str(x)+"""">Rand-Links</label>
												</div>
												<div class="input-field col s3">
													<input style="color:black;" placeholder=\""""+str(common.getinfo("MARGINRIGHT","Links",x))+"""\" name="marginright-Links-"""+str(x)+"""" id="marginright-Links-"""+str(x)+"""" type="text">
													<label for="marginright-Links-"""+str(x)+"""">Rand-Rechts</label>
												</div>
												<div class="input-field col s3">
													<input style="color:black;" placeholder=\""""+str(common.getinfo("MARGINTOP","Links",x))+"""\" name="margintop-Links-"""+str(x)+"""" id="margintop-Links-"""+str(x)+"""" type="text">
													<label for="margintop-Links-"""+str(x)+"""">Rand-Oben</label>
												</div>
												<div class="input-field col s3">
													<input style="color:black;" placeholder=\""""+str(common.getinfo("MARGINBOTTOM","Links",x))+"""\" name="marginbottom-Links-"""+str(x)+"""" id="marginbottom-Links-"""+str(x)+"""" type="text">
													<label for="marginbottom-Links-"""+str(x)+"""">Rand-Unten</label>
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
													<input style="color:black;" placeholder=\""""+checkvalues.testexist("URL", "Rechts", x)+"""\" name="url2-"""+str(x)+"""" id="url2-"""+str(x)+"""" type="text">
													<label for="url2-"""+str(x)+"""">URL Rechts</label>
												</div>
												<div class="input-field col s6">
													<input style="color:black;" placeholder=\""""+str(checkvalues.testexist("REFRESH", "Rechts", x))+"""\" name="refresh2-"""+str(x)+"""" id="refresh2-"""+str(x)+"""" type="text">
													<label for="refresh2-"""+str(x)+"""">Refresh Rechts</label>
												</div>
											</div>
											<div>
												<input type="checkbox" name="rightenabled-"""+str(x)+"""" id="rightenabled-"""+str(x)+"""" """+checkvalues.aktiv("AKTIV", "Rechts", x)+"""/>
												<label for="rightenabled-"""+str(x)+"""">Rechts aktiviert</label>&nbsp;&nbsp;&nbsp;&nbsp;
												<input type="checkbox" name="refreshrightenabled-"""+str(x)+"""" id="refreshrightenabled-"""+str(x)+"""" """+checkvalues.aktiv("REFRESHAKTIV", "Rechts", x)+"""/>
												<label for="refreshrightenabled-"""+str(x)+"""">Rechts neuladen</label>
											</div>
											<!--<div>
												<input type="checkbox" name="vonbisaktivr-"""+str(x)+"""" id="vonbisaktivr-"""+str(x)+"""" """+checkvalues.aktiv("VONBISAKTIV", "Rechts", x)+"""/>
												<label for="vonbisaktivr-"""+str(x)+"""">Zeitangabe</label>
											</div>-->
											<div class="row">
												<div class="input-field col s4">
													<input style="color:black;" placeholder=\""""+checkvalues.getdate("uhrzeit", "Rechts", x)+"""\" name="uhrzeit-Rechts-"""+str(x)+"""" id="uhrzeit-Rechts-"""+str(x)+"""" type="text">
													<label for="uhrzeit-Rechts-"""+str(x)+"""">Uhrzeit</label>
												</div>
												<div class="input-field col s4">
													<input style="color:black;" placeholder=\""""+checkvalues.getdate("wochentag", "Rechts", x)+"""\" name="wochentag-Rechts-"""+str(x)+"""" id="wochentag-Rechts-"""+str(x)+"""" type="text">
													<label for="wochentag-Rechts-"""+str(x)+"""">Wochentag</label>
												</div>
												<div class="input-field col s2">
													<input style="color:black;" placeholder=\""""+checkvalues.getdate("tag", "Rechts", x)+"""\" name="tag-Rechts-"""+str(x)+"""" id="tag-Rechts-"""+str(x)+"""" type="text">
													<label for="tag-Rechts-"""+str(x)+"""">Tag</label>
												</div>
												<div class="input-field col s2">
													<input style="color:black;" placeholder=\""""+checkvalues.getdate("monat", "Rechts", x)+"""\" name="monat-Rechts-"""+str(x)+"""" id="monat-Rechts-"""+str(x)+"""" type="text">
													<label for="monat-Rechts-"""+str(x)+"""">Monat</label>
												</div>
											</div>
											<div class="row">
												<div class="input-field col s3">
													<input style="color:black;" placeholder=\""""+str(common.getinfo("MARGINLEFT","Rechts",x))+"""\" name="marginleft-Rechts-"""+str(x)+"""" id="marginleft-Rechts-"""+str(x)+"""" type="text">
													<label for="marginleft-Rechts-"""+str(x)+"""">Rand-Links</label>
												</div>
												<div class="input-field col s3">
													<input style="color:black;" placeholder=\""""+str(common.getinfo("MARGINRIGHT","Rechts",x))+"""\" name="marginright-Rechts-"""+str(x)+"""" id="marginright-Rechts-"""+str(x)+"""" type="text">
													<label for="marginright-Rechts-"""+str(x)+"""">Rand-Rechts</label>
												</div>
												<div class="input-field col s3">
													<input style="color:black;" placeholder=\""""+str(common.getinfo("MARGINTOP","Rechts",x))+"""\" name="margintop-Rechts-"""+str(x)+"""" id="margintop-Rechts-"""+str(x)+"""" type="text">
													<label for="margintop-Rechts-"""+str(x)+"""">Rand-Oben</label>
												</div>
												<div class="input-field col s3">
													<input style="color:black;" placeholder=\""""+str(common.getinfo("MARGINBOTTOM","Rechts",x))+"""\" name="marginbottom-Rechts-"""+str(x)+"""" id="marginbottom-Rechts-"""+str(x)+"""" type="text">
													<label for="marginbottom-Rechts-"""+str(x)+"""">Rand-Unten</label>
												</div>
											</div>
										</div>
									</div>
								</div>"""
				if rows != 1:
					print """<center><a class="waves-effect waves-light btn" href="setn.py?referer=row&delrow=1&delnum="""+str(x)+"""">Displayset l&ouml;schen</a></center>"""
				print """
							</div>
						</div>"""
			x = x + 1

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

	.input-field label { 
		opacity: 0; 
	}

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

	.btn:hover, .btn-large:hover { background-color: """+colors.hexa+"""; opacity: 1; }
	.btn, .btn-large, .btn-floating { background-color: """+colors.hexa+"""; opacity: 0.8; }

	</style>
</head>
<body>
	<script type="text/javascript" src="../bin/js/jquery-2.1.3.min.js"></script>
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
					<center><a class="btn waves-effect waves-light """+colors.color+"""" href=setn.py?referer=row&createrow=1&createnum="""+str(rowsone)+"""><i class="mdi-content-add"></i></a></center>
						<hr style="border-color: """+colors.hexa+""";border-style: solid;line-height: 1px;"><br>
						<div class="row">
							<div class="col s6">
								<div class="card white darken-1">
									<div class="card-content white-text">
										<span class="card-title """+colors.color+"""-text text-darken-2">Alle Seiten</span><br>
										<div class="row">
											<div class="input-field col s12">
												<input style="color:black;" placeholder=\""""+str(checkvalues.refreshall)+"""\" name="refreshall" id="refreshall" type="text">
												<label for="refreshall">Alle Seiten neuladen</label>
											</div>
										</div>
										<div>
											<input type="checkbox" name="refreshallenabled" id="refreshallenabled" """+checkvalues.refreshallenabled+"""/>
											<label for="refreshallenabled">Globales neuladen aktiviert</label>
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
												<input style="color:black;" placeholder=\""""+str(checkvalues.refreshmon)+"""\" name="refreshmon" id="refreshmon" type="text">
												<label for="refreshmon">Monitornjus Frontend neuladen</label>
											</div>
										</div>
										<div>
											<input type="checkbox" name="refreshmonenabled" id="refreshmonenabled" """+checkvalues.refreshmonenabled+"""/>
											<label for="refreshmonenabled">Monitornjus neuladen</label>
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
		<!--<hr style="border-color: """+colors.hexa+""";border-style: solid;line-height: 1px;"><br>
		<div class="row">
			<div class="col s12 m6">
				<div class="card """+colors.color+""" darken-1">
					<div class="card-content white-text">
						<span class="card-title">Willkommen im Admin-Panel!</span>
						<p>Willkommen bei MonitorNjus """+common.version+""".</p>
					</div>
				</div>
			</div>
			<div class="col s12 m6">
				<div class="card """+colors.color+""" darken-1">
					<div class="card-content white-text">
						<span class="card-title">Anleitung:</span>
						<p>In den obigen Feldern kann man zwei Spalten festlegen, die im Frontend nebeneinander angezeigt werden. Dazu muss oben die URL eingetragen werden und die jeweile Spalte per Checkbox aktiviert werden.</p>
					</div>
				</div>
			</div>
			<center><a class="waves-effect waves-light btn-large" href="../bin/index.py">Zum Frontend</a></center>
		</div>-->
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
</html>""" % (common.datum.year)

except Exception as e:
	common.debug(e)
