#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 07.05.2015 (Version 0.7.1)

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
<style>
.iframe {
	border: none;
}


.custom {
	width: 100%;
	height: 100%;
	border: none;
}

.custom .simply-scroll-clip {
	width: 100%;
	height: 100%;
	border: none;
}

.simply-scroll-container { 
	position: fixed;
	top:0px;
	left:0px;
	border: none;
}

.simply-scroll-clip { 
	overflow: hidden;
	border: none;
}

.simply-scroll-list li img {
	border: none;
	display: block;
}
</style>
</head>
<body>
<script type="text/javascript">
(function($) {
    $(function() { //on DOM ready
        $("#scroller").simplyScroll({
            customClass: 'custom',
            orientation: 'vertical',
            auto: true,
            autoMode: 'loop',
            frameRate: 60,
            speed: 1,
            startOnLoad: true,
            pauseOnHover: false
        });
    });
})(jQuery);
</script>
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