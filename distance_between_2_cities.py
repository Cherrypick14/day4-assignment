#    to determine the distance between 2 geolocation points(Cairo and Nairobi)
#   import haversine library

import haversine as hs
from haversine import Unit

cairo_cods=(31.507098187652723, 33.30583979211274)
nairobi_cods=(-1.4899033770642174, 36.20623017525199)

#   calculating distance in miles

print(hs.haversine(cairo_cods,nairobi_cods, unit=Unit.MILES))

