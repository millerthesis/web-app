from helpers.data import get_geo_data
GEOS = ['us', 'state',] # just for reference



def get_us():
    return get_entity('0100000US', 'us')

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

    # race
    d['Population'] = int(float(rawdict['B01003_001E']))
    d['White'] = int(float(rawdict['B02001_002E']))
    d['White %'] = round(100 * d['White'] / d['Population'], 1)
    d['Median Age'] = int(float(rawdict['B01002_001E']))

    # housing
    d['Total Housing Units'] = int(float(rawdict['B25075_001E']))
    d['Number in owner-occupied units'] = int(float(rawdict['B25026_002E']))
    d['Median home value'] = int(float(rawdict['B25077_001E']))
    d['Homes worth $1 million or more'] = int(float(rawdict['B25075_025E']))

    # income
    d['Population (Poverty determined)'] = int(float(rawdict['B17001_001E']))
    d['Below poverty level'] = int(float(rawdict['B17001_002E']))
    d['% Below poverty level'] = round(d['Below poverty level'] * 100.0 / d['Population (Poverty determined)'], 1)


    d['Household income $200K+'] = int(float(rawdict['B19001_017E']))
    d['Median household income'] = int(float(rawdict['B19013_001E']))
    d['Have at least a bachelors degree'] = int(float(rawdict['B15003_022E']))


    # residency
    d['Born in state'] = int(float(rawdict['B05002_003E']))
    d['Born in other state'] = int(float(rawdict['B05002_004E']))
    d['Foreign born'] = int(float(rawdict['B05002_009E']))
    d['Moved in 1979 and earlier'] = int(float(rawdict['B25026_008E']))
    d['Moved in 1980 to 1989'] = int(float(rawdict['B25026_007E']))
    d['Moved in 1990 to 1999'] = int(float(rawdict['B25026_006E']))
    d['Moved in 2010 to 2014'] = int(float(rawdict['B25026_004E']))
    d['Moved in 2015 or later'] = int(float(rawdict['B25026_003E']))


    return d











########


# HOUSING_FIELDS = [
#     ['Total Housing Units', 'B25075_001E'],
#     ['Number in owner-occupied units', 'B25026_002E'],
#     ['Median home value', 'B25077_001E'],
#     ['Homes worth $1 million or more', 'B25075_025E'],
# ]
