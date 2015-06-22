#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 18.06.2015 (Version 0.7.5)

try:
	import os
	workingdir = os.getcwd()
	import imp
	if "bin" in workingdir:
		common = imp.load_source('common', workingdir+"/../common.py")
		checktime = imp.load_source('checktime', workingdir+"/../admin/checktime.py")
	else:
		common = imp.load_source('common', workingdir+"/common.py")
		checktime = imp.load_source('checktime', workingdir+"/admin/checktime.py")
	import cgi
	import cgitb
	import getytid

	###########################

	form = cgi.FieldStorage()
	cgitb.enable()
	gseite = form.getvalue('seite')
	gnummer = form.getvalue('nummer')
	rows = common.getrows()
	rand = False

	###########################

	if gseite == "1":
		seite = "1"
		mseite = "Links"
	elif gseite == "2":
		seite = "2"
		mseite = "Rechts"
	else:
		raise Warning("Diese Seite existiert nicht!")

	if gnummer is None:
		x = 0
		while x < rows:
			if checktime.match(common.getinfo("VONBIS", mseite, int(common.minaktiv(mseite))+x),common.datum.now()) == True and common.getinfo("AKTIV", mseite, int(common.minaktiv(mseite))+x) == 1:
				nummer = int(common.minaktiv(mseite))+x
				break
			x += 1
	else:
		nummer = int(gnummer)

	try:
		nummer
	except:
		raise Warning("Es existiert keine aktive Seite oder ein anderer Fehler ist aufgetreten!")
		exit(0)

	###########################

	url = common.getinfo("URL", mseite, int(nummer))
	refresh = common.getinfo("REFRESH", mseite, int(nummer))
	
	###########################

	x = 1
	while x < rows or x == 1:
		if nummer < rows and nummer+x <= rows:
			if common.getinfo("AKTIV", mseite, nummer+x) == 1 and checktime.match(common.getinfo("VONBIS", mseite, nummer+x),common.datum.now()) == True:
				refreshon = True
				nextnummer = nummer + x
				break
			else:
				refreshon = False
				nextnummer = nummer
		else:
			refreshon = True
			z = 0
			while z < rows:
				if checktime.match(common.getinfo("VONBIS", mseite, int(common.minaktiv(mseite))+z),common.datum.now()) == True:
					nextanumma = int(common.minaktiv(mseite))+z
					nextnummer = nextanumma
					break
				else:
					nextnummer = nummer
				z += 1
		x += 1

	###########################

	if common.getinfo("REFRESHAKTIV", mseite, nummer) == 1:
		refreshon = True
	else:
		refreshon = False

	###########################
		
	if refreshon:
		prrefresh = '\
	<meta http-equiv="refresh" content=\"'+str(refresh)+'; URL=contentset.py?seite='+str(seite)+';nummer='+str(nextnummer)+'\">'
	else:
		prrefresh = None

	###########################

	typ = common.checkfiletype(url)

	if typ == "image":
		output = '	<div id="background"></div>'
	elif typ == "video":
		output = '\
	<div class="videocontainer"><video src=\''+url+'\' style="width:100%; height:auto; max-height: 100%;" autoplay="autoplay" loop="loop">Dein Browser unterst&uuml;tzt keine HTML5 Videos...</video></div>'
	elif typ == "pdf":
		output = '\
	<iframe src=\"'+url+'\" style="position:absolute; z-index:9; height:98%; width:98%; border-style:none; overflow:hidden" scrolling="no" frameborder="0"></iframe>'
		rand = True
	elif typ == "youtube":
		output = '\
	<iframe style="position:absolute; height:100%; width:100%; top:0px; left: 0px; border-style:none; overflow:hidden" scrolling="no" frameborder="0" src="//www.youtube.com/embed/'+getytid.video_id(url)+'?rel=0&autoplay=1&loop=1&controls=0&showinfo=0"></iframe>'
		rand = True
	else:
		output = '\
	<iframe src=\"'+url+'\" style="position:absolute; width:100%; height:100%; top:0px; left:0px; border-style:none;" scrolling="no" frameborder="0"></iframe>'
		rand = True

################################ HTML ################################

	print "Content-Type: text/html"
	print
	print """\
<!DOCTYPE html>
<html lang="de">
<head>
	<meta charset="UTF-8">
	<script type="text/javascript" src="js/jquery-2.1.3.min.js"></script>
	<script type="text/javascript">
	$(document).ready(function () {$('#content').css('display', 'none');$('#content').fadeIn(1000);});
	</script>"""
	if prrefresh is not None:
		print prrefresh
	else:
		pass
	print "\
	<title>MonitorNjus</title>"
	if typ == "video":
		style = """\
	.videocontainer 
	{
		position:absolute;
		height:100%;
		width:100%;
		overflow: hidden;
		top: 0px;
	}
	.videocontainer video 
	{
		min-width: 100%;
		min-height: 100%;
	}"""
	elif typ == "image":
		style = """\
	#background {
		position: absolute;
		min-height:100%;
		width: 100%;
		height: auto;
		top: 0;
		left: 0;
		background: url("""+url+""") no-repeat center center;
		background-size: contain;         /* around images */
	}"""
	else:
		style = ""
	if rand:
		print """\
	<style>
	iframe {
		padding-left: """+common.addpx(common.getinfo("MARGINLEFT", mseite, nummer))+""";
		padding-right: """+common.addpx(common.getinfo("MARGINRIGHT", mseite, nummer))+""";
		padding-top: """+common.addpx(common.getinfo("MARGINTOP", mseite, nummer))+""";
		padding-bottom: """+common.addpx(common.getinfo("MARGINBOTTOM", mseite, nummer))+""";
		box-sizing: border-box;
	}"""
	else:
		print "	<style>"
	print style
	print "\
	</style>\n\
</head>"
	#print checktime.match(common.getinfo("VONBIS", mseite, int(common.minaktiv(mseite))),common.datum.now())
	#print nextanumma
	#print nextnummer
	print "\
<body id=\"content\">"
	#print common.getinfo("VONBIS", mseite, nummer)
	#print checktime.match(common.getinfo("VONBIS", mseite, nummer),common.datum.now())
	print output
	print "\
</body>\n\
</html>"

except Exception as e:
	common.debug(e)