#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 05.08.2015 (Version 0.9.1)

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

############################## Settings ##############################

###### Windows-Authentifizierung ######
### Art ###

listauth = False     	# Wenn True, Benutzer in "userliste" eintragen. Benutzer benötigen Schreibrechte im ADMIN Verzeichnis!
groupauth = False     	# Wenn True, muss pywin32 installiert sein! Gruppe für die Authentifizierung unter group = "xy" festlegen!

### Userliste ###

userliste = [
"administrator",
"groi",
"peter.praker"
]

### Windows-Domäne + Gruppe ###

domain = "SCHULE"
group = "G_Projekt_MonitorNjus"

######################################################################

###### Authentifizierungsfunktion ######

def me(Request, Response):
	if groupauth and listauth:
		raise Exception("listauth und groupauth können (noch) nicht gleichzeitig aktiv sein.")
	user = os.environ["LOGON_USER"]
	if listauth:
		if user.lower().replace(domain.lower()+"\\", "") in userliste:
			pass
		else:
			raise Warning("Du, \""+user+"\", hast hier nichts verloren!")
	elif groupauth:
		import imp
		ad = imp.load_source("ad", workingdir+"/admin/ad.py")
		aduser = ad.find_user()
		if group.lower() in unicode(aduser.memberOf).lower() or "administrator" in user.lower():
			pass
		else:
			raise Warning("Du, \""+user+"\", hast hier nichts verloren!")