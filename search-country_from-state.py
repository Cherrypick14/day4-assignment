#   search country from state name using Geopy pckg and Nominatim API

from geopy import Nominatim

geolocation= Nominatim(user_agent="my=app")

def state_name(state):
    location= geolocation.geocode(state)
    return location.address

print(state_name("Kisumu"))
