#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use, copy,
# modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Beilage zu MonitorNjus, 25.03.2015 (Version 0.6.1)

def replace_b(body):
	end = body\
		.replace("<style type=\"text/css\">","<!--<style>")\
		.replace("<meta http-equiv=\"expires\" content=\"0\">","<meta http-equiv=\"expires\" content=\"0\"><link rel='stylesheet' type='text/css' href='css/vertretung.css'>")\
		.replace("</head>","--></head>")\
		.replace("width=\"14\"","")\
		.replace("width=\"6\"","")\
		.replace("width=\"8\"","")\
		.replace("width=\"22\"","")\
		.replace(">Kla.",">Klasse")\
		.replace(">Rm.",">Raum")\
		.replace("<!-- Info-Stundenplan -->","")\
		.replace("<td align=\"right\"","<td ")\
		.replace("background-color: #0080FF","background-color: #0080FF;color:#fff;")\
		.replace("<title>","<!--<title>")\
		.replace("</title>","</title>--><title>Aktueller Vertretungsplan des JVG Ehingen</title>")\
		.replace('<table class="mon_head">','<!--<table class="mon_head">')\
		.replace('<table class="mon_list" >', '--><table class="mon_list" >')\
		.replace('<font size="3" face="Arial">', '<!--<font size="3" face="Arial">')\
		.replace("</body>","--></body>")
	print "Content-Type: text/html"
	print
	print """
<!DOCTYPE html>"""
	print end

def replace_h(header):
	end = header\
		.replace("<style type=\"text/css\">","<!--<style>")\
		.replace("<meta http-equiv=\"expires\" content=\"0\">","<meta http-equiv=\"expires\" content=\"0\"><link rel='stylesheet' type='text/css' href='css/vertretung.css'>")\
		.replace("</head>","--></head>")\
		.replace("width=\"14\"","")\
		.replace("width=\"6\"","")\
		.replace("width=\"8\"","")\
		.replace("width=\"22\"","")\
		.replace(">Kla.",">Klasse")\
		.replace(">Rm.",">Raum")\
		.replace("<!-- Info-Stundenplan -->","")\
		.replace("<td align=\"right\"","<td ")\
		.replace("background-color: #0080FF","background-color: #0080FF;color:#fff;")\
		.replace("<title>","<!--<title>")\
		.replace("</title>","</title>--><title>Aktueller Vertretungsplan des JVG Ehingen</title>")\
		.replace('<table class="mon_list" >','<!--<table class="mon_list" >')\
		.replace('<table class="mon_head">','<!--<table class="mon_head">')\
		.replace("</body>","--></body>")\
		.replace('<div class="mon_title">', '--><center><div class="mon_title">')
	print "Content-Type: text/html"
	print
	print """
<!DOCTYPE html>"""
	print end

try:
	import cgi, cgitb 

	form = cgi.FieldStorage() 

	nxtdayg = form.getvalue('nxtday')
	actdayg = form.getvalue('actday')
	headerg = form.getvalue('header')
	bodyg = form.getvalue('body')

	actdayarg = str(actdayg)
	nxtdayarg = str(nxtdayg)
	headerarg = str(headerg)
	bodyarg = str(bodyg)

	sync_heute_und_morgen = "sync/heute_und_morgen/"
	actday_file = sync_heute_und_morgen + "subst_001.htm"
	nxtday_file = sync_heute_und_morgen + "subst_002.htm"

	monitornews = 0
	if "1" in nxtdayarg or "10" in nxtdayarg:
		actday = 0
		nxtday = 1
	else:
		actday = 1
		nxtday = 0

	if "10" in nxtdayarg or "10" in actdayarg:
		monitornews = 1

	if "1" in headerarg:
		header = 1
		body = 0
	elif headerg == None:
		body = 1
		header = 0
	elif "1" in bodyarg:
		body = 1
		header = 0
	elif bodyg == None:
		header = 1
		body = 0

	syh = open(sync_heute_und_morgen + "subst_001.htm", "r")
	sync_heute = syh.read()

	sym = open(sync_heute_und_morgen + "subst_002.htm", "r")
	sync_morgen = sym.read()


	if actday == 1 and header == 1:
		replace_h(sync_heute)
	if nxtday == 1 and header == 1:
		replace_h(sync_morgen)
	if actday == 1 and body == 1:
		replace_b(sync_heute)
	if nxtday == 1 and body == 1:
		replace_b(sync_morgen)

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
	<h1>Es ist ein Fehler aufgetreten (vertretung.py)! Seite wird in 10 Sekunden neu geladen.</h1>
	<h3>Details:<br>"""
	print e
	print """
	</h3>
</body>
</html>"""