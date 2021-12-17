# install folium and pandas and geopy before runnig the code

import folium
import pandas
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

# html = """<h4><b6>Volcano information:</b6></h4>
#Height: %s m
#"""

def color_producer(elevation):
    if elevation< 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "blue"


html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br> 
Height: %s m
""" # Create a link with <a>, Insert single line breaks in a text with <br>

map = folium.Map(location=[43.64,-79.38],zoom_start=6, tiles= "Stamen Terrain")

FG_1 = folium.FeatureGroup(name = 'Volcanos')

# for coordinates in [[43.646,-79.384],[43.63,-79.37],[43.6346,-79.38]]:
for lt, ln, elv, nme in zip(lat,lon, elev, name):
     # iframe = folium.IFrame(html=html % str(elv), width=200, height=100)
     iframe = folium.IFrame(html=html % (nme, nme, elv), width=200, height=100)
     FG_1.add_child(folium.Marker(location=[lt,ln],popup = folium.Popup(iframe), icon = folium.Icon(icon_color = 'beige',color = color_producer(elv))))

FG_2 = folium.FeatureGroup(name = 'Population')
FG_2.add_child(folium.GeoJson(data = open('world.json','r',encoding='utf-8-sig').read(),
style_function= lambda x: {'fillColor':'blue' if x['properties']['POP2005']<70000000 
else 'red'})) # adding color based on population data
map.add_child(FG_1)
map.add_child(FG_2)
map.add_child(folium.LayerControl()) # this looks for objects to add to map from FG features
map.save("MyMap.html")
