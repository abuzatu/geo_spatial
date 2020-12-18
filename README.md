# General

Created by Adrian Buzatu on 03 Dec 2020, to create several examples of code dealing with geo spatial datasets, with or without a time series component.

# Set up the Python environment the first time

There are two options: with `virtualenv` or with `pyenv`.

## With virtualenv

Install `virtualenv`, if you do not have it already.
```
pip3 install virtualenv
```

Create a virtual environment
```
virtualenv env_geo_spatial
```

Activate the environment
```
source env_geo_spatial/bin/activate
python --version
```
## With pyenv

Choose which version of Python you want to use for this project.
```
pyenv local 3.9.0
python --version
```

## Install the Python packages needed

In either of the two cases above, install the basic packages python packages needed for this project
```
pip install -r requirements.txt
```

When a new package is not here, install it with
```
pip install jupyter
pip install numpy
pip install pandas
pip install matplotlib
pip install seaborn
pip install sklearn
pip install folium
pip install geopandas
pip install ortools
pip install plotly
pip install descartes
```

After you finished installing all the new packages, save the current environment status to a `requirements.txt` file with
```
pip freeze > requirements.txt
```
# How to set up after the first time

For all the other times, simply activate the python environment first 

## With virtualenv

Go to the folder and activate the python environment
```
cd env_geo_spatial
source env_geo_spatial/bin/activate
```

## With pyenv

Simply go to the folder and there is nothing more to to do. In the folder there is a file `.python-version` that stores the information of what Python version is used.

```
less .python-version
```

# Structure

There are several projects with examples that use geo-spatial data, with or without time series. The common functions to all are described in `utils.py`. Individual additions are in specific utils to each project. 

In each project There are three types of files:

* `.py` util files (helper files) with the common functions to be used in .py and .ipynb
* `.py` files that use the helper functions from the utils
* `.ipynb` files Jupyter Notebook files that also use the helper functions from the utils

There are several folders:

* input folder, empty, to add later data
* output folder, empty, to add later plots, result files

# Run the files

Run the regular `.py` with
```
python skeleton.py
```

Run the Jupyter Notebook
```
jupyter skeleton.ipynb
Kernel -> Restart & Clear Output
Kernel -> Restart & Run All
```
