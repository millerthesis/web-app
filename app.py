from flask import Flask
from flask import render_template, request
from helpers.entity import get_state, get_states, get_us, get_county, get_tract, get_counties_by_state_code
from helpers.indexes import get_indexes
import helpers.geocoder as geo
import helpers.censusgeo as cg
from helpers.viz import makeprotomap

from helpers.records import get_geo_records
from pathlib import Path
import json

CENSUS_RECORDS = get_geo_records()
US_RECORD = CENSUS_RECORDS['us'][0]
STATES = CENSUS_RECORDS['state']
COUNTIES = CENSUS_RECORDS['county']
TRACTS = CENSUS_RECORDS['tract']
GENTRIFICATION_KEYS = US_RECORD['gentrification'].keys()

myapp = Flask(__name__)

@myapp.route("/viz")
def vizproto():
    viz = makeprotomap()
    return render_template('infopages/altairtest.html', viz=viz)


@myapp.route("/")
def homepage():
    return render_template('homepage.html',
                                us=US_RECORD,
                                states=STATES,
                                gentrification_keys=GENTRIFICATION_KEYS
                        )


@myapp.route("/metrics")
def metricpage():
    return render_template('infopages/metric_pages/metrics.html')



@myapp.route("/tract")
def geotracter():
    addr = request.args['address']
    coords = geo.geocode(addr)
    codes = cg.lookup_tract(coords['longitude'], coords['latitude'])

    countyfips = codes['state'] + codes['county']
    county = next(c for c in COUNTIES if countyfips in c['id'])
    state = next(c for c in STATES if codes['state'] in c['id'])
    tract = get_tract(codes['tract'])

    return render_template('tract.html',
                                address_query=addr,
                                coords=coords,
                                censuscodes=codes,
                                county=county,
                                state=state,
                                tract=tract,
                                us=get_us(),
                            )



@myapp.route("/gentrification")
def gentrification_metric():
    addr = 'tk'
    coords = json.loads(Path('static/samples/prototypepage/coords.json').read_text())
    censuscodes = json.loads(Path('static/samples/prototypepage/censuscodes.json').read_text())
    us = json.loads(Path('static/samples/prototypepage/us.json').read_text())
    tract = json.loads(Path('static/samples/prototypepage/tract.json').read_text())
    county = json.loads(Path('static/samples/prototypepage/county.json').read_text())
    state = json.loads(Path('static/samples/prototypepage/state.json').read_text())

    return render_template('infopages/metric_pages/gentrification.html',

                                address_query=addr,
                                coords=coords,
                                censuscodes=censuscodes,
                                county=county,
                                state=state,
                                us=us,
                                tract=tract,
                            )



@myapp.route("/demography")
def demography():


    addr = "1200 bryn mawr chicago, il"
    coords = json.loads(Path('static/samples/prototypepage/coords.json').read_text())
    censuscodes = json.loads(Path('static/samples/prototypepage/censuscodes.json').read_text())
    us = json.loads(Path('static/samples/prototypepage/us.json').read_text())
    tract = json.loads(Path('static/samples/prototypepage/tract.json').read_text())
    county = json.loads(Path('static/samples/prototypepage/county.json').read_text())
    state = json.loads(Path('static/samples/prototypepage/state.json').read_text())

    return render_template('infopages/metric_pages/demographics.html',
                                address_query=addr,
                                coords=coords,
                                censuscodes=censuscodes,
                                county=county,
                                state=state,
                                us=us,
                                tract=tract,
                            )

@myapp.route("/housing")
def housing():
    from pathlib import Path
    import json

    addr = "1200 bryn mawr chicago, il"
    coords = json.loads(Path('static/samples/prototypepage/coords.json').read_text())
    censuscodes = json.loads(Path('static/samples/prototypepage/censuscodes.json').read_text())
    us = json.loads(Path('static/samples/prototypepage/us.json').read_text())
    tract = json.loads(Path('static/samples/prototypepage/tract.json').read_text())
    county = json.loads(Path('static/samples/prototypepage/county.json').read_text())
    state = json.loads(Path('static/samples/prototypepage/state.json').read_text())

    return render_template('infopages/metric_pages/housing.html',
                                address_query=addr,
                                coords=coords,
                                censuscodes=censuscodes,
                                county=county,
                                state=state,
                                us=us,
                                tract=tract,
                            )

@myapp.route("/income")
def income():
    from pathlib import Path
    import json

    addr = "1200 bryn mawr chicago, il"
    coords = json.loads(Path('static/samples/prototypepage/coords.json').read_text())
    censuscodes = json.loads(Path('static/samples/prototypepage/censuscodes.json').read_text())
    us = json.loads(Path('static/samples/prototypepage/us.json').read_text())
    tract = json.loads(Path('static/samples/prototypepage/tract.json').read_text())
    county = json.loads(Path('static/samples/prototypepage/county.json').read_text())
    state = json.loads(Path('static/samples/prototypepage/state.json').read_text())

    return render_template('infopages/metric_pages/income.html',
                                address_query=addr,
                                coords=coords,
                                censuscodes=censuscodes,
                                county=county,
                                state=state,
                                us=us,
                                tract=tract,
                            )

@myapp.route("/residency")
def residency():
    from pathlib import Path
    import json

    addr = "1200 bryn mawr chicago, il"
    coords = json.loads(Path('static/samples/prototypepage/coords.json').read_text())
    censuscodes = json.loads(Path('static/samples/prototypepage/censuscodes.json').read_text())
    us = json.loads(Path('static/samples/prototypepage/us.json').read_text())
    tract = json.loads(Path('static/samples/prototypepage/tract.json').read_text())
    county = json.loads(Path('static/samples/prototypepage/county.json').read_text())
    state = json.loads(Path('static/samples/prototypepage/state.json').read_text())

    return render_template('infopages/metric_pages/residency.html',
                                address_query=addr,
                                coords=coords,
                                censuscodes=censuscodes,
                                county=county,
                                state=state,
                                us=us,
                                tract=tract,
                            )

@myapp.route("/info/<endpoint>")
def infopage(endpoint):
    return render_template('infopages/{}.html'.format(endpoint))


@myapp.route("/states/<statecode>")
def state(statecode):
    fips = statecode[-2:]
    state = next(s for s in STATES if s['id'] == statecode)
    counties = [c for c in COUNTIES if c['id'][-4:2] == fips]
    return render_template('state.html',
            state=state,
            US=US_RECORD,
            counties=counties
            )


@myapp.route("/proto/")
def geoprototype():
    from pathlib import Path
    import json

    addr = "1200 bryn mawr chicago, il"
    coords = json.loads(Path('static/samples/prototypepage/coords.json').read_text())
    censuscodes = json.loads(Path('static/samples/prototypepage/censuscodes.json').read_text())
    us = json.loads(Path('static/samples/prototypepage/us.json').read_text())
    tract = json.loads(Path('static/samples/prototypepage/tract.json').read_text())
    county = json.loads(Path('static/samples/prototypepage/county.json').read_text())
    state = json.loads(Path('static/samples/prototypepage/state.json').read_text())


    return render_template('protopage.html',
                                address_query=addr,
                                coords=coords,
                                censuscodes=censuscodes,
                                county=county,
                                state=state,
                                us=us,
                                tract=tract,
                            )


@myapp.errorhandler(404)
def render_404(err):
    return render_template('meta/404.html', error=err)


# @myapp.route("/testdata")
# def xfoo():
#     return render_template('altairtest.html')


# CODE FOR geocode_address():
# from pathlib import Path
#     import json

#     addr = request.args['address']
#     coords = geo.geocode(addr)
#     censuscodes = cg.lookup_tract(coords['longitude'], coords['latitude'])
#     county = get_county(censuscodes['state'], censuscodes['county'])
#     state = get_state(censuscodes['state'])
#     tract = {}

#     return render_template('geocode.html',
#                                 address_query=addr,
#                                 coords=coords,
#                                 censuscodes=censuscodes,
#                                 county=county,
#                                 state=state,
#                                 tract=tract,
#                                 us=get_us(),
#                             )

if __name__ == '__main__':
    myapp.run(debug=True, use_reloader=True)
