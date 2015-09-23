#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjusMP, 14.09.2015 (Version 0.9.3)

try:
	import cgi
	form = cgi.FieldStorage()
	url = form.getfirst('url', None)
	typ = form.getfirst("type", None)

	############################

	if typ == "redir":
		out = """\
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>MonitorNjus scrollredirect</title>
	<!-- MonitorNjus -->
	<!-- Copyright (c) Steffen Deusch -->
	<!-- https://github.com/SteffenDE/MonitorNjus -->
	<script src="../js/jquery-2.1.4.min.js"></script>
	<script type="text/javascript">
	function resizeIframe(obj) {
		obj.style.height = obj.contentWindow.document.body.scrollHeight + 'px';
	}
	</script>
</head>
<body>
	<iframe src=\""""+unicode(url)+"""\" style="visibility: hidden; position:absolute; width:100%; height:100%; top:0px; left:0px; margin-left:2px; border-style:none; overflow:hidden" frameborder="0" scrolling="no" id="fest"></iframe>
	<script>
	var framefenster = document.getElementsByTagName("iFrame");
	var auto_resize_timer = window.setInterval("autoresize_frames()", 400);
	function autoresize_frames()
		{
		for (var i = 0; i < framefenster.length; ++i)
			{
			if(framefenster[i].contentWindow.document.body)
				{
				var framefenster_size = framefenster[i].contentWindow.document.body.scrollHeight;
				/*var framefenster_size = framefenster[i].contentWindow.document.body.offsetHeight;*/
				framefenster[i].style.height = framefenster_size + 'px';
				var height = window.innerHeight;
				if(framefenster_size <= height)
					{
					framefenster[i].style.visibility = "visible"
					}
				else {
					window.location.href = \"comprollen.py?type=rollen&url="""+unicode(url)+"""\";
				}
				}
			}
		}
	</script>
</body>
</html>"""

	elif typ == "rollen":
		out = """\
<!DOCTYPE html>
<html>
<head>
<title>MonitorNjus Autorollen</title>
<meta charset="UTF-8">
<script type="text/javascript" src="../js/jquery-2.1.4.min.js"></script>
<script type="text/javascript" src="../js/jquery.simplyscroll.js"></script>
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

</body>
</html>"""

	else:
		raise Exception("Falscher oder fehlender Queryparameter: type")

	########### Ausgabe ###########
	print("Content-type: text/html; charset: utf-8\n\n")
	print(unicode(out))

except Exception as e:
	import os
	workingdir = os.path.dirname(os.path.realpath(__file__))
	import imp
	modulesdir = workingdir+"/../../modules"
	common = imp.load_source("common", modulesdir+"/common.py")
	common.debug(e)