from flask import Flask
from flask import render_template, request
from helpers.entity import get_state, get_states, get_us
import helpers.geocoder as geo

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
    data = geo.geocode(addr)
    coords = geo.get_coords(data)

    return render_template('geocode.html',
                                address_query=addr,
                                coords=coords,

                            )



# @myapp.route("/testdata")
# def xfoo():
#     return render_template('altairtest.html')

if __name__ == '__main__':
    myapp.run(debug=True, use_reloader=True)
