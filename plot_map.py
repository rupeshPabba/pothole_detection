import folium
from folium.features import DivIcon
import mysql.connector

def fetch_gps_coordinates():
    db_config = {
        'user': 'root',   #change your user for mysql
        'password': '######',  #change your password here
        'host': 'localhost',
        'database': '######' #change your database name
    }
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT latitude, longitude FROM gps_loc"
    cursor.execute(query)
    rows = cursor.fetchall()
    gps_coordinates = [{"latitude": row[0], "longitude": row[1]} for row in rows]
    cursor.close()
    conn.close()

    return gps_coordinates

def calculate_center_point(coordinates):
    total_lat = sum(coord["latitude"] for coord in coordinates)
    total_lon = sum(coord["longitude"] for coord in coordinates)
    avg_lat = total_lat / len(coordinates)
    avg_lon = total_lon / len(coordinates)
    return avg_lat, avg_lon

def draw_circle(center_lat, center_lon, radius, map_obj):
    folium.Circle(
        location=[center_lat, center_lon],
        radius=radius,
        color='red',
        fill=True,
        fill_color='blue',
        fill_opacity=0.2
    ).add_to(map_obj)

gps_coords = fetch_gps_coordinates()
center_lat, center_lon = calculate_center_point(gps_coords)

my_map = folium.Map(location=[center_lat, center_lon], zoom_start=15)

for coord in gps_coords:
    folium.Marker(
        location=[coord["latitude"], coord["longitude"]],
        icon=folium.Icon(icon="cloud")
    ).add_to(my_map)

# Draw a circle with a radius of 1 km (1000 meters)
draw_circle(center_lat, center_lon, 750, my_map)

my_map.save("gps_map.html")
