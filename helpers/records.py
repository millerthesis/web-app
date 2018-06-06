import json
from pathlib import Path

RECORDS_PATH = Path('./', 'static', 'data', 'records', 'records.json')
GEONAMES = ['us', 'state', 'county', 'tract']


def getdata():
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

        elif d['geo'] == 'us':
            d['short_name'] = 'U.S.'

        # set geo relations
        geo = d['geo']
        idslug = d['id'].split('US')[-1]
        if geo == 'us':
            # 0100000US
            d['parent_id'] = None
        elif geo == 'state':
            # 0400000US01
            d['parent_id'] = '0100000US'
        elif geo == 'county':
            # 0500000US01007
            d['state_id'] = d['parent_id'] = '0400000US' + idslug[0:2]
        elif geo == 'tract':
            # 1400000US54003971500
            d['county_id'] = d['parent_id'] = '0500000US' + idslug[0:5]
            d['state_id'] = d['county_id'] = '0400000US' + idslug[0:2]

    return [d for d in data.values()]




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
