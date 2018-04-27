from helpers.data import get_geo_data

def get_state(statecode):
    statesdata = get_geo_data('state')
    for s in statesdata:
        if s['GEO_ID'] == statecode:
            return make_state(s)
    
    raise ValueError("{s} is not a valid state code".format(s=statecode))


def get_states():
    states = []
    statesdata = get_geo_data('state')
    for s in statesdata:
        states.append( make_state(s)  )
    return states

def make_state(statedict):
    d = {}
    d['name'] = statedict['NAME']
    d['id'] = statedict['GEO_ID']
    d['Population'] = int(float(statedict['B00001_001E']))
    d['White'] = int(float(statedict['B02001_002E']))
    d['White %'] = round(100 * d['White'] / d['Population'], 1)
    return d
