# monitornjus
## What is MonitorNjus?
Python application written for displaying various pages time-based or static on a monitor in a intranet (e.g. in a school with the paedML Musterlösung).

## example
http://monitornjus.steffend.de

idea based on MonitorNews by Tamer Berber

## Setup
### German
MonitorNjus ist eine Alternative zu "MonitorNews" von Tamer Berber. Im Gegensatz zu "MonitorNews" ist MonitorNjus in Python geschrieben. Auf dem Server, der eingesetzt werden soll muss also Python installiert sein. MonitorNjus in für Python 2 ausgelegt.

#### common.py
In der Datei "common.py" werden im Abschnitt "Settings" mögliche Einstellungen vorgenommen.

Die Variable "debugv" legt die De­tail­liert­heit der Fehlermeldungen fest. 0 bedeutet keine Details, 1 bedeutet Fehler anzeigen, 2 beduetet vollen Traceback anzeigen.

Die Variablen "listauth" und "groupauth" legen die Art der Authentifizierung fest. Beide Arten sind nur für die Authentifizierung unter Windows per IIS gedacht.
Eventuell wird noch eine simple Authentifizierung mittels prompt nach Benutzernamen und Passwort hinzugefügt.
"listauth" greift auf die Variable "REMOTE_USER" des IIS zu und prüft, ob sich dieser Benutzer in der Benutzerliste befindet.
Diese Benutzer benötigen Schreibzugriff auf das MonitorNjus Admin Verzeichnis!
"groupauth" greift auch auf die Variable "REMOTE_USER" zu und prüft per pywin32, ob der Benutzer in der Gruppe, die per "group" festgelegt wird, ist.
Diese Gruppe benötigt Schreibzugriff auf das MonitorNjus Admin Verzeichnis!

"domain" legt die Windows-Domäne fest (z.B. "SCHULE").
"group" legt die Active-Directory Benutzergruppe fest, gegen die die zugreifenden Benutzer authentifiziert werden sollen.

#### bin/vertretung.py
Diese Datei ist dafüt gedacht, den Vertretungplan einer Schule, die UNTIS einsetzt in einem passenderen Design auf dem Monitor anzuzeigen. Die jeweiligen replace Befehle können nach Belieben geändert werden.
Der Dateisystempfad zu den HTML Dateien für den aktuellen bzw. nächsten Tag muss in der Variablen "path" angegeben werden. 
Beispiele:
"D:/MLData/Benutzer/Projekte/MonitorNjus/sync/heute_und_morgen/"
"C:/MonitorNjus/Sync/hum/"
...

In disem Verzeichnis sollten sich die beiden von UNTIS generierten HTML Dateien befinden, deren Namen per Variable "name_heute" und "name_morgen" festlegen lassen.
