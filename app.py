from flask import Flask
from flask import render_template
from helpers.entity import get_state, get_states, get_us

myapp = Flask(__name__)

@myapp.route("/")
def homepage():
    rawhtml = render_template('homepage.html', states=get_states())
    return rawhtml

@myapp.route("/states/<statecode>")
def state(statecode):
    rawhtml = render_template('state.html', state=get_state(statecode), US=get_us())
    return rawhtml

@myapp.route("/testdata")
def xfoo():
    return render_template('altairtest.html')

if __name__ == '__main__':
    myapp.run(debug=True, use_reloader=True)
