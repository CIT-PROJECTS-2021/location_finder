import folium
import json
from requests import get

ip_address_information = get('http://ip-api.com/json/').text
ip_address_information = json.loads(ip_address_information)
ip_address_information = dict(ip_address_information) 

#for i in ip_address:
#    print(f' {i:15} --> {ip_address[i]} ')
latitude_longitude = ip_address_information['lat'],ip_address_information['lon']
map = folium.Map(
    location=latitude_longitude,
    zoom_start=19,
    control_scale=True
)
folium.Marker(
    location=latitude_longitude,
    popup='My ip address'
).add_to(map)

map.save('me.html')

