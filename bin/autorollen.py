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

except Exception as e:
	import os
	workingdir = os.getcwd()
	import imp
	if "bin" in workingdir:
		common = imp.load_source('common', workingdir+"/../common.py")
		checktime = imp.load_source('checktime', workingdir+"/../admin/checktime.py")
	else:
		common = imp.load_source('common', workingdir+"/common.py")
		checktime = imp.load_source('checktime', workingdir+"/admin/checktime.py")
	common.debug(e)