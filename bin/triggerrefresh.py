#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 14.09.2015 (Version 0.9.3)

print u"Content-type: text/event-stream"
print u"Cache-Control: no-cache\n"

import os
workingdir = os.path.dirname(os.path.realpath(__file__))
import sys
import time

ttime = 0

while True:
	datei = open(workingdir+'/refresh', 'r')
	content = datei.read()
	datei.close()

	if int(content) == 1:
		print(u"data: reload\n\n")
		sys.stdout.flush()
		time.sleep(4)
		datei = open(workingdir+"/refresh", "w")
		datei.write("0")
		datei.close()
		break
	elif ttime >= 3600:
		break
	else:
		time.sleep(3)

	ttime += 3
print("data: none\n\n")