# Metadata Extraction Sripts

Dieses Repository enthält eine Sammlung von Python-Skripten zur Extraktion von Metadaten aus verschiedenen Dateitypen. Das Hauptziel dieser Skripte ist es, die Metadaten der Dateien auszulesen und sie in einer leicht lesbaren Form anzuzeigen.

## Requirements

Mein aktuelles Python-Setup, mit dem ich aktuell arbeite:
```PYTHON
# Libraries
ipython
ipykernel
numpy
matplotlib
Pillow
folium

# Linting
pylint
flake8
mypy
isort
black
pre-commit
autopep8
```

Alle erforderlichen Pakete können wie folgt installiert werden:
```PYTHON
pip install -r requirements.txt
```

## Einsatz von Chat-GPT 4
Hiermit mache ich den Einsatz von Chat-GPT in der Version 4 kenntlich.
- Alle Scripts wurden nachträglich mit Chat-GPT 4 debugged.
- Die Scripts 1-3 basieren noch auf meinem ursprünglichen Entwurf
- Das modulare Vorgehen in den späteren Scripts wurde von GPT 4 vorgeschlagen.
- Sowohl die Geodaten-Scripts als auch die erweiterten Bildtypen-Scripts hätte ich ohne GPT 4 nicht alleine erstellen können. Gerade das Formatieren von Geodaten zu den passenden Längen- und Breitengraden wäre mir sonst nicht gelungen.

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

## Script 4) Geodaten von Bildern auf einer Karte als Pin anzeigen

Das Python-Skript `display_jpg_geodata_on_map.py` extrahiert die Geodaten (Breitengrad und Längengrad) aus den EXIF-Metadaten aller .jpg und .jpeg Bilder in einem angegebenen Ordner und zeigt die Geodaten auf einer Karte an. Die Karte wird im Ordner "Auswertung_Geodaten" auf Ihrem Desktop als HTML-Datei gespeichert und im Webbrowser geöffnet.

### Verwendung

Um das Skript zu verwenden, führen Sie den folgenden Befehl aus:
```PYTHON
display_jpg_geodata_on_map.py
```

Es muss danach eine Pfadangbae gemacht werden
```PYTHON
/path/to/your/image/folder
```
In der Textausgabe sind Details zur Auswertung ersichtlich: 
```PYTHON
Bilder mit Geodaten:
Bild Breitengrad Längengrad
IMG_001.jpg 52.520008 13.404954
IMG_002.jpg 48.856613 2.352222

Anzahl der ausgewerteten Bilder: 10
```

Ein neuer Tab im Webbrowser wird geöffnet und zeigt die Karte mit den Geodaten der Bilder an. Darüber hinaus wird die Karte im folgenden Folder abgelegt:
```PYTHON
C:/Users/User/Desktop/Auswertung_Geodaten/image_map.html
```

## Script 5) Geodaten von Bildern auf einer Karte als verbundene Pin anzeigen

Das Python-Skript `display_jpg_geodata_on_map_connected.py`funktioniert wie Script 4. Jedoch werden Pins mit dem gleichen Tagesdatum miteinander verbunden.

## Script 6) Extrahieren und Exportieren von Metadaten für verschiedene Bildformate

Das Python-Skript `export_metadaten_jpg_png_raw_tiff_to_csv.py` extrahiert die EXIF-Metadaten für verschiedene Bildformate (.jpg, .jpeg, .tiff, .tif, .png, .nef, .cr2, .arw, .dng) aus einem angegebenen Ordner und exportiert sie in eine CSV-Datei. Die CSV-Datei wird im Ordner "Auswertung_Metadaten" auf dem Desktop gespeichert.

### Verwendung

Das Script kann analog wie die anderen Skripts verwendet werden.  Die erstellte CSV-Datei enthält alle Metadaten der unterstützten Bildformate in einer Datei im angegebenen Ordner.

