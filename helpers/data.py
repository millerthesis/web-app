import csv
from pathlib import Path

GEODATA_PATH = Path('./', 'static', 'data')


def get_geo_data(geo):
    srcpath = Path(GEODATA_PATH, geo + '.csv')
    txt = srcpath.read_text()
    return list(csv.DictReader(txt.splitlines()))

