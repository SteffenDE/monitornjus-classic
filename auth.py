#!/usr/bin/env/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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

### Windows-Domäne ###

domain = "SCHULE"

### Gruppe ###

group = "G_Projekt_MonitorNjus"

######################################################################

###### Authentifizierungsfunktion ######

def authenticated():
		if groupauth and listauth:
			raise Exception("listauth und groupauth können (noch) nicht gleichzeitig aktiv sein.")
		if listauth:
				import os
				user = os.environ["REMOTE_USER"]
				if user.lower().replace(domain.lower()+"\\", "") in userliste:
						pass
				else:
						print "Content-Type: text/html"
						print
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
						print "Content-Type: text/html"
						print
						print """\
<!DOCTYPE html>
<html>
<body>
<h1>Du (%s) hast hier nichts verloren!</h1>
</body>
</html>""" % user
						exit(0)
				del sys
		else:
			pass