from flask import Flask, render_template, request, redirect, session, url_for

# Create the app object and the session
app = Flask("Vizzard")
session = {}

@app.route('/')
def index():
    """Landing page for the app"""
    return render_template('index.html')

app.run(debug=True)