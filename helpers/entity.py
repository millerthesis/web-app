from helpers.data import get_geo_data
GEOS = ['us', 'state',] # just for reference


def get_us():
    return get_entity('0100000US', 'us')

def get_states():
    return get_entities('state')

def get_state(code):
    if len(code) == 2:
        _id = '0400000US' + code
    else:
        _id = code

    return get_entity(_id, 'state')

def get_tract(code=False):
    code = '0500000US06081'
    # dummy
    d = get_entity(code, 'county')
    d['name'] = 'Dummy Tract'
    return d

def get_county(state_code, county_code):
    _id = '0500000US' + state_code + county_code
    return get_entity(_id, 'county')


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
    d['White (total)'] = int(float(rawdict['B02001_002E']))
    d['% White'] = round(100 * d['White (total)'] / d['Population'], 1)
    d['Median Age'] = int(float(rawdict['B01002_001E']))

    # housing
    d['Total Housing Units'] = int(float(rawdict['B25075_001E']))
    d['Number in owner-occupied units'] = int(float(rawdict['B25026_002E']))
    d['Median home value'] = int(float(rawdict['B25077_001E']))
    d['Homes worth $1 million or more'] = int(float(rawdict['B25075_025E']))
    d['Percent of homes worth $1 million or more'] = round(d['Homes worth $1 million or more'] * 100.0 / d['Total Housing Units'], 1)

    # income
    d['Population (Poverty determined)'] = int(float(rawdict['B17001_001E']))
    d['Below poverty level'] = int(float(rawdict['B17001_002E']))
    d['% Below poverty level'] = round(d['Below poverty level'] * 100.0 / d['Population (Poverty determined)'], 1)
    d['Household income $200k+'] = int(float(rawdict['B19001_017E']))
    d['Percent of households with income $200k+'] = round(d['Household income $200k+'] * 100.0 / d['Population'], 1)
    d['Median household income'] = int(float(rawdict['B19013_001E']))
    d['Have at least a bachelors degree'] = int(float(rawdict['B15003_022E']))
    d['Percent with bachelors degree'] = round(d['Have at least a bachelors degree'] * 100.0 / d['Population'], 1)

    # residency
    d['Born in state'] = int(float(rawdict['B05002_003E']))
    d['Percent born in state'] = round(d['Born in state'] * 100.0 / d['Population'], 1)
    d['Born in other state'] = int(float(rawdict['B05002_004E']))
    d['Percent born in other state'] = round(d['Born in other state'] * 100.0 / d['Population'], 1)
    d['Foreign born'] = int(float(rawdict['B05002_009E']))
    d['Percent foreign born'] = round(d['Foreign born'] * 100.0 / d['Population'], 1)
    d['Moved in 1979 and earlier'] = int(float(rawdict['B25026_008E']))
    d['Moved in 1980 to 1989'] = int(float(rawdict['B25026_007E']))
    d['Moved in 1990 to 1999'] = int(float(rawdict['B25026_006E']))
    d['Moved in 2010 to 2014'] = int(float(rawdict['B25026_004E']))
    d['Moved in 2015 or later'] = int(float(rawdict['B25026_003E']))

    return d

########

    # ########
    #     # historical residency
    #     d['Born in state_00'] = int(float(rawdict['P021003']))
    #     d['Born in different state_00'] = int(float(rawdict['P021004']))
    #     d['Foreign born_00'] = int(float(rawdict['P021009']))
    #     d['Moved in before 1969_09'] = int(float(rawdict['B25109_008E']))
    #     d['Moved in between 1970-1979_09'] = int(float(rawdict['B25109_007E']))
    #     d['Moved in between 1980-1989_09'] = int(float(rawdict['B25109_006E']))
    #     d['Moved in between 1990-1999_09'] = int(float(rawdict['B25109_005E']))
    #     d['Moved in between 2000-2004_09'] = int(float(rawdict['B25109_004E']))
    #     d['Moved in 2005 or later_09'] = int(float(rawdict['B25026_003E']))

    #     # historical income
    #     d['Percent for poverty determined_00'] = int(float(rawdict['P087001']))
    #     d['Amount below poverty level_00'] = int(float(rawdict['P087002']))
    #     d['Household income $200K+_00'] = int(float(rawdict['P052017']))
    #     d['Median household income_00'] = int(float(rawdict['P053001']))
    #     d['Amount with bachelors degrees_00'] = int(float(rawdict['P037015, P037032']))

    #     # historical race
    #     d['Total population_00'] = int(float(rawdict['P001001']))
    #     d['White people (percent)_00'] = int(float(rawdict['P003003']))
    #     d['Median age_00'] = int(float(rawdict['P013001']))

    #     # historical housing
    #     d['Median value (dollars)_09 for owner-occupied housing units'] = int(float(rawdict['B25077_001E']))
    #     d['Homes worth $1 million or more_09'] = int(float(rawdict['B25075_025E']))

# HOUSING_FIELDS = [
#     ['Total Housing Units', 'B25075_001E'],
#     ['Number in owner-occupied units', 'B25026_002E'],
#     ['Median home value', 'B25077_001E'],
#     ['Homes worth $1 million or more', 'B25075_025E'],
# ]
