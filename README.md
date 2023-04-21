# Metadata Extraction Scripts

Dieses Repository enthält eine Sammlung von Python-Skripten zur Extraktion von Metadaten aus verschiedenen Dateitypen. Das Hauptziel dieser Skripte ist es, die Metadaten der Dateien auszulesen und sie in einer leicht lesbaren Form anzuzeigen.

## Script 1) Exif Metadaten aus JPG-Bild-Datei auslesen

Mit dem Python-Skript `extract_jpg_metadata.py` können die Metadaten von einer JPG-Datei ausgelesen werden. Hierbei werden die EXIF-Metadaten aus der Bilddatei und mittels print Befehl angezeigt.

1. Das Skript fordert den Benutzer auf, den Pfad zum Bild einzugeben.
2. Es öffnet das angegebene Bild mit der Image.open()-Funktion aus der Pillow-Bibliothek.
3. Das Skript überprüft, ob das Bild EXIF-Daten enthält, indem es die _getexif()-Funktion aufruft.
4. Falls vorhanden, werden die EXIF-Daten extrahiert und die Tags decodiert, um lesbare Namen für die Metadaten zu erhalten.
5. Zum Schluss gibt das Skript die extrahierten EXIF-Metadaten in der Konsole aus.

Was sind EXIF-Metadaten?
https://de.wikipedia.org/wiki/Exchangeable_Image_File_Format

### Abhängigkeiten

- Python 3.6+
- Pillow (PIL Fork)

```PYTHON
pip install Pillow
```


## Script 2) Exif Metadaten aus einem Ordner von Bildern auslesen

Das Python-Skript `extract_jpg_metadata_from_folder.py` liest die EXIF-Metadaten aus allen .jpg und .jpeg Bildern in einem angegebenen Ordner.

### Verwendung

Um das Skript zu verwenden, führe den folgenden Befehl aus:
```PYTHON
python extract_jpg_metadata_from_folder.py
```

Das Skript wird Sie auffordern, den Pfad zum Ordner einzugeben, der die Bilddateien enthält, für die Sie die EXIF-Metadaten anzeigen möchten. Wenn die Bilddateien EXIF-Metadaten enthalten, werden diese in einer leicht lesbaren Form angezeigt.


## Script 3) Exif Metadaten aus einem Ordner mit Bildern in eine CSV-Datei exportieren

Das Python-Skript `export_jpg_metadata_to_csv.py` liest die EXIF-Metadaten aus allen .jpg und .jpeg Bildern in einem angegebenen Ordner aus und exportiert sie in eine CSV-Datei. Die CSV-Datei wird im Ordner "Auswertung_Metadaten" auf dem Desktop gespeichert.

### Verwendung

Um das Skript zu verwenden, führen Sie den folgenden Befehl aus:
```PYTHON
python extract_jpg_metadata_to_csv.py
```
Das Skript brauch einen Pfad, der nun eingeben werden muss. Die Metadaten werden dann in einer CSV-Datei gespeichert und der Pfad zur CSV-Datei wird angezeigt.

### Beispiel
Pfadangabe:
```PYTHON
/path/to/your/image/folder
```

Metadaten werden dann wie folgt ausgegeben und abgespeichert: 
```PYTHON
/Users/username/Desktop/Auswertung_Metadaten/Metadaten_2023-04-04_12-30-45.csv 
```

