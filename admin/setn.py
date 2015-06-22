#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 18.06.2015 (Version 0.7.5)

try:
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
	#cgitb.enable()

	########################################################################

	referer = form.getfirst('referer', None)

	def updateurl_refresh(Name, GETNAME, Seite, Nummer, widgname):
		if "index" in referer:
			gval = form.getfirst(Name, None)
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
			gval = form.getfirst(Name, None)
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
			raise Warning("Function updateurl_refresh: This referer does not exist.")

	def updateaktiv(Name, GETNAME, Seite, Nummer, widgname):
		if "index" in referer:
			if form.getfirst(Name, None):
				val_flag = 1
			else:
				val_flag = 0
			if val_flag is not None:
				if val_flag == common.getinfo(GETNAME, Seite, Nummer):
					pass
				else:
					common.writeinfo(Seite, Nummer, GETNAME, int(val_flag))
		elif "widgets" in referer:
			if form.getfirst(Name, None):
				val_flag = 1
			else:
				val_flag = 0
			if val_flag is not None:
				if val_flag == common.getwidgetinfo(widgname, GETNAME):
					pass
				else:
					common.writewidgetinfo(widgname, GETNAME, int(val_flag))
		else:
			raise Warning("Function updateaktiv: This referer does not exist.")

	def update_align(Name, GETNAME, widgname):
		if "widgets" in referer:
			if form.getfirst(Name, None):
				val = form.getfirst(Name, None)
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
		else:
			raise Warning("Function update_align: This referer is not allowed.")

	def updatetime(Seite, Nummer):
		if "index" in referer:
			uhrzeit = form.getfirst("uhrzeit-"+Seite+"-"+str(Nummer), None)
			wochentag = form.getfirst("wochentag-"+Seite+"-"+str(Nummer), None)
			tag = form.getfirst("tag-"+Seite+"-"+str(Nummer), None)
			monat = form.getfirst("monat-"+Seite+"-"+str(Nummer), None)
			if uhrzeit is None and wochentag is None and tag is None and monat is None:
				pass
			else:
				if uhrzeit is None:
					uhrzeit = "*"
				if wochentag is None:
					wochentag = "*"
				if tag is None:
					tag = "*"
				if monat is None:
					monat = "*"
				common.writeinfo(Seite, Nummer, "VONBIS", uhrzeit+"|"+wochentag+"|"+tag+"|"+monat)
		else:
			raise Warning("Function updatetime: This referer is not allowed.")

	if "index" in referer:
		refresh = "<meta http-equiv=\"refresh\" content=\"0; URL=../admin/index.py\">"

		x = 1
		while x <= common.getrows():
			if str(x) in common.getallrows():
				if "url1-"+str(x) in form: updateurl_refresh("url1-"+str(x), "URL", "Links", x, "")
				if "url2-"+str(x) in form: updateurl_refresh("url2-"+str(x), "URL", "Rechts", x, "")
				if "refresh1-"+str(x) in form: updateurl_refresh("refresh1-"+str(x), "REFRESH", "Links", x, "")
				if "refresh2-"+str(x) in form: updateurl_refresh("refresh2-"+str(x), "REFRESH", "Rechts", x, "")
				if "marginleft-Links-"+str(x) in form: updateurl_refresh("marginleft-Links-"+str(x), "MARGINLEFT", "Links", x, "")
				if "marginright-Links-"+str(x) in form: updateurl_refresh("marginright-Links-"+str(x), "MARGINRIGHT", "Links", x, "")
				if "margintop-Links-"+str(x) in form: updateurl_refresh("margintop-Links-"+str(x), "MARGINTOP", "Links", x, "")
				if "marginbottom-Links-"+str(x) in form: updateurl_refresh("marginbottom-Links-"+str(x), "MARGINBOTTOM", "Links", x, "")
				if "marginleft-Rechts-"+str(x) in form: updateurl_refresh("marginleft-Rechts-"+str(x), "MARGINLEFT", "Rechts", x, "")
				if "marginright-Rechts-"+str(x) in form: updateurl_refresh("marginright-Rechts-"+str(x), "MARGINRIGHT", "Rechts", x, "")
				if "margintop-Rechts-"+str(x) in form: updateurl_refresh("margintop-Rechts-"+str(x), "MARGINTOP", "Rechts", x, "")
				if "marginbottom-Rechts-"+str(x) in form: updateurl_refresh("marginbottom-Rechts-"+str(x), "MARGINBOTTOM", "Rechts", x, "")
				updateaktiv("leftenabled-"+str(x), "AKTIV", "Links", x, "")
				updateaktiv("rightenabled-"+str(x), "AKTIV", "Rechts", x, "")
				updateaktiv("refreshleftenabled-"+str(x), "REFRESHAKTIV", "Links", x, "")
				updateaktiv("refreshrightenabled-"+str(x), "REFRESHAKTIV", "Rechts", x, "")
				updatetime("Links", x)
				updatetime("Rechts", x)
			x += 1

		if "refreshall" in form: updateurl_refresh("refreshall", "REFRESH", "global", 0, "")
		if "refreshmon" in form: updateurl_refresh("refreshmon", "REFRESH", "globalmon", 0, "")
		updateaktiv("refreshallenabled", "REFRESHAKTIV", "global", 0, "")
		updateaktiv("refreshmonenabled", "REFRESHAKTIV", "globalmon", 0, "")

	elif "widgets" in referer:
		refresh = "<meta http-equiv=\"refresh\" content=\"0; URL=../admin/widgets.py\">"

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

	elif "row" in referer:
		refresh = "<meta http-equiv=\"refresh\" content=\"0; URL=../admin/index.py\">"
		cnum = form.getfirst("createnum", None)
		dnum = form.getfirst("delnum", None)
		if cnum is not None:
			num = int(cnum)
			common.createrow(num)
		else:
			pass
		if dnum is not None:
			num = int(dnum)
			common.delrow(num)
		else:
			pass

	else:
		refresh = ""

	print """\
Content-Type: text/html

<!DOCTYPE html>
<html lang="de">
<head>"""
	#for item in form:
		#print item+": "+form[item].value+"<br>"
	print refresh
	print """\
</head>
<body>
</body>
</html>"""

except Exception as e:
	common.debug(e)