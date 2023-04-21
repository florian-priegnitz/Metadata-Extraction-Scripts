# Metadata Extraction Scripts

Dieses Repository enthält eine Sammlung von Python-Skripten zur Extraktion von Metadaten aus verschiedenen Dateitypen. Das Hauptziel dieser Skripte ist es, die Metadaten der Dateien auszulesen und sie in einer leicht lesbaren Form anzuzeigen.

## Script1) Exif Metadaten aus JPG-Bild-Datei auslesen

Mit dem Python-Skript `extract_jpg_metadata.py` können die Metadaten von einer JPG-Datei ausgelesen werden. Hierbei werden die EXIF-Metadaten aus der Bilddatei und mittels print Befehl angezeigt.

### Abhängigkeiten

- Python 3.6+
- Pillow (PIL Fork)


## Script 2) Exif Metadaten aus einem Ordner von Bildern auslesen

Das Python-Skript `extract_jpg_metadata_from_folder.py` liest die EXIF-Metadaten aus allen .jpg und .jpeg Bildern in einem angegebenen Ordner.

### Verwendung

Um das Skript zu verwenden, führen Sie den folgenden Befehl aus:
```PYTHON
python extract_jpg_metadata_from_folder.py
```

Das Skript wird Sie auffordern, den Pfad zum Ordner einzugeben, der die Bilddateien enthält, für die Sie die EXIF-Metadaten anzeigen möchten. Wenn die Bilddateien EXIF-Metadaten enthalten, werden diese in einer leicht lesbaren Form angezeigt.
