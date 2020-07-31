# plotting dependencies
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt

# data analysis dependencies
import numpy as np
import pandas as pd

# other
import datetime as dt

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# import Flask
from flask import Flask, jsonify

# create the engine for our sql database
engine = create_engine('sqlite:///hawaii.sqlite')
# set a base class for an automap schema
Base = automap_base()
# reflect an existing database into a new model
Base.prepare(engine, reflect = True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# create a flask application called app
app = Flask(__name__)

# define the welcome route
@app.route("/")

def welcome():
    '''
    Welcome is a routing function. The return statement will have f-strings as a reference to all of the other routes. 
    '''
    return(
    '''
    Welcome to the Climate Analysis API!</br>
    Available Routes:</br>
    /api/v1.0/precipitation</br>
    /api/v1.0/stations</br>
    /api/v1.0/tobs</br>
    /api/v1.0/temp/start/end
    ''' )

@app.route("/api/v1.0/precipitation")

def precipitation():
    '''Returns the precipitation data for the last year'''
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
	filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

@app.route("/api/v1.0/stations")

def stations():
    '''returns a list of all the stations'''
    active_stations = session.query(Measurement.station, func.count(Measurement.station)).\
            group_by(Measurement.station).\
            order_by(func.count(Measurement.station).desc()).all()
    return jsonify(active_stations)
    # def stations():
    # results = session.query(Station.station).all()
    # stations = list(np.ravel(results))
    # return jsonify(stations=stations)

@app.route("/api/v1.0/tobs")

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    
    # unravel the results into a one-dimensional array and convert that array into a list
    temps = list(np.ravel(results))

    return jsonify(temps = temps)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def range(start=None,end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    # if there is no end date selected
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)
    
    # if there is an end date
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
    
if __name__ == "__main__":
    # @TODO: Create your app.run statement here
    app.run()