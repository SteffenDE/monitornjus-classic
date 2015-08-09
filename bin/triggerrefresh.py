#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 09.08.2015 (Version 0.9.2)

print u"Content-type: text/event-stream"
print u"Cache-Control: no-cache"
print

import datetime
import os
import time
import imp
import sys

workingdir = os.path.dirname(os.path.realpath(__file__))
common = imp.load_source("common", workingdir+"/../common.py")

while True:
	content = int(common.readsettings("REFRESH"))

	if int(content) == 1:
		print(u"data: reload\n\n")
		sys.stdout.flush()
		time.sleep(4)
		common.writesettings("REFRESH", "0")
	else:
		print(u"data: none\n\n")
		sys.stdout.flush()
	time.sleep(3)