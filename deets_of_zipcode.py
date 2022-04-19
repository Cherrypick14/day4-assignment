#   locating the zip code of a place using Nominatim API

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my-app")

user_zip= int(input("Please enter a zipcode to start a search: "))
#   zipcode1 ="00912"

print(f"The given zipcode1 is: {user_zip}\n")

location= geolocator.geocode(user_zip)

print(location.address)