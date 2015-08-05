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

def me():
	if groupauth and listauth:
		raise Exception("listauth und groupauth können (noch) nicht gleichzeitig aktiv sein.")

	if listauth:
		import os
		user = os.environ["REMOTE_USER"]
		if user.lower().replace(domain.lower()+"\\", "") in userliste:
			pass
		else:
			print u"Content-Type: text/html;charset=utf-8\n"
			print """\
<!DOCTYPE html>
<html>
<body>
<h1>Du (%s) hast hier nichts verloren!</h1>
</body>
</html>""" % user
			exit(0)

	elif groupauth:
		import ad
		import os
		user = os.environ["REMOTE_USER"]
		aduser = ad.find_user()
		if group.lower() in unicode(aduser.memberOf).lower() or "administrator" in user.lower():
			pass
		else:
			print u"Content-Type: text/html;charset=utf-8\n"
			print
			print """\
<!DOCTYPE html>
<html>
<body>
<h1>Du (%s) hast hier nichts verloren!</h1>
</body>
</html>""" % user
			exit(0)

	else:
		pass