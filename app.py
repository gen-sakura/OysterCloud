# Gen Sakura, 2023
# Flask app for OysterCloud backend for NOAA ShuckProject
# Email gensakura002@gmail.com for all questions and suggestions.
# Next year's team feel free to modify/add your name here.
# Based off Azure flask template in the README.md

# Import all dependencies
import os
import sys

# Add pythonScripts to path
path = os.path.abspath('pythonScripts')
sys.path.append(path)

import JSON_stuff as jss # from pythonScripts
import json as json

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

# Define Constants
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

# App configuration and rendering
app = Flask(__name__)

@app.route('/')
def index():
   print('Request for index page received')
   
   # Load and create JSON file for the last 1000 pH readings
   jss.create_last_1000_pH_dataset_JSON()
   json_url = os.path.join(SITE_ROOT, 'last_1000_pH_data.json')
   last_1000_pH_data = json.load(open(json_url))

   return render_template('index.html', jsonfile=last_1000_pH_data)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
