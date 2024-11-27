from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import time

def get_distance_between_addresses(address1, address2):
    geolocator = Nominatim(user_agent="pizzeria_distance_calculator")
    try:
        location1 = geolocator.geocode(address1)
        time.sleep(1)
        location2 = geolocator.geocode(address2)
        if location1 and location2:
            coords1 = (location1.latitude, location1.longitude)
            coords2 = (location2.latitude, location2.longitude)
            distance = geodesic(coords1, coords2).kilometers
            return round(distance, 2)
        return None
    except Exception:
        return None
