#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 25.03.2015 (Version 0.6.1)

import cgi, cgitb 

form = cgi.FieldStorage() 
url = form.getvalue('url')

print "Content-Type: text/html"
print
print """
<!DOCTYPE html>
<html>
<head>
<title>MonitorNjus scrollredirect</title>
<meta charset="UTF-8">
<script type="text/javascript" src="js/jquery-2.1.3.min.js"></script>
<script type="text/javascript" src="js/jquery.simplyscroll.js"></script>"""
# <script type="text/javascript">
 
#     function resizeIframe(obj) {
#         obj.style.height = obj.contentWindow.document.body.scrollHeight + 'px';
#     }

#     function initialize() {
#         var frame = document.getElementsByTagName('iframe')[0];
#         if(frame.contentWindow.document.body.scrollHeight > 950)
#         	{
#             window.location.href = "autorollen.py?url="""+url+""""
#         	}
#     }

# </script>
print """
<script type="text/javascript">
function resizeIframe(obj) {
    obj.style.height = obj.contentWindow.document.body.scrollHeight + 'px';
}

var framefenster = document.getElementsByTagName("iFrame");
var auto_resize_timer = window.setInterval("autoresize_frames()", 400);
function autoresize_frames()
	{
	for (var i = 0; i < framefenster.length; ++i)
		{
    	if(framefenster[i].contentWindow.document.body)
    		{
        	var framefenster_size = framefenster[i].contentWindow.document.body.offsetHeight;
            if(document.all && !window.opera)
            	{
            	framefenster_size = framefenster[i].contentWindow.document.body.scrollHeight;
            	}
            framefenster[i].style.height = framefenster_size + 'px';
			if(framefenster_size > 950)
				{
              	window.location.href = "autorollen.py?url="""+url+"""";
				}
        	}
      	}
    }
</script>
</head>
<body onload="autoresize_frames()">
<iframe src=\""""+url+"""\" style="position:absolute; width:100%; height:100%; top:0px; left:0px; margin-left:2px; border-style:none; overflow:hidden" scrolling="no" id="fest" onload="javascript:resizeIframe(this);"></iframe>
</body>"""