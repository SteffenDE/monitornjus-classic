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
    print """\
<!DOCTYPE html>
<html>
<head>
<script language="JavaScript1.2">
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
			if(framefenster_size < 950)
				{
              	document.write('<iFrame src=\""""+url+"""\" style="width:100%; height: 100%;" frameborder="0" name="fest" scrolling="no"></iFrame>');
				}
        	}
      	}
    }
</script>
</head>
<body>
<script type="text/javascript">
//Laufrichtung(up,down)
var frame = '<iFrame src=\""""+url+"""\" style="width:100%; height:100%;" frameborder="0" name="links" scrolling="no"></iFrame>'

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