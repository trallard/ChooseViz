import os
from flask import Flask, render_template, request, redirect, session, url_for

# Create the app object and the session
app = Flask("Vizzard")
session = {}

@app.route('/')
def index():
    """Landing page for the app"""
    return render_template('index.html')

@app.route('/picker')
def picker():
    return render_template('data_picker.html')

@app.route("/picker_search", methods=['POST'])
def data_pick():
    data1 = request.values['data1']
    data2 = request.values['data2']
    return render_template('plot-show.html', data1=data1)

if 'PORT' in os.environ:
     app.run(host='0.0.0.0', port=int(os.environ['PORT']))
else:
     app.run(debug=True)
