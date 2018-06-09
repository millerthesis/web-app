from flask import Flask
from flask import render_template, request
from helpers.entity import get_state, get_states, get_us, get_county, get_tract, get_counties_by_state_code
from helpers.indexes import get_indexes
import helpers.geocoder as geo
import helpers.censusgeo as cg
from helpers.viz import makeprotomap
from helpers.records import get_all_records

from helpers.metrics import *


from pathlib import Path
import json

CENSUS_RECORDS = get_all_records()
US_RECORD = next(c for c in CENSUS_RECORDS if c['geo'] == 'us')
STATES = [c for c in CENSUS_RECORDS if c['geo'] == 'state']
COUNTIES = [c for c in CENSUS_RECORDS if c['geo'] == 'county']
TRACTS = [c for c in CENSUS_RECORDS if c['geo'] == 'tract']
GENTRIFICATION_KEYS = US_RECORD['gentrification'].keys()



def get_record_by_id(id):
    return next(d for d in CENSUS_RECORDS if d['id'] == id)

def get_records_by_parent_id(id, data=CENSUS_RECORDS):
    return [d for d in data if d['parent_id'] == id]




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




@myapp.route("/state/<statecode>")
def state(statecode):
    entity = state = get_record_by_id(statecode)
    parent = US_RECORD
    children = counties = get_records_by_parent_id(statecode, COUNTIES)
    peers = STATES
    return render_template('entity.html',
            state=state,
            parent=parent,
            entity=entity,
            us=US_RECORD,
            peers=peers,
            children=children,
            entities_group=[state,US_RECORD,],
                all_entities=[US_RECORD, entity] + peers + children,
            )

@myapp.route("/county/<countycode>")
def county(countycode):
    entity = county = get_record_by_id(countycode)
    parent=state = get_record_by_id(entity['parent_id'])
    peers = state_counties = get_records_by_parent_id(entity['parent_id'], COUNTIES)
    children = tracts = get_records_by_parent_id(entity['id'], TRACTS)

    return render_template('entity.html',
            state=state,
            county=county,
            entity=entity,
            children=children,
            parent=parent,
            peers=peers,
            us=US_RECORD,
            entities_group=[county,state,US_RECORD,],
            all_entities=[US_RECORD, parent, entity] + peers + children,
            )

@myapp.route("/tract/<tractcode>")
def tract(tractcode):

    entity = tract = get_record_by_id(tractcode)
    peers = get_records_by_parent_id(entity['parent_id'], TRACTS)
    parent = county = get_record_by_id(entity['parent_id'])
    state = get_record_by_id(county['parent_id'])
    children = []

    return render_template('entity.html',
            state=state,
            county=county,
            entity=entity,
            children=[],
            peers=peers,
            us=US_RECORD,
            entities_group=[tract,county,state,US_RECORD,],
            all_entities=[US_RECORD, parent, entity] + peers + children,)



@myapp.route("/geotract")
def geotracter():
    addr = request.args['address']
    # coords = geo.geocode(addr)
    # codes = cg.lookup_tract(coords['longitude'], coords['latitude'])

    # countyfips = codes['state'] + codes['county']
    # county = next(c for c in COUNTIES if countyfips in c['id'])
    # state = next(c for c in STATES if codes['state'] in c['id'])
    # tract = get_tract(codes['tract'])

    # return render_template('tract.html',
    #                             address_query=addr,
    #                             coords=coords,
    #                             censuscodes=codes,
    #                             county=county,
    #                             state=state,
    #                             tract=tract,
    #                             us=get_us(),
    #                         )




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

    return render_template('infopages/metric_pages/demographics.html',
                                us=US_RECORD,
                                states=STATES,
                                tracts=TRACTS,
                                counties=get_metric_counties(COUNTIES)
                            )




@myapp.route("/housing")
def housing():


    return render_template('infopages/metric_pages/housing.html',
                                us=US_RECORD,
                                states=STATES,
                                tracts=TRACTS,
                                counties=get_metric_counties(COUNTIES)
                            )

@myapp.route("/income")
def income():


    return render_template('infopages/metric_pages/income.html',
                                 us=US_RECORD,
                                states=STATES,
                                tracts=TRACTS,
                                counties=get_metric_counties(COUNTIES)
                            )

@myapp.route("/residency")
def residency():


    return render_template('infopages/metric_pages/residency.html',
                                us=US_RECORD,
                                states=STATES,
                                tracts=TRACTS,
                                counties=get_metric_counties(COUNTIES)
                            )

@myapp.route("/info/<endpoint>")
def infopage(endpoint):
    return render_template('infopages/{}.html'.format(endpoint))





@myapp.errorhandler(404)
def render_404(err):
    return render_template('meta/404.html', error=err)

if __name__ == '__main__':
    myapp.run(debug=True, use_reloader=True)
