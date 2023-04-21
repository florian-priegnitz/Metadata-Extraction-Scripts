import folium
import os
import webbrowser
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

def get_lat_lon_from_gps_info(gps_info):
    latitude = gps_info.get(2, None)
    longitude = gps_info.get(4, None)
    lat_ref = gps_info.get(1, None)
    lon_ref = gps_info.get(3, None)

    if not latitude or not longitude:
        return None

    lat_deg, lat_min, lat_sec = latitude
    lon_deg, lon_min, lon_sec = longitude
    lat = lat_deg + (lat_min / 60) + (lat_sec / 3600)
    lon = lon_deg + (lon_min / 60) + (lon_sec / 3600)

    if lat_ref == "S":
        lat = -lat
    if lon_ref == "W":
        lon = -lon

    return lat, lon

print("Bitte geben Sie den Pfad zum Ordner mit den Bildern ein:")
folder_path = input()

files = os.listdir(folder_path)

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "Auswertung_Geodaten")
os.makedirs(desktop_path, exist_ok=True)

geo_data_list = []
total_count = 0

for file in files:
    file_path = os.path.join(folder_path, file)

    if file_path.lower().endswith(('.jpg', '.jpeg')):
        try:
            image = Image.open(file_path)

            if hasattr(image, '_getexif'):
                exif_info = image._getexif()
                if exif_info:
                    exif_data = {}
                    for tag, value in exif_info.items():
                        decoded_tag = TAGS.get(tag, tag)
                        exif_data[decoded_tag] = value

                    gps_info = exif_data.get("GPSInfo", None)
                    if gps_info:
                        lat_lon = get_lat_lon_from_gps_info(gps_info)
                        date_taken = None

                        if "DateTimeOriginal" in exif_data:
                            date_taken_str = exif_data["DateTimeOriginal"]
                            date_taken = datetime.strptime(date_taken_str, "%Y:%m:%d %H:%M:%S")

                        if lat_lon and date_taken:
                            geo_data_list.append([file, lat_lon[0], lat_lon[1], date_taken])
                            total_count += 1

        except Exception as e:
            print(f"Fehler beim Öffnen des Bildes: {e}")

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

