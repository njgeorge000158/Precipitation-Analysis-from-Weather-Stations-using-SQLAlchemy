# **Precipitation Analysis from Weather Stations using SQLAlchemy**

----

### **Installation:**

----

If the computer has Anaconda, Jupyter Notebook, and a recent version of Python, the IPython notebook already has the following dependencies installed: datetime, io, json, matplotlib, numpy, pandas, pathlib, os, pandas, requests, requests_html, scipy.

In addition to those modules, the IPython notebook needs the following to execute: holoviews, hvplot, geoviews, geopy, aspose-words, dataframe-image, sqlite, sqlalchemy, flask, flask_cors.

Here are the requisite Terminal commands for the installation of these peripheral modules (SQLite is already installed on macOS):

pip3 install -U holoviews

pip3 install -U hvplot

pip3 install -U geoviews

pip3 install -U geopy

pip3 install -U aspose-words

pip3 install -U dataframe-image

pip3 install -U sqlalchemy

pip3 install -U Flask

pip3 install -U flask-cors

----

### **Usage:**

----

The IPython notebook, climate_analysis.ipynb, and Flask API, climate_api.py, use the files in the folder, resources, and will not run without them.  The IPython Notebook and Flask API must have the following Python scripts in the same folder with them:

climate_analysis_constants.py

climate_api.py

logx.py

mathx.py

matplotlibx.py

pandasx.py

timex.py

If the folders, logs and images, are not present, the IPython notebook will create them.  The folder, resources, holds the sqlite database file for the IPython Notebook and Flask API; the folder, logs, contains log files from testing the IPython Notebook; and the folder, images, has the PNG image files of the IPython Notebook's tables and plots.

To place the IPython notebook in Log Mode or Image Mode set the parameter for the appropriate subroutine in coding cell #2 to True. In Log Mode, the notebook writes information to the log file in the folder, logs. If the program is in Image Mode, it writes all DataFrames, hvplot maps, and matplotlib plots to PNG files in the folder, images.

----

### **Resource Summary:**

----

#### Source code

climate_analysis.ipynb, climate_api.py, climate_analysis_constants.py, climate_api.py, logx.py, mathx.py, matplotlibx.py, pandasx.py, timex.py

#### Input files

hawaii.sqlite

#### Output files

n/a

#### SQL script

n/a

#### Software

Flask, Jupyter Notebook, Matplotlib, Numpy, Pandas, Python 3.11.5, SQLite

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

----

### **GitHub Repository Branches:**

----

#### main branch 

|&rarr; [./climate_analysis_constants.py](./climate_analysis_constants.py)

|&rarr; [./climate_analysis.ipynb](./climate_analysis.ipynb)

|&rarr; [./climate_api.py](./climate_api.py)

|&rarr; [./README.TECHNICAL.md](./README.TECHNICAL.md)

|&rarr; [./README.md](./README.md)

|&rarr; [./table-of-contents.md](./table-of-contents.md)

|&rarr; [./images/](./images/)

  &emsp; |&rarr; [./images/climate_analysisFigure24MinimumMaximumandAverageTemperaturesByYear.png](./images/climate_analysisFigure24MinimumMaximumandAverageTemperaturesByYear.png)
  
  &emsp; |&rarr; [./images/climate_analysisFigure32TemperatureObservationsTOBsHistogram2010.png](./images/climate_analysisFigure32TemperatureObservationsTOBsHistogram2010.png)
  
  &emsp; |&rarr; [./images/climate_analysisFigure33TemperatureObservationsTOBsHistogram2011.png](./images/climate_analysisFigure33TemperatureObservationsTOBsHistogram2011.png)
  
  &emsp; |&rarr; [./images/climate_analysisFigure34TemperatureObservationsTOBsHistogram2012.png](./images/climate_analysisFigure34TemperatureObservationsTOBsHistogram2012.png)

  &emsp; |&rarr; [./images/climate_analysisFigure35TemperatureObservationsTOBsHistogram2013.png](./images/climate_analysisFigure35TemperatureObservationsTOBsHistogram2013.png)

  &emsp; |&rarr; [./images/climate_analysisFigure36TemperatureObservationsTOBsHistogram2014.png](./images/climate_analysisFigure36TemperatureObservationsTOBsHistogram2014.png)

  &emsp; |&rarr; [./images/climate_analysisFigure37TemperatureObservationsTOBsHistogram2015.png](./images/climate_analysisFigure37TemperatureObservationsTOBsHistogram2015.png)

  &emsp; |&rarr; [./images/climate_analysisFigure38TemperatureObservationsTOBsHistogram2016.png](./images/climate_analysisFigure38TemperatureObservationsTOBsHistogram2016.png)

  &emsp; |&rarr; [./images/climate_analysisFigure39TemperatureObservationsTOBsHistogram2017.png](./images/climate_analysisFigure39TemperatureObservationsTOBsHistogram2017.png)

  &emsp; |&rarr; [./images/climate_analysisFigure411TotalPrecipitationvsYear.png](./images/climate_analysisFigure411TotalPrecipitationvsYear.png)

  &emsp; |&rarr; [./images/climate_analysisFigure421PrecipitationvsTime2010.png](./images/climate_analysisFigure421PrecipitationvsTime2010.png)

  &emsp; |&rarr; [./images/climate_analysisFigure422PrecipitationHistogram2010.png](./images/climate_analysisFigure422PrecipitationHistogram2010.png)

  &emsp; |&rarr; [./images/climate_analysisFigure431PrecipitationvsTime2011.png](./images/climate_analysisFigure431PrecipitationvsTime2011.png)

  &emsp; |&rarr; [./images/climate_analysisFigure432Precipitation2011Histogram.png](./images/climate_analysisFigure432Precipitation2011Histogram.png)

  &emsp; |&rarr; [./images/climate_analysisFigure441PrecipitationvsTime2012.png](./images/climate_analysisFigure441PrecipitationvsTime2012.png)

  &emsp; |&rarr; [./images/climate_analysisFigure442Precipitation2012Histogram.png](./images/climate_analysisFigure442Precipitation2012Histogram.png)

  &emsp; |&rarr; [./images/climate_analysisFigure451PrecipitationvsTime2013.png](./images/climate_analysisFigure451PrecipitationvsTime2013.png)

  &emsp; |&rarr; [./images/climate_analysisFigure452Precipitation2013Histogram.png](./images/climate_analysisFigure452Precipitation2013Histogram.png)

  &emsp; |&rarr; [./images/climate_analysisFigure461PrecipitationvsTime20144.png](./images/climate_analysisFigure461PrecipitationvsTime2014.png)

  &emsp; |&rarr; [./images/climate_analysisFigure462Precipitation2014Histogram.png](./images/climate_analysisFigure462Precipitation2014Histogram.png)

  &emsp; |&rarr; [./images/climate_analysisFigure471PrecipitationvsTime2015.png](./images/climate_analysisFigure471PrecipitationvsTime2015.png)

  &emsp; |&rarr; [./images/climate_analysisFigure472Precipitation2015Histogram.png](./images/climate_analysisFigure472Precipitation2015Histogram.png)

  &emsp; |&rarr; [./images/climate_analysisFigure481PrecipitationvsTime2016.png](./images/climate_analysisFigure481PrecipitationvsTime2016.png)

  &emsp; |&rarr; [./images/climate_analysisFigure482Precipitation2016Histogram.png](./images/climate_analysisFigure482Precipitation2016Histogram.png)

  &emsp; |&rarr; [./images/climate_analysisFigure491PrecipitationvsTime20178Months.png](./images/climate_analysisFigure491PrecipitationvsTime20178Months.png)

  &emsp; |&rarr; [./images/climate_analysisFigure492Precipitation20178MonthsHistogram.png](./images/climate_analysisFigure492Precipitation20178MonthsHistogram.png)

  &emsp; |&rarr; [./images/climate_analysisFigure3101TemperatureObservationsTOBsHistograms20102017.png](./images/climate_analysisFigure3101TemperatureObservationsTOBsHistograms20102017.png)

  &emsp; |&rarr; [./images/climate_analysisFigure3102TemperatureObservationsTOBsDistribution.png](./images/climate_analysisFigure3102TemperatureObservationsTOBsDistribution.png)

  &emsp; |&rarr; [./images/climate_analysisFigure4101PrecipitationvsTime20102017.png](./images/climate_analysisFigure4101PrecipitationvsTime20102017.png)

  &emsp; |&rarr; [./images/climate_analysisFigure4102PrecipitationHistograms20102017.png](./images/climate_analysisFigure4102PrecipitationHistograms20102017.png)

  &emsp; |&rarr; [./images/climate_analysisFigure4103PrecipitationDistribution20102017.png](./images/climate_analysisFigure4103PrecipitationDistribution20102017.png)

  &emsp; |&rarr; [./images/climate_analysisTable23MostActiveStationIDsandTOBSByYear.png](./images/climate_analysisTable23MostActiveStationIDsandTOBSByYear.png)

  &emsp; |&rarr; [./images/climate_analysisTable24MinimumMaximumandAverageTemperaturesByYear.png](./images/climate_analysisTable24MinimumMaximumandAverageTemperaturesByYear.png)

  &emsp; |&rarr; [./images/climate_analysisTable32TemperatureObservationsTOBsStatistics2010.png](./images/climate_analysisTable32TemperatureObservationsTOBsStatistics2010.png)

  &emsp; |&rarr; [./images/climate_analysisTable33TemperatureObservationsTOBsStatistics2011.png](./images/climate_analysisTable33TemperatureObservationsTOBsStatistics2011.png)

  &emsp; |&rarr; [./images/climate_analysisTable34TemperatureObservationsTOBsStatistics2012.png](./images/climate_analysisTable34TemperatureObservationsTOBsStatistics2012.png)

  &emsp; |&rarr; [./images/climate_analysisTable35TemperatureObservationsTOBsStatistics2013.png](./images/climate_analysisTable35TemperatureObservationsTOBsStatistics2013.png)

  &emsp; |&rarr; [./images/climate_analysisTable36TemperatureObservationsTOBsStatistics2014.png](./images/climate_analysisTable36TemperatureObservationsTOBsStatistics2014.png)

  &emsp; |&rarr; [./images/climate_analysisTable37TemperatureObservationsTOBsStatistics2015.png](./images/climate_analysisTable37TemperatureObservationsTOBsStatistics2015.png)

  &emsp; |&rarr; [./images/climate_analysisTable38TemperatureObservationsTOBsStatistics2016.png](./images/climate_analysisTable38TemperatureObservationsTOBsStatistics2016.png)

  &emsp; |&rarr; [./images/climate_analysisTable39TemperatureObservationsTOBsStatistics2017.png](./images/climate_analysisTable39TemperatureObservationsTOBsStatistics2017.png)

  &emsp; |&rarr; [./images/climate_analysisTable42Precipitation2010SummaryStatistics.png](./images/climate_analysisTable42Precipitation2010SummaryStatistics.png)

  &emsp; |&rarr; [./images/climate_analysisTable43Precipitation2011SummaryStatistics.png](./images/climate_analysisTable43Precipitation2011SummaryStatistics.png)

  &emsp; |&rarr; [./images/climate_analysisTable44Precipitation2012SummaryStatistics.png](./images/climate_analysisTable44Precipitation2012SummaryStatistics.png)

  &emsp; |&rarr; [./images/climate_analysisTable45Precipitation2013SummaryStatistics.png](./images/climate_analysisTable45Precipitation2013SummaryStatistics.png)

  &emsp; |&rarr; [./images/climate_analysisTable46Precipitation2014SummaryStatistics.png](./images/climate_analysisTable46Precipitation2014SummaryStatistics.png)

  &emsp; |&rarr; [./images/climate_analysisTable47Precipitation2015SummaryStatistics.png](./images/climate_analysisTable47Precipitation2015SummaryStatistics.png)

  &emsp; |&rarr; [./images/climate_analysisTable48Precipitation2016SummaryStatistics.png](./images/climate_analysisTable48Precipitation2016SummaryStatistics.png)

  &emsp; |&rarr; [./images/climate_analysisTable49Precipitation20178MonthsSummaryStatistics.png](./images/climate_analysisTable49Precipitation20178MonthsSummaryStatistics.png)

  &emsp; |&rarr; [./images/climate_analysisTable3102TemperatureObservationsTOBsCorrelationMatrix20102016.png](./images/climate_analysisTable3102TemperatureObservationsTOBsCorrelationMatrix20102016.png)

  &emsp; |&rarr; [./images/ClimatePyTable4101TemperatureObservationsTOBs20102017SummaryStatistics.png](./images/ClimatePyTable4101TemperatureObservationsTOBs20102017SummaryStatistics.png)

  &emsp; |&rarr; [./images/climate_analysisTable4102PrecipitationCorrelationMatrix20102016.png](./images/climate_analysisTable4102PrecipitationCorrelationMatrix20102016.png)

  &emsp; |&rarr; [./images/climate_analysisTable4111TotalPrecipitationinchesvsYear20102017.png](./images/climate_analysisTable4111TotalPrecipitationinchesvsYear20102017.png)

  &emsp; |&rarr; [./images/climate_analysisTable4112TotalPrecipitationStatistics20102017.png](./images/climate_analysisTable4112TotalPrecipitationStatistics20102017.png)

  &emsp; |&rarr; [./images/README.md](./images/README.md)

|&rarr; [./logs/](./logs/)

  &emsp; |&rarr; [./logs/20240426climate_analysis_log.txt](./logs/20240426climate_analysis_log.txt)

  &emsp; |&rarr; [./logs/README.md](./logs/README.md)

|&rarr; [./resources/](./resources/)

  &emsp; |&rarr; [./resources/hawaii.sqlite](./resources/hawaii.sqlite)

  &emsp; |&rarr; [./resources/README.md](./resources/README.md)

----

### **References:**

----

[Flask API documentation](https://flask.palletsprojects.com/en/2.3.x/api/)

[Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/stable/)

[Matplotlib Documentation](https://matplotlib.org/stable/index.html)

[Numpy documentation](https://numpy.org/doc/1.26/)

[Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)

[Python Documentation](https://docs.python.org/3/contents.html)

[SQLite documentation](https://www.sqlite.org/docs.html)

----

### **Authors and Acknowledgment:**

----

### Copyright

Nicholas J. George © 2023. All Rights Reserved.
