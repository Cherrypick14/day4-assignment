#   locating the zip code of a place using Nominatim API

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my-app")

def find_zipcode():

    user_zip= int(input("Please enter a zipcode to start a search: "))
    location= geolocator.geocode(user_zip)
    return  user_zip,location


print(find_zipcode())
