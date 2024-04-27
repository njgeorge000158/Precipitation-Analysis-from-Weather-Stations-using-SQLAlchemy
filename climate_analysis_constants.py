#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  climate_analysis_constants.py
 #
 #  File Description:
 #      This Python script, climate_analysis_constants.py, contains generic Python 
 #      constants for completing tasks in the IPython Notebook, climate_analysis.ipynb.
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  04/11/2024      Initial Development                     Nicholas J. George
 #
 #******************************************************************************************/


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'climate_analysis_constants.py'


# In[3]:


CONSTANT_SQLITE_DATABASE_FILE = 'sqlite:///resources/hawaii.sqlite'

year_string_list = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017*']

first_dates_string_list \
    = ['2010-01-01', '2011-01-01', '2012-01-01', '2013-01-01', '2014-01-01',
       '2015-01-01', '2016-01-01', '2017-01-01']

last_dates_string_list \
    = ['2010-12-31', '2011-12-31', '2012-12-31', '2013-12-31', '2014-12-31',
       '2015-12-31', '2016-12-31', '2017-08-23']

total_precipitation_dictionary \
    = {'2010': 0.0,
       '2011': 0.0,
       '2012': 0.0,
       '2013': 0.0,
       '2014': 0.0,
       '2015': 0.0,
       '2016': 0.0,
       '2017*': 0.0}


# In[ ]:




