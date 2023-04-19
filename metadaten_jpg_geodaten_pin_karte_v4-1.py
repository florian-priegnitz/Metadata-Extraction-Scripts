import folium
import os
import webbrowser
from datetime import datetime
from folium import PolyLine
from PIL import Image
from PIL.ExifTags import TAGS

def get_lat_lon_from_gps_info(gps_info):
    # ... (keine Änderungen in dieser Funktion)

def get_capture_date(exif_data):
    date_string = exif_data.get("DateTimeOriginal", None)
    if date_string:
        try:
            return datetime.strptime(date_string, "%Y:%m:%d %H:%M:%S")
        except ValueError:
            pass
    return None

print("Bitte geben Sie den Pfad zum Ordner mit den Bildern ein:")
folder_path = input()

# ... (keine Änderungen in diesem Abschnitt)

geo_data_list = []

for file in files:
    # ... (keine Änderungen in diesem Abschnitt)

    gps_info = exif_data.get("GPSInfo", None)
    if gps_info:
        lat_lon = get_lat_lon_from_gps_info(gps_info)
        capture_date = get_capture_date(exif_data)
        if lat_lon and capture_date:
            geo_data_list.append([file, lat_lon[0], lat_lon[1], capture_date])

geo_data_list.sort(key=lambda x: x[3])

# Erstellen Sie eine Karte
m = folium.Map(location=[0, 0], zoom_start=2)

# Tabelle im Terminal anzeigen
print("\nAlle Bilder mit Geodaten:")
print("Bild".ljust(12), "Breitengrad".ljust(14), "Längengrad")
print("-" * 40)

coordinates = []

for file, lat, lon, _ in geo_data_list:
    lat_decimal = float(lat)
    lon_decimal = float(lon)
    print(file.ljust(12), f"{lat_decimal:.6f}".ljust(14), f"{lon_decimal:.6f}")

    # Fügen Sie Marker zur Karte hinzu
    folium.Marker([lat_decimal, lon_decimal], tooltip=file).add_to(m)
    coordinates.append([lat_decimal, lon_decimal])

# Zeichnen Sie eine Linie zwischen den Pins
poly_line = PolyLine(locations=coordinates, color="blue", weight=2.5, opacity=0.8)
poly_line.add_to(m)

# Speichern Sie die Karte in einer HTML-Datei
map_file = os.path.join(desktop_path, "image_map.html")
m.save(map_file)

# Öffnen Sie die Karte im Webbrowser
webbrowser.open(map_file)
