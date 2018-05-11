from pathlib import Path
from urllib.parse import urlencode
import json
import requests
from copy import copy

SAMPLE_DATA_PATH = Path('static', 'samples', 'census-lookup.json') #TK


# https://geocoding.geo.census.gov/geocoder/geographies/coordinates?x=-118.2439&y=34.0544&benchmark=Public_AR_Current&format=json&vintage=Current_Current
BASE_ENDPOINT = 'https://geocoding.geo.census.gov/geocoder/geographies/coordinates'
BASE_PARAMS = {
    'benchmark':  'Public_AR_Current',
    'vintage': 'Current_Current',
    'format': 'json',
}




def lookup(longitude, latitude):
    """
    Calls Census Geocoder API

    Returns dictionary
    """
    myparams = copy(BASE_PARAMS)


    # blah blah blah this part is the dummy part:
    txt = SAMPLE_DATA_PATH.read_text()
    ##############
    return json.loads(txt)



def get_tract(data):
    ###
    d = {}
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




