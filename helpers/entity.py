from helpers.data import get_geo_data


def get_states():
    return get_entities('state')

def get_state(code):
    return get_entity(code, 'state')


def get_entities(geo): # e.g. 'state', 'county'
    entities = []
    data = get_geo_data(geo)
    for s in data:
        entities.append( make_entity(s)  )
    return entities


def get_entity(code, geo):
    data = get_geo_data(geo)
    for s in data:
        if s['GEO_ID'] == code:
            return make_entity(s)
    
    raise ValueError("{s} is not a valid code".format(s=code))



def make_entity(rawdict):
    d = {}
    d['name'] = rawdict['NAME']
    d['id'] = rawdict['GEO_ID']
    d['Population'] = int(float(rawdict['B01003_001E']))
    d['White'] = int(float(rawdict['B02001_002E']))
    d['White %'] = round(100 * d['White'] / d['Population'], 1)
    return d
