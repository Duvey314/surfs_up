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

# create the engine for our sql database
engine = create_engine('sqlite:///hawaii.sqlite')
# set a base class for an automap schema
Base = automap_base()
# reflect an existing database into a new model
Base.prepare(engine, reflect = True)

# Create our session (link) from Python to the DB
session = Session(engine)

# check the keys for the class
print(Base.classes.keys())