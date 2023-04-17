from PIL import Image
from PIL.ExifTags import TAGS
import os

# Benutzer auffordern, den Pfad zum Bild einzugeben
print("Bitte geben Sie den Pfad zum Bild ein:")
file_path = input()

# Überprüfen, ob die Datei existiert und die Dateiendung .jpg oder .jpeg hat
if not os.path.exists(file_path) or not file_path.lower().endswith(('.jpg', '.jpeg')):
    print("Die angegebene Datei existiert nicht oder hat eine ungültige Dateiendung. Bitte überprüfen Sie den Pfad und die Dateiendung (.jpg oder .jpeg).")

else:
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
