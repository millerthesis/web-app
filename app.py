from flask import Flask
from flask import render_template
from helpers.state import get_state, get_states

myapp = Flask(__name__)

@myapp.route("/")
def homepage():
    rawhtml = render_template('homepage.html', states=get_states())
    return rawhtml

@myapp.route("/states/<statecode>")
def state(statecode):
    rawhtml = render_template('state.html', state=get_state(statecode))
    return rawhtml

if __name__ == '__main__':
    myapp.run(debug=True, use_reloader=True)
