from os import name
import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

def icon_producer(ele):
    if ele<1000 :
        return "green.png"
    elif 1000 <= ele < 3000 :
        return "orange.png"
    else:
        return "red.png"

map = folium.Map(location=[40.178, -99.903], zoom_start=6, tiles="OpenStreetMap")

fg = folium.FeatureGroup(name+"My Map")

for i in range(len(data)):
    pop = str(data.iloc[i]["VOLCANX020"]) + "\n" + str(data.iloc[i]["NAME"])

    icon = folium.features.CustomIcon(icon_producer(data.iloc[i]["ELEV"]), icon_size=(28, 30))

    fg.add_child(folium.Marker(
        location=[data.iloc[i]["LAT"], data.iloc[i]["LON"]],
        popup=pop,
        icon=icon
            )
            )

map.add_child(fg)
map.save("map.html")