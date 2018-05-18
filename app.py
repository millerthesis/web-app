from flask import Flask
from flask import render_template, request
from helpers.entity import get_state, get_states, get_us, get_county
import helpers.geocoder as geo
import helpers.censusgeo as cg

myapp = Flask(__name__)

@myapp.route("/")
def homepage():
    return render_template('homepage.html', states=get_states())

@myapp.route("/info/<endpoint>")
def infopage(endpoint):
    return render_template('infopages/{}.html'.format(endpoint))


@myapp.route("/states/<statecode>")
def state(statecode):
    return render_template('state.html', state=get_state(statecode), US=get_us())



@myapp.route("/geocode")
def geocode_address():
    addr = request.args['address']
    coords = geo.geocode(addr)
    censuscodes = cg.lookup_tract(coords['longitude'], coords['latitude'])
    county = get_county(censuscodes['state'], censuscodes['county'])
    state = get_state(censuscodes['state'])
    tract = 'TK'

    return render_template('geocode.html',
                                address_query=addr,
                                coords=coords,
                                censuscodes=censuscodes,
                                county=county,
                                state=state,
                                us=get_us(),
                            )


@myapp.route("/proto")
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

if __name__ == '__main__':
    myapp.run(debug=True, use_reloader=True)
