import os
from PIL import Image
from PIL.ExifTags import TAGS

# Benutzer auffordern, den Pfad zum Ordner mit den Bildern einzugeben
print("Bitte geben Sie den Pfad zum Ordner mit den Bildern ein:")
folder_path = input()

# Liste aller Dateien im Ordner
files = os.listdir(folder_path)

# Für jede Datei im Ordner
for file in files:
    file_path = os.path.join(folder_path, file)

    # Prüfen, ob es sich um ein Bild handelt (nur für .jpg und .jpeg)
    if file_path.lower().endswith(('.jpg', '.jpeg')):
        print(f"\nMetadaten für Bild: {file}")

        # Bild öffnen
        try:
            image = Image.open(file_path)
        except Exception as e:
            print(f"Fehler beim Öffnen des Bildes: {e}")

        # Prüfen, ob das Bild EXIF-Daten hat und diese auslesen
        if hasattr(image, '_getexif'):
            exif_info = image._getexif()
            if exif_info:
                exif_data = {}
                # Tags decodieren und EXIF-Daten speichern
                for tag, value in exif_info.items():
                    decoded_tag = TAGS.get(tag, tag)
                    exif_data[decoded_tag] = value

                # EXIF-Daten ausgeben
                for tag, value in exif_data.items():
                    print(f"{tag}: {value}")
            else:
                print("Keine EXIF-Daten gefunden.")
        else:
            print("Keine EXIF-Daten gefunden.")
