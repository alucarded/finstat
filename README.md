# Features
Currently the app does (more or less) the following:
1) Downloads CSV economic data from European Central Bank Statistical Warehouse ( http://sdw.ecb.europa.eu/ ) and FRED Economic Data ( https://fred.stlouisfed.org/ )
2) Processes them and interpolates missing values
3) Plots the time series data with Plotly in Django webapp

# Installation
Python 3.x is required. Pip3 is recommended to install dependencies:
pip3 install -r finstat_web/finstat/requirements.txt

# Windows
Run Power Shell script under finstat_web/finstat

# Linux
Run shell script under finstat_web/finstat

