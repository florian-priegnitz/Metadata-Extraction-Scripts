import os
import csv
import time
from PIL import Image
from PIL.ExifTags import TAGS

def get_exif_data(file_path):
    exif_data = {}

    # Bild öffnen und prüfen, ob es EXIF-Daten hat
    try:
        image = Image.open(file_path)
        if hasattr(image, '_getexif'):
            exif_info = image._getexif()
            if exif_info:
                for tag, value in exif_info.items():
                    decoded_tag = TAGS.get(tag, tag)
                    exif_data[decoded_tag] = value
    except Exception as e:
        print(f"Fehler beim Auslesen der Metadaten: {e}")

    return exif_data

# Benutzer auffordern, den Pfad zum Ordner mit den Bildern einzugeben
print("Bitte geben Sie den Pfad zum Ordner mit den Bildern ein:")
folder_path = input()

# Liste aller Dateien im Ordner
files = os.listdir(folder_path)

metadata_list = []
all_tags = set()

# Metadaten für jedes unterstützte Bild extrahieren
for file in files:
    file_path = os.path.join(folder_path, file)

    # Prüfen, ob es sich um ein unterstütztes Bild handelt
    if file_path.lower().endswith(('.jpg', '.jpeg', '.tiff', '.tif', '.png', '.nef', '.cr2', '.arw', '.dng')):
        print(f"\nMetadaten für Bild: {file}")

        exif_data = get_exif_data(file_path)
        metadata_list.append((file, exif_data))
        all_tags.update(exif_data.keys())

# Pfad zum Desktop-Ordner "Auswertung_Metadaten" erstellen
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "Auswertung_Metadaten")
os.makedirs(desktop_path, exist_ok=True)

# Dateiname mit Timestamp erstellen
timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
csv_file_name = f"Metadaten_{timestamp}.csv"
csv_file_path = os.path.join(desktop_path, csv_file_name)

# CSV-Datei öffnen und Schreibzugriff erhalten
with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["Bild"] + sorted(list(all_tags))
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # CSV-Header schreiben
    csv_writer.writeheader()

    # Metadaten für jedes Bild in die CSV-Datei schreiben
    for file, exif_data in metadata_list:
        row = {"Bild": file}
        row.update(exif_data)
        csv_writer.writerow(row)

print(f"Metadaten wurden in {csv_file_path} gespeichert.")
