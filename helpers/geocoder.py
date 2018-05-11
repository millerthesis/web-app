from pathlib import Path
import json

SAMPLE_GEOCODE_DATA_PATH = Path('static', 'samples', 'mapbox-geocode.json')

def geocode(address):
    # blah blah blah
    txt = SAMPLE_GEOCODE_DATA_PATH.read_text()
    return json.loads(txt)


def get_coords(data):
    feat = data['features'][0]
    d = {}
    d['name'] = feat['place_name']
    d['longitude'] = feat['geometry']['coordinates'][0]
    d['latitude'] = feat['geometry']['coordinates'][1]
    return d
