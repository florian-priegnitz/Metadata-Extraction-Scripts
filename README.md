# Metadaten von Dateien mittels Python Script auslesen und dokumentieren<br/>
Im Rahmen einer Hausarbeit des Studiums IT Forensik Sommersemester 2022 sollten Metadaten von Images systematisch dokumentiert werden. Aus dieser Arbeit ist dieses python-Script entstanden.
Ein erstes Ziel war es mittels Bash in Linux das Script bei der Analyse von sichergestellten Images zu nutzen, um damit Metadaten von Dateien systematisch und schnell zu dokumentieren. 
Langfristig möchte ich das Script so umbauen, dass ich größere Medienmengen damit auswerten kann, um die Metadaten dann z.B. mittels CSV in eine Datenbank zu Überführen.

Mein Python-Setup basiert auf dem Setup aus einem Kurs von Jan Schaffranek<br/>
Link Github <a href="https://github.com/franneck94/UdemyPythonIntro"> Jan Schaffrannek Udemy Python Intro</a>

<b>Einsatz von GPT-4</b><br/>
An dieser Stelle mache ich den Einsatz von GPT-4 kenntlich. Aktuell habe ich keinen Plattformzugriff sondern nutze GPT-4 über die normale Chatfunktion. GPT 3.5 Legacy und Default kamen nicht zum Einsatz. Wenn ich Scripts neu erstelle, nutze ich GPT-4 für das Debugging, für das Überprüfen des Scripts im Allgemeinen. Ich mache auf den Einsatz deswegen aufmerksam, weil es mir hilft beim Scripten, weil es gute wissenschaftliche Praxis ist, transparent zu arbeiten.

- Ich habe alle veröffentlichten Scripts noch einmal mittels GPT-4 überprüfen lassen.
- Es wurden Änderungen an den Scripts vorgenommen, woraus ich lernen konnte.
- GPT-4 hat mir vorgeschlagen, eher modular zu programmieren, so dass Details in Funktionen ausgelagert werden; diese Versionen werde ich hier ebenfalls veröffentlichen.

<b>Version 1 "Metadaten von einem JPG-Bild auslesen"</b><br/>

Dieses Python-Skript liest die EXIF-Metadaten eines Bildes aus und zeigt sie in der Konsole. Das Skript verwendet hierfür die Pillow-Bibliothek zur Verarbeitung von Bildern und zum Auslesen von EXIF-Daten (Wichtig: pip install Pillow).

Funktionsweise
- Das Skript fordert den Benutzer auf, den Pfad zum Bild einzugeben.
- Es öffnet das angegebene Bild mit der Image.open()-Funktion aus der Pillow-Bibliothek.
- Das Skript überprüft, ob das Bild EXIF-Daten enthält, indem es die _getexif()-Funktion aufruft.
- Falls vorhanden, werden die EXIF-Daten extrahiert und die Tags decodiert, um lesbare Namen für die Metadaten zu erhalten.
- Zum Schluss gibt das Skript die extrahierten EXIF-Metadaten in der Konsole aus.
- Mittels os wird überprüft, die angegebene Bilddatei ein JPG-Datei ist.

Voraussetzungen
- Um das Skript auszuführen, benötigen Sie die Pillow-Bibliothek.

Verwendung
Führe das Skript aus und gib den Pfad zum gewünschten Bild ein. Das Skript gibt dann die EXIF-Metadaten des Bildes in der Konsole aus. Achte darauf, dass der eingegebene Pfad korrekt ist und der Schreibweise Ihres Betriebssystems entspricht.

Hinweis
Das Skript liest nur die Metadaten von Bildern im JPEG-Format, da nicht alle Bildformate EXIF-Metadaten unterstützen. Wenn das angegebene Bild keine EXIF-Daten enthält oder das Bild nicht geöffnet werden kann, gibt das Skript eine entsprechende Fehlermeldung aus.

<b>Version 2 "Metadaten von einem Ordner mit JPG-Bildern auslesen"</b><br/>

In dieser Version habe ich den Code erweitert, so dass jetzt ganze Folder ausgelesen werden können. 
- Zuerst wird der User aufgefordert, den Pfad zum Ordner mit den Bildern einzugeben. 
- Anschließend listet der Code alle Dateien im angegebenen Ordner auf und prüft, ob es sich um eine JPG- oder JPEG-Datei handelt. 
- Für jedes Bild im Ordner werden die Metadaten ausgelesen und in der Konsole angezeigt.

Der Befehl files = os.listdir(folder_path) verwendet die os-Bibliothek, um eine Liste aller Dateien und Ordner im angegebenen Verzeichnis (folder_path) zu erstellen. Die Liste enthält die Namen der Dateien und Ordner als Zeichenketten. In diesem Fall ist folder_path der Pfad zum Ordner, den der User eingegeben hat.

<b>Version 3 "Metadaten von JPG-Bildern in eine CSV-Datei schreiben und auf dem Desktop ablegen"</b><br/>

In einem nächsten Schritt wurde das Script so erweitert, dass die Metadaten in eine CSV-Datei gespeichert wurden.

- CSV-Bibliothek importieren: Die csv-Bibliothek wird importiert, um die CSV-Datei einfach zu erstellen und zu bearbeiten.
- Pfad zum Desktop-Ordner erstellen: Der Code erstellt den Pfad zum Desktop-Ordner "Auswertung_Metadaten" und verwendet os.makedirs() mit exist_ok=True, um den Ordner zu erstellen, falls er noch nicht existiert.
- Timestamp erstellen: Der Timestamp wird mit der time-Bibliothek erstellt und im Dateinamen der CSV-Datei verwendet, um eine eindeutige Datei für jede Ausführung des Skripts zu erstellen.
- Extrahieren und Speichern von Tags: Der Code extrahiert die Tags aus den Metadaten und speichert sie in einer Menge namens all_tags. Die Menge stellt sicher, dass die Tags eindeutig sind. Da die Tags sowohl Zeichenketten als auch Ganzzahlen enthalten können, konvertieren wir sie in Zeichenketten, bevor wir sie der Menge hinzufügen und sortieren.
- CSV-Datei öffnen und bearbeiten: Der Code öffnet die CSV-Datei im Schreibmodus und verwendet die csv.DictWriter-Klasse

Bei den Metadaten gab es einen TypeError: '<' not supported between instances of 'int' and 'str'. Dieser beruhte darauf, dass zuerst versucht wurde, die Tags zu sortieren, obwohl diese sowohl Zeichenketten als auch Ganzzahlen enthalten. Hier mussten 'decoded_tag' in eine Zeichenkette konvertiert werden, bevor es sortiert werden kann: all_tags.add(str(decoded_tag)).
