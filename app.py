import os
from flask import Flask, render_template, request, redirect, session, url_for

# Create the app object and the session
app = Flask("Vizzard")
session = {}

@app.route('/')
def index():
    """Landing page for the app"""
    return render_template('index.html')


if 'PORT' in os.environ:
     app.run(host='0.0.0.0', port=int(os.environ['PORT']))
else:
     app.run(debug=True)
