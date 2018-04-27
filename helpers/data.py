import csv
from pathlib import Path

META_PATH = Path('./', 'static', 'meta', 'census_meta.csv')
GEODATA_PATH = Path('./', 'static', 'data')

def get_census_meta():
    txt = META_PATH.read_text()
    rawdata = csv.DictReader(txt.splitlines())
    data = []
    for row in rawdata:
        if row['readable_name']:
            d = {}
            d['readable_name'] = row['readable_name']
            d['api_value'] = row['api_value']
            data.append(d)
    return data
    

def get_geo_data(geo):
    srcpath = Path(GEODATA_PATH, geo + '.csv')
    txt = srcpath.read_text()
    return list(csv.DictReader(txt.splitlines()))