from os import name
import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

def icon_producer(ele):
    if ele<1000 :
        return "icons/green.png"
    elif 1000 <= ele < 3000 :
        return "icons/orange.png"
    else:
        return "icons/red.png"

map = folium.Map(location=[40.178, -99.903], zoom_start=4, tiles="CartoDB positron")

fg = folium.FeatureGroup(name+"My Map")

for i in range(len(data)):
    pop = str(data.iloc[i]["VOLCANX020"]) + "\n" + str(data.iloc[i]["NAME"])

    icon = folium.features.CustomIcon(icon_producer(data.iloc[i]["ELEV"]), icon_size=(28, 30))

    fg.add_child(folium.Marker(
        location=[data.iloc[i]["LAT"], data.iloc[i]["LON"]],
        popup=pop,
        icon=icon))

fg.add_child(folium.GeoJson(open("world.json", 'r', encoding="utf-8-sig").read(),
style_function= lambda x: {'fillColor': 'green' if x["properties"]["POP2005"] < 10000000
else 'orange' if 10000000 <= x["properties"]["POP2005"] < 20000000 else 'red'}))

map.add_child(fg)
map.save("map.html")