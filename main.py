import phonenumbers
from phonenumbers import geocoder
import geolocation

NUMBER = '+2567055088051'

ch_number=phonenumbers.parse(NUMBER,'CH')
#print(geocoder.description_for_number(ch_number,'en'))
print(dir(geolocation))