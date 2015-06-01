#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 07.05.2015 (Version 0.7.1)

import random                       # Random Modul importieren

rancolor = ['red','indigo','blue','light-blue','cyan','teal','green','light-green','lime','amber','orange','deep-orange','grey','blue-grey']
color = random.choice(rancolor)     # Zufallsauswahl der Darbe

if color == "red":                  # Umwandlung des Farbnamens in Hexadezimal
	hexa = "#f44336"
elif color == "indigo":
	hexa = "#3f51b5"
elif color == "blue":
	hexa = "#2196f3"
elif color == "light-blue":
	hexa = "#03a9f4"
elif color == "cyan":
	hexa = "#00bcd4"
elif color == "teal":
	hexa = "#009688"
elif color == "green":
	hexa = "#4caf50"
elif color == "light-green":
	hexa = "#8bc34a"
elif color == "lime":
	hexa = "#cddc39"
elif color == "amber":
	hexa = "#ffc107"
elif color == "orange":
	hexa = "#ff9800"
elif color == "deep-orange":
	hexa = "#ff5722"
elif color == "grey":
	hexa = "#9e9e9e"
elif color == "blue-grey":
	hexa = "#607d8b"
else: 
	hexa == "wtf"