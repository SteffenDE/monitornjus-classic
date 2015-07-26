#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 22.07.2015 (Version 0.8.4)

import sys
reload(sys)
sys.setdefaultencoding('utf8')

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
		.replace('<font size="3" face="Arial"', '<!--<font size="3" face="Arial"')\
		.replace("</body>","--></body>")
	print "Content-Type: text/html\n"
	sys.stdout.write(end)

def replace_h(header):
	end = header\
		.replace("<style type=\"text/css\">","<!--<style>")\
		.replace("<meta http-equiv=\"expires\" content=\"0\">","<meta http-equiv=\"expires\" content=\"0\">\n<link rel='stylesheet' type='text/css' href='css/vertretung.css'>")\
		.replace("</head>","--></head>")\
		.replace("<!-- Info-Stundenplan -->","")\
		.replace('<table class="mon_list" >','<!--<table class="mon_list" >')\
		.replace('<table class="mon_head">','<!--<table class="mon_head">')\
		.replace("</body>","--></body>")\
		.replace('<div class="mon_title">', '--><center><div class="mon_title">')
	print "Content-Type: text/html\n"
	sys.stdout.write(end)

try:
	import cgi
	#import cgitb; cgitb.enable()

	form = cgi.FieldStorage() 

	nxtday = int(form.getfirst('nxtday', "0"))
	actday = int(form.getfirst('actday', "0"))
	header = int(form.getfirst('header', "0"))
	body = int(form.getfirst('body', "1"))

	if actday and header:
		syh = open(path + name_heute, "r")
		replace_h(syh.read())
	elif nxtday and header:
		sym = open(path + name_morgen, "r")
		replace_h(sym.read())
	elif actday and body:
		syh = open(path + name_heute, "r")
		replace_b(syh.read())
	elif nxtday and body:
		sym = open(path + name_morgen, "r")
		replace_b(sym.read())
	else:
		raise Warning("No arguments passed!")

except Exception as e:
	if body:
		import os
		import imp
		workingdir = os.path.dirname(os.path.realpath(__file__))
		common = imp.load_source('common', workingdir+"/../common.py")
		common.debug(e)
	else:
		print "Content-Type: text/html\n\n"