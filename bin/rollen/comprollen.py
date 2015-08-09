#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Copyright (c) 2015 Steffen Deusch
# Beilage zu MonitorNjus, 09.08.2015 (Version 0.9.2)

try:
	import cgi
	import sys

	form = cgi.FieldStorage() 
	url = form.getfirst('url', None)
	typ = form.getfirst("type", None)

	######### Settings #########

	schritte = 1        # Pixel pro Step
	speed = 15          # Millisekundeb pro Step
	direction = "up"    # up / down

	############################

	print u"Content-Type: text/html;charset=utf-8\n"

	if typ == "redir":
		print u"""\
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>MonitorNjus scrollredirect</title>
	<!-- MonitorNjus -->
	<!-- Copyright (c) Steffen Deusch -->
	<!-- https://github.com/SteffenDE/MonitorNjus -->
	<script type="text/javascript">
	function resizeIframe(obj) {
		obj.style.height = obj.contentWindow.document.body.scrollHeight + 'px';
	}
	var height = window.innerHeight;
	var framefenster = document.getElementsByTagName("iFrame");
	var auto_resize_timer = window.setInterval("autoresize_frames()", 400);
	function autoresize_frames()
		{
		for (var i = 0; i < framefenster.length; ++i)
			{
			if(framefenster[i].contentWindow.document.body)
				{
				var framefenster_size = framefenster[i].contentWindow.document.body.offsetHeight;
				framefenster[i].style.height = framefenster_size + 'px';
				/*document.write(framefenster_size+"<br>")
				document.write(height)*/
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
</head>
<body onload="autoresize_frames()">
	<iframe src=\""""+unicode(url)+"""\" style="visibility: hidden; position:absolute; width:100%; height:100%; top:0px; left:0px; margin-left:2px; border-style:none; overflow:hidden" frameborder="0" scrolling="no" id="fest"></iframe>
</body>"""
		sys.stdout.write("</html>")

	elif typ == "rollen":
		print u"""\
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>MonitorNjus Rollen</title>
	<!-- MonitorNjus -->
	<!-- Copyright (c) Steffen Deusch -->
	<!-- https://github.com/SteffenDE/MonitorNjus -->
	<style>
	.fadeIn {
		opacity:0;
		-webkit-animation:fadeIn ease-in 1;
		-moz-animation:fadeIn ease-in 1;
		-o-animation:fadeIn ease-in 1;
		animation:fadeIn ease-in 1;
		-webkit-animation-fill-mode:forwards;
		-moz-animation-fill-mode:forwards;
		-o-animation-fill-mode:forwards;
		animation-fill-mode:forwards;
	}
	.fadeIn-animation {
		-webkit-animation-duration:0.5s;
		-moz-animation-duration:0.5s;
		-o-animation-duration:0.5s;
		animation-duration:0.5s;
	}
	@-webkit-keyframes fadeIn { from { opacity:0; } to { opacity:1; } }
	@-moz-keyframes fadeIn { from { opacity:0; } to { opacity:1; } }
	@-o-keyframes fadeIn { from { opacity:0; } to { opacity:1; } }
	@keyframes fadeIn { from { opacity:0; } to { opacity:1; } }
	</style>
	<script type="text/javascript">
	function resizeIframe(obj) {
		obj.style.height = obj.contentWindow.document.body.scrollHeight + 'px';
	}
	</script>
</head>
<body class=\"fadeIn fadeIn-animation\">
	<script type="text/javascript">
	var frame = '<iframe src=\""""+unicode(url)+"""\" style="width:100%; height:100%;" frameborder="0" name="links" scrolling="no" onload="javascript:resizeIframe(this);"></iframe>'
	var strDir      ='"""+unicode(direction)+"""';
	var Interval = """+unicode(speed)+""";
	var intRepeat   = 2;
	var strBgc      ='#fff';
	var strTxtc     ='#ffffff';
	var strAlign    ='left';
	var intStep="""+unicode(schritte)+""";
	blnDir=(strDir=='up'||strDir=='down')?true:false;
	strAlign=(blnDir)?'text-align:'+strAlign+';':'';
	var objGo;
	intPos=0;
	strNews=frame;
	for(i=1;i<intRepeat;++i)
		{
		strNews+=frame;
		}
	strTicker='<div style="position:absolute; left:0px; top: 0px; width:100%; height:100%;"><div><div id="ticker"style="position:relative;color:'+strTxtc+';background-color:'+strBgc+';">'+strNews+'</div></div></div>';
	document.write(strTicker);
	function DM_ticken()
	{
		objTicker=document.getElementById('ticker');
		arrDir=new Array();
		arrDir['up']    =new Array(-1,objTicker.offsetHeight,'top');
		arrDir['down']  =new Array(1,objTicker.offsetHeight,'top');
		dblOffset=arrDir[strDir][1]/intRepeat;
	switch(strDir)
		{
		case 'up':
			intPos=(Math.abs(intPos)>dblOffset)?0:intPos;break;
		case 'down':
			intPos=(intPos>0)?-dblOffset:intPos;break;
		}
	objTicker.style[arrDir[strDir][2]]=intPos + "px";
	intPos+=intStep*arrDir[strDir][0];
	}
	objGo=setInterval('DM_ticken()',Interval);
	</script>
</body>"""
		sys.stdout.write("</html>")

	else:
		raise Exception("Falscher oder fehlender Queryparameter: type")

except Exception as e:
	import os
	import imp
	workingdir = os.path.dirname(os.path.realpath(__file__))
	common = imp.load_source('common', workingdir+"/../../common.py")
	common.debug(e)