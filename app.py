from flask import Flask
from flask import render_template


myapp = Flask(__name__)

@myapp.route("/")
def homepage():
    rawhtml = render_template('homepage.html')
    return rawhtml

if __name__ == '__main__':
    myapp.run(debug=True, use_reloader=True)
