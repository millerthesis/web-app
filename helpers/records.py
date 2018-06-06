import json
from pathlib import Path

RECORDS_PATH = Path('./', 'static', 'data', 'records')
GEONAMES = ['us', 'state', 'county', 'tract']


def get_us():
    data = json.loads(RECORDS_PATH.joinpath('us.json').read_text())
    d = data[0]
    d['parent_id'] = None
    d['full_name'] = d['name']
    d['short_name'] = 'U.S.'
    return d

def get_states():
    data = json.loads(RECORDS_PATH.joinpath('state.json').read_text())
    for d in data:
        idslug = d['id'].split('US')[-1][0:2]
        d['full_name'] = d['name']
        d['short_name'] = d['name'].split(',')[0]
        d['name'] = d['short_name']
        d['parent_id'] = '0100000US'

    return data

def get_counties():
    data = json.loads(RECORDS_PATH.joinpath('county.json').read_text())
    for d in data:
        idslug = d['id'].split('US')[-1][0:2]
        d['full_name'] = d['name']
        d['short_name'] = d['name'].split(',')[0]
        d['name'] = d['short_name']
        d['state_id'] = d['parent_id'] = '0400000US' + idslug
    return data

def get_tracts():
    records = []
    for jpath in RECORDS_PATH.joinpath('tract').glob('*.json'):
        data = json.loads(jpath.read_text())
        for d in data:
            idslug = d['id'].split('US')[-1]
            d['full_name'] = d['name']
            d['short_name'] = d['name'].split(',')[0]
            d['name'] = ', '.join(d['full_name'].split(',')[0:-1])
            d['county_id'] = d['parent_id'] = '0500000US' + idslug[0:5]
            d['state_id'] = '0400000US' + idslug[0:2]
            records.append(d)
    return records


def getdata():
    results = []
    results.append(get_us())
    results.extend(get_states())
    results.extend(get_counties())
    results.extend(get_tracts())
    return results

def get_all_records():
    """
    returns a dict
    {'us': [], 'state': []}
    """
    data = getdata()
    return data
    # records = {}
    # for geo in GEONAMES:
    #     records[geo] = [d for d in data if d['geo'] == geo]
    # return records



def get_sample_record():
    return getdata()[0]


if __name__ == '__main__':
    import json
    print(json.dumps(get_sample_record(), indent=2))
