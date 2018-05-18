from copy import copy
import json
from pathlib import Path
import requests
from urllib.parse import urlencode

SAMPLE_DATA_PATH = Path('static', 'samples', 'census-lookup.json') #TK


# https://geocoding.geo.census.gov/geocoder/geographies/coordinates?x=-118.2439&y=34.0544&benchmark=Public_AR_Current&format=json&vintage=Current_Current
BASE_ENDPOINT = 'https://geocoding.geo.census.gov/geocoder/geographies/coordinates'
BASE_PARAMS = {
    'benchmark':  'Public_AR_Current',
    'vintage': 'Current_Current',
    'format': 'json',
}



def lookup_tract(longitude, latitude):
  d = lookup(longitude, latitude)
  return get_tract(d)


def lookup(longitude, latitude):
    myparams = copy(BASE_PARAMS)
    myparams['x'] = longitude
    myparams['y'] = latitude
    r = requests.get(BASE_ENDPOINT, params=myparams)
    data = r.json()
    return data


def get_tract(data):
    tracts = data['result']['geographies']['Census Tracts']
    t = tracts[0]
    d = {}
    d['name'] = t['NAME']
    d['tract'] = t['TRACT']
    d['state'] = t['STATE']
    d['county'] = t['COUNTY']
    return d




"""
What the census structure looks like:
"Census Tracts": [
        {
          "OID": 207901115289435,
          "STATE": "06",
          "FUNCSTAT": "S",
          "NAME": "Census Tract 2074",
          "AREAWATER": 6458,
          "LSADC": "CT",
          "CENTLON": "-118.2455899",
          "BASENAME": "2074",
          "INTPTLAT": "+34.0562223",
          "MTFCC": "G5020",
          "COUNTY": "037",
          "GEOID": "06037207400",
          "CENTLAT": "+34.0557740",
          "INTPTLON": "-118.2466420",
          "AREALAND": 862957,
          "OBJECTID": 13453,
          "TRACT": "207400"
        }
      ],


"""

