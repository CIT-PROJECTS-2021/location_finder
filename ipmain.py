import geocoder
import folium

g=geocoder.ip('me')
print(g)

my_line_address=g.latlng
print(my_line_address)

my_map1=folium.Map(
    location=my_line_address,
    zoom_start=12
)
my_map1.save('.index.html')