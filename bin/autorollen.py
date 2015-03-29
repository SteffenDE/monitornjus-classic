#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 25.03.2015 (Version 0.6.1)

try:
	import cgi, cgitb 

	form = cgi.FieldStorage() 
	url = form.getvalue('url')

	print "Content-Type: text/html"
	print
	print """
<!DOCTYPE html>
<html>
<head>
<title>MonitorNjus Autorollen</title>
<meta charset="UTF-8">
<script type="text/javascript" src="js/jquery-2.1.3.min.js"></script>
<script type="text/javascript" src="js/jquery.simplyscroll.js"></script>
<script type="text/javascript">
	 
	function resizeIframe(obj) {
	    obj.style.height = obj.contentWindow.document.body.scrollHeight + 'px';
	}

</script>
<link href="css/loop.css" type="text/css" rel="stylesheet"/>
</head>
<body>
<script type="text/javascript" src="js/scroller.js"></script>
<div id="scroller">
    <iframe src=\""""+url+"""\" style="position:static; width:100%; margin-left:2px; border-style:none; overflow:hidden" scrolling="no" name="links" onload="javascript:resizeIframe(this);"></iframe>
</div>

</body>"""

except Exception, e:
	print "Content-Type: text/html"
	print
	print """<!DOCTYPE html>
<html lang="de">
<head>
	<meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no"/>
    <link href="css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>
    <link href="css/mnews.css" type="text/css" rel="stylesheet" media="screen,projection"/>
    <META HTTP-EQUIV="refresh" CONTENT="10">
</head>
<body>
	<h1>Es ist ein Fehler aufgetreten (autorollen.py)! Seite wird in 10 Sekunden neu geladen.</h1>
	<h3>Details:<br>"""
	print e
	print """
	</h3>
</body>
</html>"""