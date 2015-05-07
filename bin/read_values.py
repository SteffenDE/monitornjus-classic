#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 07.05.2015 (Version 0.7.1)

import os
workingdir = os.getcwd()
import imp
if "bin" in workingdir:
    common = imp.load_source('common', workingdir+"/../common.py")
else:
    common = imp.load_source('common', workingdir+"/common.py")

read_refreshallenabled = common.getinfo("REFRESHAKTIV", "global", 0)
read_refreshmonenabled = common.getinfo("REFRESHAKTIV", "globalmon", 0)

read_refreshall = common.getinfo("REFRESH", "global", 0)
read_refreshmon = common.getinfo("REFRESH", "globalmon", 0)

read_adminlinkaktiv = common.getwidgetinfo("Admin-Link", "AKTIV")
read_adminlinkvalign = common.getwidgetinfo("Admin-Link", "valign")
read_adminlinkalign = common.getwidgetinfo("Admin-Link", "align")
read_adminlinkvmargin = common.getwidgetinfo("Admin-Link", "vmargin")
read_adminlinkmargin = common.getwidgetinfo("Admin-Link", "margin")

read_uhraktiv = common.getwidgetinfo("Uhr", "AKTIV")
read_uhrvalign = common.getwidgetinfo("Uhr", "valign")
read_uhralign = common.getwidgetinfo("Uhr", "align")
read_uhrvmargin = common.getwidgetinfo("Uhr", "vmargin")
read_uhrmargin = common.getwidgetinfo("Uhr", "margin")
read_uhrlink = common.getwidgetinfo("Uhr", "URL")
read_uhrheight = common.getwidgetinfo("Uhr", "height")
read_uhrwidth = common.getwidgetinfo("Uhr", "width")

read_logoaktiv = common.getwidgetinfo("Logo", "AKTIV")
read_logovalign = common.getwidgetinfo("Logo", "valign")
read_logoalign = common.getwidgetinfo("Logo", "align")
read_logovmargin = common.getwidgetinfo("Logo", "vmargin")
read_logomargin = common.getwidgetinfo("Logo", "margin")
read_logolink = common.getwidgetinfo("Logo", "URL")
read_logoheight = common.getwidgetinfo("Logo", "height")
read_logowidth = common.getwidgetinfo("Logo", "width")

read_widgetaktiv = common.getwidgetinfo("Freies-Widget", "AKTIV")
read_widgetvalign = common.getwidgetinfo("Freies-Widget", "valign")
read_widgetalign = common.getwidgetinfo("Freies-Widget", "align")
read_widgetvmargin = common.getwidgetinfo("Freies-Widget", "vmargin")
read_widgetmargin = common.getwidgetinfo("Freies-Widget", "margin")
read_widgetlink = common.getwidgetinfo("Freies-Widget", "URL")
read_widgetheight = common.getwidgetinfo("Freies-Widget", "height")
read_widgetwidth = common.getwidgetinfo("Freies-Widget", "width")