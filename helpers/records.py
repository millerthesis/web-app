import json
from pathlib import Path

RECORDS_PATH = Path('./', 'static', 'data', 'records', 'records.json')
GEONAMES = ['us', 'state', 'county', 'tract']

def get_flat_data():
    srcpath = RECORDS_PATH
    data = json.loads(srcpath.read_text())
    records = []
    for d in data.values():
        d['full_name'] = d['name']
        d['short_name'] = d['name'].split(',')[0]
        if d['geo'] == 'county':
            d['name'] = d['short_name']
        elif d['geo'] == 'tract':
            d['name'] = ', '.join(d['full_name'].split(',')[0:-1])
    return [d for d in data.values()]


def get_geo_records():
    """
    returns a dict
    {'us': [], 'state': []}
    """
    data = get_flat_data()
    records = {}
    for geo in GEONAMES:
        records[geo] = [d for d in data if d['geo'] == geo]
    return records

