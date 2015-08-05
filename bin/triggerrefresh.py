#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 05.08.2015 (Version 0.9.1)

print u"Content-type: text/event-stream"
print u"Cache-Control: no-cache"
print

import datetime
import os
import time

workingdir = os.path.dirname(os.path.realpath(__file__))

datei = open(workingdir+'/refresh', 'r')
content = datei.read()
datei.close()

if int(content) == 1:
	print(u"data: reload\n\n")
	time.sleep(4)
	datei = open(workingdir+"/refresh", "w")
	datei.write("0")
	datei.close()
else:
	print(u"data: none\n\n")