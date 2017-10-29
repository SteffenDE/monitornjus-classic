# Dead. See [MonitorNews](https://gitlab.steffend.me/monitornews/monitornews-web)
# monitornjus
## What is MonitorNjus?
Python  CGI application written for displaying various pages time-based or static on a monitor in the intranet (e.g. in a school).

## Alternative Versions:
[mod_python](https://files.steffend.de/monitornjus/0.9.2/momp.zip)<br>
[Classic-ASP](https://files.steffend.de/monitornjus/0.9.2/moasp.zip)

## example
http://monitornjus.steffend.de

idea based on MonitorNews by Tamer Berber

## Setup
### German
MonitorNjus ist eine Alternative zu "MonitorNews" von Tamer Berber. Im Gegensatz zu "MonitorNews" ist MonitorNjus in Python geschrieben. Auf dem Server, der eingesetzt werden soll muss also Python installiert sein. MonitorNjus in für Python 2 ausgelegt.

#### common.py
In der Datei "common.py" werden im Abschnitt "Settings" mögliche Einstellungen vorgenommen.

Die Variable "debugv" legt die De­tail­liert­heit der Fehlermeldungen fest. 0 bedeutet keine Details, 1 bedeutet Fehler anzeigen, 2 beduetet vollen Traceback anzeigen.

Die Variablen "listauth" und "groupauth" legen die Art der Authentifizierung fest. Beide Arten sind nur für die Authentifizierung unter Windows per IIS gedacht.<br>
Eventuell wird noch eine simple Authentifizierung mittels prompt nach Benutzernamen und Passwort hinzugefügt.
"listauth" greift auf die Variable "REMOTE_USER" des IIS zu und prüft, ob sich dieser Benutzer in der Benutzerliste befindet.<br>
Diese Benutzer benötigen Schreibzugriff auf das MonitorNjus Admin Verzeichnis!
"groupauth" greift auch auf die Variable "REMOTE_USER" zu und prüft per pywin32, ob der Benutzer in der Gruppe, die per "group" festgelegt wird, ist.<br>
Diese Gruppe benötigt Schreibzugriff auf das MonitorNjus Admin Verzeichnis!

"domain" legt die Windows-Domäne fest (z.B. "SCHULE").
"group" legt die Active-Directory Benutzergruppe fest, gegen die die zugreifenden Benutzer authentifiziert werden sollen.

#### bin/vertretung.py
Diese Datei ist dafüt gedacht, den Vertretungplan einer Schule, die UNTIS einsetzt in einem passenderen Design auf dem Monitor anzuzeigen. Die jeweiligen replace Befehle können nach Belieben geändert werden.
Der Dateisystempfad zu den HTML Dateien für den aktuellen bzw. nächsten Tag muss in der Variablen "path" angegeben werden.<br>
Beispiele:<br>
"D:/MLData/Benutzer/Projekte/MonitorNjus/sync/heute_und_morgen/"<br>
"C:/MonitorNjus/Sync/hum/"<br>
...<br>

In disem Verzeichnis sollten sich die beiden von UNTIS generierten HTML Dateien befinden, deren Namen per Variable "name_heute" und "name_morgen" festlegen lassen.
