# The repo for the webapp

Data cleaning and analysis was conducted in Python. The web app is powered by Flask, a microframework for Python. Mapping and geocoding services provided by Mapbox. Data visualizations were created with Carto, a mapping and location analysis service.


## Running the server locally

Make sure you have the dependencies installed by running `pip` like so:

```sh
pip install --upgrade pip
```

To run the server locally:

```sh
python app.py
```

And visit the site in your browser: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)



## To deploy on Heroku

(Note: make sure you've gotten the app to run locally, as mentioned above, before moving to this step)


The Heroku cloud service has a nice guide here: [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python)

This next section covers the minimal of the steps needed to get this Flask app going.

### Install the Heroku command-line tool

You should already have signed-up for a Heroku account and be **logged in.**

You can either download the Mac installer here: https://cli-assets.heroku.com/heroku.pkg

Or use Homebrew if you happen to have it installed:

```sh
brew install heroku/brew/heroku
```

### Authenticate with the `heroku` tool

With the heroku CLI tool installed, you can now run `heroku` commands. The very first command should be:

```
heroku login
```

Which will prompt you for your username and password (even if you're logged in via your browser)

### Prepare Heroku for hosting your app

This next step assumes you're in the home directory of `web-app` -- i.e., where you would be running `python app.py` if you had wanted to deploy the app locally.

To deploy onto Heroku, we use the `heroku create` subcommand to tell the *Heroku service* to provision a new server and get it ready:

```
heroku create
```

You'll get a response like this:

```sh
Creating app... done, ⬢ stark-waters-82009
https://stark-waters-82009.herokuapp.com/ | https://git.heroku.com/stark-waters-82009.git
```

If this were your Heroku account, this means the app will soon exist at this URL:

https://stark-waters-82009.herokuapp.com/ 

### Deploy your code on to the Heroku server

Getting your code onto the Heroku server is as easy as it is getting (i.e. *pushing*) your code onto onto Github's server

```
git push heroku master
```
