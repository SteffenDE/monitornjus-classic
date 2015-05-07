#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 07.05.2015 (Version 0.7.1)

import cgi, cgitb
import os
import imp
workingdir = os.getcwd()
if "admin" in workingdir:
    common = imp.load_source('common', workingdir+"/../common.py")
else:
    common = imp.load_source('common', workingdir+"/common.py")

common.authenticated()

########################################################################

form = cgi.FieldStorage() 
cgitb.enable()

########################################################################

referer = form.getvalue('referer')

def updateurl_refresh(Name, GETNAME, Seite, Nummer, widgname):
  if "index" in referer:
    gval = form.getvalue(Name)
    if gval is not None:
      val = gval
    else:
      val = None
    if val is not None:
      if val == common.getinfo(GETNAME, Seite, Nummer):
        pass
      else:
        if str(gval).isdigit():
          common.writeinfo(Seite, Nummer, GETNAME, int(val))
        else:
          common.writeinfo(Seite, Nummer, GETNAME, str(val))
  elif "widgets" in referer:
    gval = form.getvalue(Name)
    if gval is not None:
      val = gval
    else:
      val = None
    if val is not None:
      if val == common.getwidgetinfo(widgname, GETNAME):
        pass
      else:
        if str(gval).isdigit():
          common.writewidgetinfo(widgname, GETNAME, int(val))
        else:
          common.writewidgetinfo(widgname, GETNAME, str(val))
  else:
    pass

def updateaktiv(Name, GETNAME, Seite, Nummer, widgname):
  if "index" in referer:
    if form.getvalue(Name):
      val_flag = 1
    else:
      val_flag = 0
    if val_flag is not None:
      if val_flag == common.getinfo(GETNAME, Seite, Nummer):
        pass
      else:
        common.writeinfo(Seite, Nummer, GETNAME, int(val_flag))
  elif "widgets" in referer:
    if form.getvalue(Name):
      val_flag = 1
    else:
      val_flag = 0
    if val_flag is not None:
      if val_flag == common.getwidgetinfo(widgname, GETNAME):
        pass
      else:
        common.writewidgetinfo(widgname, GETNAME, int(val_flag))
  else:
    pass

def update_align(Name, GETNAME, widgname):
  if "widgets" in referer:
    if form.getvalue(Name):
      val = form.getvalue(Name)
    else:
      val = None
    if val is not None:
      if str(val).isdigit():
        if val == common.getwidgetinfo(widgname, GETNAME):
          pass
        else:
          common.writewidgetinfo(widgname, GETNAME, int(val))
      else:
        if str(val) == common.getwidgetinfo(widgname, GETNAME):
          pass
        else:
          common.writewidgetinfo(widgname, GETNAME, str(val))

def updatetime(Seite, Nummer):
  if "index" in referer:
    uhrzeit = form.getvalue("uhrzeit-"+Seite+"-"+str(Nummer))
    wochentag = form.getvalue("wochentag-"+Seite+"-"+str(Nummer))
    tag = form.getvalue("tag-"+Seite+"-"+str(Nummer))
    monat = form.getvalue("monat-"+Seite+"-"+str(Nummer))
    if uhrzeit is None and wochentag is None and tag is None and monat is None:
      pass
    elif uhrzeit is not None or wochentag is not None or tag is not None or monat is not None:
      if uhrzeit is None:
        uhrzeit = "*"
      if wochentag is None:
        wochentag = "*"
      if tag is None:
        tag = "*"
      if monat is None:
        monat = "*"
      common.writeinfo(Seite, Nummer, "VONBIS", uhrzeit+"|"+wochentag+"|"+tag+"|"+monat)

if "index" in referer:
  x = 1
  while x <= common.getrows():
    if str(x) in common.getallrows():
      updateurl_refresh("url1-"+str(x), "URL", "Links", x, "")
      updateurl_refresh("url2-"+str(x), "URL", "Rechts", x, "")
      updateurl_refresh("refresh1-"+str(x), "REFRESH", "Links", x, "")
      updateurl_refresh("refresh2-"+str(x), "REFRESH", "Rechts", x, "")
      updateaktiv("leftenabled-"+str(x), "AKTIV", "Links", x, "")
      updateaktiv("rightenabled-"+str(x), "AKTIV", "Rechts", x, "")
      updateaktiv("refreshleftenabled-"+str(x), "REFRESHAKTIV", "Links", x, "")
      updateaktiv("refreshrightenabled-"+str(x), "REFRESHAKTIV", "Rechts", x, "")
      updatetime("Links", x)
      updatetime("Rechts", x)
      updateaktiv("vonbisaktivl-"+str(x), "VONBISAKTIV", "Links", x, "")
      updateaktiv("vonbisaktivr-"+str(x), "VONBISAKTIV", "Rechts", x, "")
    x = x + 1

  updateurl_refresh("refreshall", "REFRESH", "global", 0, "")
  updateurl_refresh("refreshmon", "REFRESH", "globalmon", 0, "")

  updateaktiv("refreshallenabled", "REFRESHAKTIV", "global", 0, "")
  updateaktiv("refreshmonenabled", "REFRESHAKTIV", "globalmon", 0, "")


elif "widgets" in referer:
  updateurl_refresh("uhrlink", "URL", "", 0, "Uhr")
  updateurl_refresh("logolink", "URL", "", 0, "Logo")
  updateurl_refresh("widgetlink", "URL", "", 0, "Freies-Widget")

  updateaktiv("adminlinkaktiv", "AKTIV", "", 0, "Admin-Link")
  updateaktiv("uhraktiv", "AKTIV", "", 0, "Uhr")
  updateaktiv("logoaktiv", "AKTIV", "", 0, "Logo")
  updateaktiv("widgetaktiv", "AKTIV", "", 0, "Freies-Widget")

  update_align("dropdown_adminlink_valign", "valign", "Admin-Link")
  update_align("dropdown_adminlink_vmargin", "vmargin", "Admin-Link")
  update_align("adminlinkalign", "align", "Admin-Link")
  update_align("adminlinkmargin", "margin", "Admin-Link")

  update_align("dropdown_uhr_valign", "valign", "Uhr")
  update_align("dropdown_uhr_vmargin", "vmargin", "Uhr")
  update_align("uhralign", "align", "Uhr")
  update_align("uhrmargin", "margin", "Uhr")
  update_align("uhrwidth", "width", "Uhr")
  update_align("uhrheight", "height", "Uhr")

  update_align("dropdown_logo_valign", "valign", "Logo")
  update_align("dropdown_logo_vmargin", "vmargin", "Logo")
  update_align("logoalign", "align", "Logo")
  update_align("logomargin", "margin", "Logo")
  update_align("logowidth", "width", "Logo")
  update_align("logoheight", "height", "Logo")

  update_align("dropdown_widget_valign", "valign", "Freies-Widget")
  update_align("dropdown_widget_vmargin", "vmargin", "Freies-Widget")
  update_align("widgetalign", "align", "Freies-Widget")
  update_align("widgetmargin", "margin", "Freies-Widget")
  update_align("widgetwidth", "width", "Freies-Widget")
  update_align("widgetheight", "height", "Freies-Widget")

if "row" in referer:
  if form.getvalue("createrow") is not None:
    createrow = 1
  else:
    createrow = 0
  cnum = form.getvalue("createnum")
  if createrow is not None and cnum is not None:
    num = int(cnum)
  else:
    num = None
  if num is not None:
    common.createrow(num)
  else:
    pass
  if form.getvalue("delrow") is not None:
    delrow = 1
  else:
    delrow = None
  dnum = form.getvalue("delnum")
  if delrow is not None and dnum is not None:
    num = int(dnum)
  else:
    num = None
  if num is not None:
    common.delrow(num)
  else:
    pass
  refresh = "<meta http-equiv=\"refresh\" content=\"0; URL=../admin/index.py\">"
else:
  pass

if "index" in referer:
  refresh = "<meta http-equiv=\"refresh\" content=\"0; URL=../admin/index.py\">"
elif "widgets" in referer:
  refresh = "<meta http-equiv=\"refresh\" content=\"0; URL=../admin/widgets.py\">"

print "Content-Type: text/html"
print
print """
<!DOCTYPE html>
<html lang="de">
<head>
"""+refresh+"""
</head>
<body>
</body>
</html>"""
