#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 07.05.2015 (Version 0.7.1)

try:
    import os
    workingdir = os.getcwd()
    import imp
    if "bin" in workingdir:
        common = imp.load_source('common', workingdir+"/../common.py")
        checktime = imp.load_source('checktime', workingdir+"/../admin/checktime.py")
    else:
        common = imp.load_source('common', workingdir+"/common.py")
        checktime = imp.load_source('checktime', workingdir+"/admin/checktime.py")

    rows = common.getrows()

    timeL = False
    timeR = False
    x = 1
    while x <= rows:
        if checktime.match(common.getinfo("VONBIS", "Links", x),common.datum.now()) == True and common.getinfo("AKTIV", "Links", x) == 1:
            timeL = True
        if checktime.match(common.getinfo("VONBIS", "Rechts", x),common.datum.now()) == True and common.getinfo("AKTIV", "Rechts", x) == 1:
            timeR = True
        else:
            pass
        if timeL == True and timeR == True:
            break
        x = x + 1

    geteilt = False
    if "1" in common.getgeteilt("Links") and "1" in common.getgeteilt("Rechts") and timeL == True and timeR == True:
        geteilt = True

    if geteilt == True:
        disp = """
    <frameset frameborder="0" rows="*,0">
        <frameset frameborder="0" cols="50,50">
            <frame scrolling="no" src="contentset.py?seite=1" name="links" />
            <frame scrolling="no" src="contentset.py?seite=2" name="rechts" />
      </frameset> 
    </frameset>
    <noframes>
    </noframes>"""
    elif "1" in common.getgeteilt("Links") and "0" in common.getgeteilt("Rechts") and timeL == True:
        disp = """
    <frameset frameborder="0" rows="*,0">
        <frame scrolling="no" src="contentset.py?seite=1" name="links" />
    </frameset>"""
    elif "1" in common.getgeteilt("Rechts") and "0" in common.getgeteilt("Links") and timeR == True:
        disp = """
    <frameset frameborder="0" rows="*,0">
        <frame scrolling="no" src="contentset.py?seite=2" name="rechts" />
    </frameset>"""
    elif "1" in common.getgeteilt("Links") and "1" in common.getgeteilt("Rechts") and timeL == True:
        disp = """
    <frameset frameborder="0" rows="*,0">
        <frame scrolling="no" src="contentset.py?seite=1" name="links" />
    </frameset>"""
    elif "1" in common.getgeteilt("Rechts") and "1" in common.getgeteilt("Links") and timeR == True:
        disp = """
    <frameset frameborder="0" rows="*,0">
        <frame scrolling="no" src="contentset.py?seite=2" name="rechts" />
    </frameset>"""
    else:
        disp = """
    <div class="row">
        <div class="col s12">
            <h1>Konfigurationsfehler.</h1>
        </div>
    </div>"""

    print "Content-Type: text/html"
    if common.getinfo("REFRESHAKTIV", "global", 0) == 1:
        refresh = "    <META HTTP-EQUIV=\"refresh\" CONTENT=\""+str(common.getinfo("REFRESH", "global", 0))+"\">"
    else:
        refresh = ""
    print
    print """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no"/>
    <link href="css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>"""
    print refresh
    print """
    <title>MonitorNjus</title>
</head>"""
    #print timeL
    #print timeR
    #print geteilt
    print disp
    print """
</html>"""

except Exception as e:
    common.debug(e)