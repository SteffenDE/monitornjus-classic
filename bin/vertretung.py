#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 14.09.2015 (Version 0.9.3)

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

######### Settings #########

path = "sync/heute_und_morgen/"
name_heute = "subst_001.htm"
name_morgen = "subst_002.htm"

############################

actday_file = path + name_heute
nxtday_file = path + name_morgen

def replace_b(body):
	end = body\
		.replace("<style type=\"text/css\">","<!--<style>")\
		.replace("<meta http-equiv=\"expires\" content=\"0\">","<meta http-equiv=\"expires\" content=\"0\"><link rel='stylesheet' type='text/css' href='css/vertretung.css'>")\
		.replace("</head>","--></head>")\
		.replace("<!-- Info-Stundenplan -->","")\
		.replace('<table class="mon_head">','<!--<table class="mon_head">')\
		.replace('<table class="mon_list" >', '--><table class="mon_list" >')\
		.replace('<p>\r\n<font size="3" face="Arial"', '<!--<font size="3" face="Arial"')\
		.replace('<font size="3" face="Arial"','<!--<font size="3" face="Arial"')\
		.replace("</body>","--></body>")\
		.replace("iso-8859-1","utf-8")
	if '<th class="list" align="center">(Lehrer)</th>' in body:
		end = end\
			.replace('<th class="list" align="center">Klasse(n)</th>', '<th class="list" align="center">Kl.</th>')\
			.replace('<th class="list" align="center">Vertreter</th>', '<th class="list" align="center">Vertr.</th>')
	elif '<tr class="list"><td class="list" align="center" >Keine Vertretungen</td></tr>' in body:
		end = end.replace('Keine Vertretungen','<h2 style="color: #494949;">Keine Vertretungen</h2>')
	try:
		return unicode(end).encode("utf-8")
	except:
		return unicode(end.decode("iso-8859-1")).encode("utf-8")

def replace_h(header):
	end = header\
		.replace("<style type=\"text/css\">","<!--<style>")\
		.replace("<meta http-equiv=\"expires\" content=\"0\">","<meta http-equiv=\"expires\" content=\"0\">\n<link rel='stylesheet' type='text/css' href='css/vertretung.css'>")\
		.replace("</head>","--></head>")\
		.replace("<!-- Info-Stundenplan -->","")\
		.replace('<table class="mon_list" >','<!--<table class="mon_list" >')\
		.replace('<table class="mon_head">','<!--<table class="mon_head">')\
		.replace("</body>","--></body>")\
		.replace('<div class="mon_title">', '--><center><div class="mon_title">')\
		.replace("iso-8859-1","utf-8")
	try:
		return unicode(end).encode("utf-8")
	except:
		return unicode(end.decode("iso-8859-1")).encode("utf-8")

try:
	import cgi
	#import cgitb; cgitb.enable()

	form = cgi.FieldStorage() 

	nxtday = int(form.getfirst('nxtday', "0"))
	actday = int(form.getfirst('actday', "0"))
	header = int(form.getfirst('header', "0"))
	body = int(form.getfirst('body', "1"))

	httpheader = u"Content-Type: text/html;charset=utf-8\n"

	if actday and header:
		syh = open(path + name_heute, "r")
		print httpheader
		print replace_h(syh.read())
	elif nxtday and header:
		sym = open(path + name_morgen, "r")
		print httpheader
		print replace_h(sym.read())
	elif actday and body:
		syh = open(path + name_heute, "r")
		print httpheader
		print replace_b(syh.read())
	elif nxtday and body:
		sym = open(path + name_morgen, "r")
		print httpheader
		print replace_b(sym.read())
	else:
		raise Warning("No arguments passed!")

except Exception as e:
	if not header:
		import os
		workingdir = os.path.dirname(os.path.realpath(__file__))
		import sys
		reload(sys)
		sys.path.append(workingdir+"/../")
		sys.setdefaultencoding('utf-8')
		from modules import common
		common.debug(e)
	else:
		print httpheader