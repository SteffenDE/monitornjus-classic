#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Copyright (c) 2015 Steffen Deusch
# Beilage zu MonitorNjus, 02.06.2015 (Version 0.7.4)

try:
    import cgi, cgitb 
    import os

    form = cgi.FieldStorage() 
    url = form.getvalue('url')
    typ = form.getvalue("type")

    print "Content-Type: text/html"
    print

    if typ == "redir":
        print """\
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
        print """\
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
              	window.location.href = \""""+os.environ["SCRIPT_NAME"]+"?type=rollen&url="""+url+"""\";
				}
            else {
                framefenster[i].style.display = "block"
            }
        	}
      	}
    }
</script>
</head>
<body onload="autoresize_frames()">
<iframe src=\""""+url+"""\" style="display: none; position:absolute; width:100%; height:100%; top:0px; left:0px; margin-left:2px; border-style:none; overflow:hidden" scrolling="no" id="fest" onload="javascript:resizeIframe(this);"></iframe>
</body>"""

    elif typ == "rollen":
        print """\
<!DOCTYPE html>
<html>
<head>
<script type="text/javascript" src="../js/jquery-2.1.3.min.js"></script>
<script type="text/javascript">
    $(document).ready(function () {$('#content').css('display', 'none');$('#content').fadeIn(1000);});
</script>
<script>
    function resizeIframe(obj) {
        obj.style.height = obj.contentWindow.document.body.scrollHeight + 'px';
    }
</script>
"""
# <script language="JavaScript1.2">
# var framefenster = document.getElementsByTagName("iFrame");
# var auto_resize_timer = window.setInterval("autoresize_frames()", 400);
# function autoresize_frames()
#     {
#     for (var i = 0; i < framefenster.length; ++i)
#         {
#         if(framefenster[i].contentWindow.document.body)
#             {
#             var framefenster_size = framefenster[i].contentWindow.document.body.offsetHeight;
#             if(document.all && !window.opera)
#                 {
#                 framefenster_size = framefenster[i].contentWindow.document.body.scrollHeight;
#                 }
#             framefenster[i].style.height = framefenster_size + 'px';
#             }
#         }
#     }
# </script>
        print """\
</head>
<body onload="autoresize_frames()">
<script type="text/javascript">
//Laufrichtung(up,down)
var frame = '<iframe src=\""""+url+"""\" style="width:100%; height:100%;" frameborder="0" name="links" scrolling="no" onload="javascript:resizeIframe(this);"></iframe>'
var strDir      ='up';
    //Interval in ms
var Interval = 20;
    //Falls Leeraum zwischen News...hier Wert erhoehen...minimum:1
var intRepeat   = 2;
    //Background-color
var strBgc      ='#fff';
    //Text-color
var strTxtc     ='#ffffff';
    //Textausrichtung
var strAlign    ='left';
    //Schritt pro Durchlauf(px)
var intStep=1;
/* * * * * * * * * * * * * * * * * * D E R  T I C K E R * * * * * * * * * * * * * * * * * * * * * */
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
</body></html>"""

    else:
        raise Exception("Falscher oder fehlender Queryparameter: type")

except Exception as e:
    import os
    workingdir = os.getcwd()
    print workingdir
    import imp
    if "rollen" in workingdir:
        common = imp.load_source('common', workingdir+"/../../common.py")
    else:
        common = imp.load_source('common', workingdir+"/../common.py")
    common.debug(e)
