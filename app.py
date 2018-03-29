import os
from flask import Flask, render_template, request, url_for
from flask import Blueprint
from helpers.plotting import find_plots

# Create the app object and the session
app = Flask("Vizzard")
session = {}

blueprint = Blueprint('site', __name__, static_folder='plots')
app.register_blueprint(blueprint)


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
    print(data1)
    data2 = request.values['data2']
    plot_dic = find_plots(data1)
    print(plot_dic)
    return render_template('plot-show.html', plot_dict=plot_dic)

if 'PORT' in os.environ:
     app.run(host='0.0.0.0', port=int(os.environ['PORT']))
else:
     app.run(debug=True)
