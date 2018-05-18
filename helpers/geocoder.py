from urllib.parse import quote
from os import environ
import requests

GEOCODE_API_URL = 'https://api.mapbox.com/geocoding/v5/mapbox.places/{place}.json?access_token={token}'
# SAMPLE_GEOCODE_DATA_PATH = Path('static', 'samples', 'mapbox-geocode.json')



def geocode(address):
    d = call_geocoder(address)
    return get_coords(d)


def call_geocoder(address):
    safeaddress = quote(address, '')
    url = GEOCODE_API_URL.format(place=safeaddress, token=environ['MAPBOX_ACCESS_TOKEN'])
    resp = requests.get(url)
    return resp.json()

def get_coords(data):
    feat = data['features'][0]
    d = {}
    d['name'] = feat['place_name']
    d['longitude'] = feat['geometry']['coordinates'][0]
    d['latitude'] = feat['geometry']['coordinates'][1]
    return d
