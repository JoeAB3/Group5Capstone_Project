import numpy as np
import pandas as pd
from clusteringData import Kmean_Olympics
# for sqlalchemy
from config import db_password
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
# for plotting
import plotly.express as px
#for flask
from flask import Flask, render_template, redirect, url_for, request

#setup the database
print('setup the database')
db_string = f"postgresql://postgres:{db_password}@127.0.0.1:5432/OlympicAnalysis_FP"
#Create the database engine
engine = create_engine(db_string)
olympics_df = pd.read_sql_table('Analysis', engine)

# --- Setup FLASK ----
# create a new flask app
print('setup FLASK')
app = Flask(__name__)
# create the first route
@app.route('/')

def index():

    return render_template("index.html", fig = "clustering.html")

@app.route('/clustering')
def plot_kmeans():
    print('running kmeans')
    year = int(request.args.get('years'))
    print(year)
    plot_indsc = Kmean_Olympics(olympics_df,year)
    plot_indsc.write_html("static/images/clustering.html")
    return redirect('/', code=302)
    
if __name__=='__main__':
    app.run(debug=True)
