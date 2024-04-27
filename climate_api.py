#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  climate_api.py
 #
 #  File Description:
 #      This Python script, climate_api.py, is a Flask API based on the queries in
 #      climate_analysis.ipynb.  
 #
 #      Here is a list of the functions for each route:
 #
 #      all_available_routes
 #      precipitation
 #      stations
 #      tobs
 #      start_route
 #      start_end_route
 #      
 #      Here is a list of support functions:
 #      
 #      return_most_active_station_id
 #      return_prior_date_one_year
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  09/06/2023      Initial Development                     Nicholas J. George
 #
 #******************************************************************************************/

import climate_analysis_constants

import timex

import datetime as dt
import numpy as np

from flask import Flask, jsonify
from flask_cors import CORS

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'climate_api.py'


# In[3]:


#################################################
# Database Setup
#################################################

# This line of code generates the engine to the correct sqlite file.
engine_sqlalchemy = create_engine(climate_analysis_constants.CONSTANT_SQLITE_DATABASE_FILE)

# This line of code sets up an existing database schema for reflection 
# into a new model.
base_classes_sqlalchemy = automap_base()

# This line of code reflects the database tables.
base_classes_sqlalchemy.prepare(autoload_with = engine_sqlalchemy)

# These lines of code save the references to the station and measurement 
# tables.
stations_class_sqlalchemy = base_classes_sqlalchemy.classes.station

measurements_class_sqlalchemy = base_classes_sqlalchemy.classes.measurement

# Each function correctly creates and binds the session 
# between the python app and database (see below).


# In[4]:


#################################################
# Flask Setup
#################################################
flask_app = Flask(__name__)

flask_app.json.sort_keys = False

CORS(flask_app)


# In[5]:


#################################################
# Support Functions
#################################################

#*******************************************************************************************
 #
 #  Function Name:  return_most_active_station_id
 #
 #  Function Description:
 #      This function returns the ID for the most active station.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/06/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_most_active_station_id():
    
    session_sqlalchemy = Session(engine_sqlalchemy)
        
    query_result_tuple_list \
        = session_sqlalchemy \
            .query(measurements_class_sqlalchemy.station, 
                   func.count(measurements_class_sqlalchemy.station)) \
            .group_by(measurements_class_sqlalchemy.station) \
            .order_by(func.count(measurements_class_sqlalchemy.station) \
            .desc()) \
            .all()
        
    session_sqlalchemy.close()

    
    return query_result_tuple_list[0][0]


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  return_prior_date_one_year
 #
 #  Function Description:
 #      This function returns the date one year prior to the most recent date 
 #      in the data set.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/06/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_prior_date_one_year():
    
    session_sqlalchemy = Session(engine_sqlalchemy)
        
    query_results_tuple \
        = session_sqlalchemy \
            .query(measurements_class_sqlalchemy.date) \
            .order_by(measurements_class_sqlalchemy.date.desc()) \
            .first()
        
    session_sqlalchemy.close()
        
    most_recent_date_string = query_results_tuple[0]
    
        
    return timex.return_prior_date_days(most_recent_date_string)


# In[7]:


#################################################
# Flask Routes
#################################################

#*******************************************************************************************
 #
 #  Flask API Route Name:  all_available_routes
 #
 #  Flask API Route Description:
 #      This function is a Flask API route that occurs when the user arrives 
 #      at the route URL, '/'; the route lists all available routes in the
 #      Flask API.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/06/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

@flask_app.route('/')

def all_available_routes():
    
    message_string \
        = 'WELCOME TO THE CLIMATE API!\n' \
        + 'Here is a list of the available routes:\n\n' \
        + '* Precipitation:\n' \
        + '  /api/v1.0/precipitation\n\n' \
        + '* list of Stations:\n' \
        + '  /api/v1.0/stations\n\n' \
        + '* list of temperature observations for the previous year:\n' \
        + '  /api/v1.0/tobs\n\n' \
        + '* To calculate the minimum, average, and maximum temperatures\n' \
        + '  for a specific start date:\n' \
        + '  /api/v1.0/[start_date format:yyyy-mm-dd]\n\n' \
        + '* To calculate the minimum, average, and maximum temperatures\n' \
        + '  for a specific range of dates:\n' \
        + '  /api/v1.0/[start_date format:yyyy-mm-dd]/[end_date format:yyyy-mm-dd]\n\n'

    
    return message_string


# In[8]:


#*******************************************************************************************
 #
 #  Flask API Route Name:  precipitation
 #
 #  Flask API Route Description:
 #      This function is a Flask API route that occurs when the user arrives 
 #      at the precipitaton URL, '/api/v1.0/precipitation'; the route converts 
 #      the query results from the precipitation analysis (id est, retrieve only 
 #      the last 12 months of data) to a dictionary and returns the JSON 
 #      representation to the caller.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/06/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

@flask_app.route('/api/v1.0/precipitation')

def precipitation():

    precipitation_dictionary_list = []

    
    session_sqlalchemy = Session(engine_sqlalchemy)

    # This line of code performs a query to retrieve the last twelve months 
    # of precipitation data.
    query_results_tuple_list \
        = session_sqlalchemy \
            .query(measurements_class_sqlalchemy.date, 
                   measurements_class_sqlalchemy.prcp) \
            .filter(measurements_class_sqlalchemy.date >= return_prior_date_one_year()) \
            .all()
    
    session_sqlalchemy.close()

            
    precipitation_dictionary = {}

    # This line of code creates a dictionary from the data and appends it to a list.
    for date, prcp in query_results_tuple_list:
            
        precipitation_dictionary['date'] = date
        
        precipitation_dictionary['prcp'] = prcp
        
        precipitation_dictionary_list.append(precipitation_dictionary)

    
    # This line of code returns the JSON representation of the dictionary.
    return jsonify(precipitation_dictionary_list)


# In[9]:


#*******************************************************************************************
 #
 #  Flask API Route Name:  stations
 #
 #  Flask API Route Description:
 #      This function is a Flask API route that occurs when the user arrives 
 #      at the stations URL, '/api/v1.0/stations'; the route returns to the 
 #      caller the JSON representation of a list of stations.
 #
 #
 #  Return Type: list
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/06/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

@flask_app.route('/api/v1.0/stations')

def stations():

    session_sqlalchemy = Session(engine_sqlalchemy)
    
    # This line of code performs a query to retrieve a list of stations.
    query_results_tuple_list \
        = session_sqlalchemy \
            .query(stations_class_sqlalchemy.station) \
            .order_by(stations_class_sqlalchemy.station) \
            .all()

    session_sqlalchemy.close()

    
    # This line of code converts the list of SQLAlchemy Row Objects into a normal list.
    station_dictionary_list = list(np.ravel(query_results_tuple_list))

    
    return jsonify(station_dictionary_list)


# In[10]:


#*******************************************************************************************
 #
 #  Flask API Route Name:  tobs
 #
 #  Flask API Route Description:
 #      This function is a Flask API route that occurs when the user arrives 
 #      at the tobs URL, '/api/v1.0/tobs'; the route converts the query result 
 #      with the dates and temperature observations of the most active station
 #      for the previous year to a dictionary and returns the JSON representation 
 #      to the caller.
 #
 #
 #  Return Type: list
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/06/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

@flask_app.route('/api/v1.0/tobs')

def tobs():
    
    tobs_active_station_dictionary_list = []

    
    session_sqlalchemy = Session(engine_sqlalchemy)

    # This line of code performs a query to retrieve the dates 
    # and temperature observations from the most active station.
    query_results_tuple_list \
        = session_sqlalchemy \
            .query(measurements_class_sqlalchemy.date,
                   measurements_class_sqlalchemy.tobs,
                   measurements_class_sqlalchemy.prcp) \
            .filter(measurements_class_sqlalchemy.date >= return_prior_date_one_year()) \
            .filter(measurements_class_sqlalchemy.station == return_most_active_station_id()) \
            .order_by(measurements_class_sqlalchemy.date) \
            .all()

    session_sqlalchemy.close()

    
    tobs_dictionary = {}
    
    # This line of code creates a dictionary from the data and appends it to a list.
    for date, tobs, prcp in query_results_tuple_list:
        
        tobs_dictionary['date'] = date
        
        tobs_dictionary['tobs'] = tobs
        
        tobs_dictionary['prcp'] = prcp
        
        tobs_active_station_dictionary_list.append(tobs_dictionary)

    
    # This line of code returns the JSON representation of the dictionary.
    return jsonify(tobs_active_station_dictionary_list)


# In[11]:


#*******************************************************************************************
 #
 #  Flask API Route Name:  start_route
 #
 #  Flask API Route Description:
 #      This function is a Flask API route that occurs when the user arrives 
 #      at the start URL, '/api/v1.0/<start_date>'; the route returns a JSON 
 #      list of the minimum, maximum, and average temperatures for a specified 
 #      start date.
 #
 #
 #  Return Type: list
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  start_date_string
 #                          The parameter is the start date of the query.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/06/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

@flask_app.route('/api/v1.0/<start_date>')

def start_route(start_date_string):
   
    temperatures_dictionary_list = []

    
    session_sqlalchemy = Session(engine_sqlalchemy)

    # This line of code performs a query to retrieve the temperature metrics
    # based on a start date.
    query_results_tuple_list \
        = session_sqlalchemy \
            .query(func.min(measurements_class_sqlalchemy.tobs), 
                   func.max(measurements_class_sqlalchemy.tobs), 
                   func.avg(measurements_class_sqlalchemy.tobs)) \
            .filter(measurements_class_sqlalchemy.date >= startDateString) \
            .all()

    session_sqlalchemy.close()

    
    temperatures_dictionary = {}

    # This line of code creates a dictionary from the data and appends it 
    # to a list.
    for min_temp, max_temp, avg_temp in query_results_tuple_list:
            
        temperatures_dictionary['min_temp'] = min_temp
        
        temperatures_dictionary['max_temp'] = max_temp
        
        temperatures_dictionary['avg_temp'] = avg_temp
        
        temperatures_dictionary_list.append(temperatures_dictionary)

    
    # This line of code returns the JSON representation of the dictionary.
    return jsonify(temperatures_dictionary_list)


# In[12]:


#*******************************************************************************************
 #
 #  Flask API Route Name:  start_end_route
 #
 #  Flask API Route Description:
 #      This function is a Flask API route that occurs when the user arrives 
 #      at the start/end URL, ''/api/v1.0/<start_date>/<end_date>''; the route 
 #      returns a JSON list of the minimum, maximum, and average temperatures 
 #      for a specified date range.
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String
 #          startDateString
 #                          This input parameter is the start date of the query.
 #  String
 #          endDateString
 #                          This input parameter is the end date of the query.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/06/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

@flask_app.route('/api/v1.0/<start_date>/<end_date>')

def start_end_route \
        (startDateString, 
         endDateString):
    
    temperatures_dictionary_list \
        = []

            
    session_sqlalchemy = Session(engine_sqlalchemy)

    # This line of code performs a query to retrieve the temperature metrics
    # based on a date range.
    query_results_tuple_list \
        = session_sqlalchemy \
            .query(func.min(measurements_class_sqlalchemy.tobs), 
                   func.max(measurements_class_sqlalchemy.tobs), 
                   func.avg(measurements_class_sqlalchemy.tobs)) \
            .filter(measurements_class_sqlalchemy.date >= startDateString) \
            .filter(measurements_class_sqlalchemy.date <= endDateString) \
            .all()

    session_sqlalchemy.close()

    
    temperatures_dictionary = {}
            
    # This line of code creates a dictionary from the data and appends it 
    # to a list.
    for min_temp, max_temp, avg_temp in query_results_tuple_list:
        
        temperatures_dictionary['min_temp'] = min_temp
        
        temperatures_dictionary['max_temp'] = max_temp
        
        temperatures_dictionary['avg_temp'] = avg_temp
        
        temperatures_dictionary_list.append(temperatures_dictionary)

            
    # This line of code returns the JSON representation of the dictionary.
    return jsonify(temperatures_dictionary_list)


# In[ ]:


if __name__ == '__main__': 
    
    flask_app.run(port = 5000, debug = False)


# In[ ]:




