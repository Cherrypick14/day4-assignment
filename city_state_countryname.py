#    a Python function to get the city, state and country name of a specified
#   latitude and longitude using Nominatim API and Geopy package

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

geolocator = Nominatim(user_agent="my-app")

def city_state_country(cords):
    reverse = RateLimiter(geolocator.reverse,min_delay_seconds=1)
    location= reverse(cords, exactly_one=1)
    address = location.raw['address']
    city = address.get('city','')
    state = address.get('state','')
    country = address.get('country','')
    return city,state,country

print(city_state_country("0.17985023125326466, 37.61248005798618"))