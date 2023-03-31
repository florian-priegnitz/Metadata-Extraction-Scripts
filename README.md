# metadaten-von-dateien-mittels-python-script-auslesen
Im Rahmen einer Hausarbeit des Studiums IT Forensik sollen Metadaten von Images systematisch dokumentiert werden. Ein erstes Ziel ist es mittels Bash in Linux das Script bei der Analyse von sichergestellten Images zu nutzen, um damit Metadaten von Dateien systematisch und schnell zu dokumentieren. Langfristig möchte ich ein Script so bauen, dass ich ganze Folder oder Laufwerke damit auswerten kann, um die Metadaten dann z.B. mittels CSV in eine Datenbank zu Überführen.

Version 1 "Metadaten von einem Bild auslesen"
Dieses Python-Skript liest die EXIF-Metadaten eines Bildes aus und zeigt sie in der Konsole. Das Skript verwendet hierfür die Pillow-Bibliothek zur Verarbeitung von Bildern und zum Auslesen von EXIF-Daten (Wichtig: pip install Pillow).

Funktionsweise
- Das Skript fordert den Benutzer auf, den Pfad zum Bild einzugeben.
- Es öffnet das angegebene Bild mit der Image.open()-Funktion aus der Pillow-Bibliothek.
- Das Skript überprüft, ob das Bild EXIF-Daten enthält, indem es die _getexif()-Funktion aufruft.
- Falls vorhanden, werden die EXIF-Daten extrahiert und die Tags decodiert, um lesbare Namen für die Metadaten zu erhalten.
- Zum Schluss gibt das Skript die extrahierten EXIF-Metadaten in der Konsole aus.
Voraussetzungen
- Um das Skript auszuführen, benötigen Sie die Pillow-Bibliothek.

Verwendung
Führe das Skript aus und gib den Pfad zum gewünschten Bild ein. Das Skript gibt dann die EXIF-Metadaten des Bildes in der Konsole aus. Achte darauf, dass der eingegebene Pfad korrekt ist und der Schreibweise Ihres Betriebssystems entspricht.

Hinweis
Das Skript liest nur die Metadaten von Bildern im JPEG-Format, da nicht alle Bildformate EXIF-Metadaten unterstützen. Wenn das angegebene Bild keine EXIF-Daten enthält oder das Bild nicht geöffnet werden kann, gibt das Skript eine entsprechende Fehlermeldung aus.
