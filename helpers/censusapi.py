from urllib.parse import urlencode, quote

API_TYPES = {
    'acs5-subject': 'https://api.census.gov/data/2016/acs/acs5/subject',
    'acs5-detailed': 'https://api.census.gov/data/2016/acs/acs5',
    'decennial': 'https://api.census.gov/data/2010/sf1',
}   

params = {
    'state': '06',
    'county': '037',
    'tract': '207400',
}

def for_tract_querystring(state, county, tract):
    params = {
    'tract': '207400',
    'in state': '06',
    'county': '037',
    }

    return urlencode(params)
    """
    state, county, tract are strings, e.g.
        "06", "037", "207400"

    Returns:
        "tract:207400&in=state:06%20county:037"
    """



def tract_request_url(apitype, fieldnames, state, county, tract):
   
    if API_TYPES == 'acs5-subject':
        print( + urlencode(params))

    if API_TYPES == 'acs5-detailed':
        print( + urlencode(params))

    if API_TYPES == 'decennial':
        print( + urlencode(params))


"""
    Args:
        apitype <str>: either "acs5-subject" or "acs5-detailed" or "decennial"

    Returns a string
        Subject Tables call
        https://api.census.gov/data/2016/acs/acs5/subject?get=NAME,S0101_C01_001E&for=tract:207400&in=state:06%20county:037

        Detailed Tables call
        https://api.census.gov/data/2016/acs/acs5?get=NAME,B01001_001E&for=tract:207400&in=state:06%20county:037

        Decennial call
        https://api.census.gov/data/2010/sf1?get=NAME,P0010001,P0030001&for=tract:207400&in=state:06%20county:037"""


    if apiname not in API_TYPES.keys():
        raise ValueError("apiname must be {}".format(API_TYPES.keys()))

    api_endpoint = API_TYPES[apitype]
    fieldnames = ['NAME'] + fieldnames
    forqs = for_tract_querystring(state, county, tract)

    return forqs



"""
# info about subject API
# https://api.census.gov/data/2016/acs/acs5/subject/examples.html
# https://api.census.gov/data/2016/acs/acs5/variables.html
# https://www.census.gov/programs-surveys/decennial-census/data/api.html

"""

