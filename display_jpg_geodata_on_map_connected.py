import folium
import os
import webbrowser
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

def get_lat_lon_from_gps_info(gps_info):
    # (bereits vorhandener Code für diese Funktion)

print("Bitte geben Sie den Pfad zum Ordner mit den Bildern ein:")
folder_path = input()

files = os.listdir(folder_path)

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "Auswertung_Geodaten")
os.makedirs(desktop_path, exist_ok=True)

geo_data_list = []
total_count = 0

for file in files:
    # (bereits vorhandener Code für diese Schleife)

    if gps_info:
        lat_lon = get_lat_lon_from_gps_info(gps_info)
        date_taken = None

        if "DateTimeOriginal" in exif_data:
            date_taken_str = exif_data["DateTimeOriginal"]
            date_taken = datetime.strptime(date_taken_str, "%Y:%m:%d %H:%M:%S")

        if lat_lon and date_taken:
            geo_data_list.append([file, lat_lon[0], lat_lon[1], date_taken])

# Sortieren der Liste nach Datum und Uhrzeit
geo_data_list.sort(key=lambda x: x[3])

# Erstellen Sie eine Karte
m = folium.Map(location=[0, 0], zoom_start=2)

# Tabelle im Terminal anzeigen
print("\nBilder mit Geodaten:")
print("Bild".ljust(12), "Breitengrad".ljust(14), "Längengrad".ljust(14), "Datum")
print("-" * 54)

coordinates = []

for file, lat, lon, date_taken in geo_data_list:
    lat_decimal = float(lat)
    lon_decimal = float(lon)
    print(file.ljust(12), f"{lat_decimal:.6f}".ljust(14), f"{lon_decimal:.6f}".ljust(14), date_taken.strftime("%Y-%m-%d %H:%M:%S"))

    # Fügen Sie Marker zur Karte hinzu
    folium.Marker([lat_decimal, lon_decimal], tooltip=file).add_to(m)
    coordinates.append([lat_decimal, lon_decimal])

# Verbinden Sie die Pins, wenn sie am selben Tag aufgenommen wurden
prev_date = geo_data_list[0][3].date()
grouped_coordinates = []
for i, (_, lat, lon, date_taken) in enumerate(geo_data_list):
    current_date = date_taken.date()
    if current_date == prev_date:
        grouped_coordinates.append([lat, lon])
    else:
        if len(grouped_coordinates) > 1:
            folium.PolyLine(grouped_coordinates, color="blue", weight=2.5, opacity=1).add_to(m)
        grouped_coordinates = [[lat, lon]]
        prev_date = current_date

if len(grouped_coordinates) > 1:
    folium.PolyLine(grouped_coordinates, color="blue", weight=2.5, opacity=1).add_to(m)

# Speichern Sie die Karte in einer HTML-Datei
map_file = os.path.join(desktop_path, "image_map.html")
m.save(map_file)

# Öffnen Sie die Karte im Webbrowser
webbrowser.open(map_file)

# Ausgabe der Anzahl der ausgewerteten Bilder
print(f"\nAnzahl der ausgewerteten Bilder: {total_count}")
