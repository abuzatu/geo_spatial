import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import logging
import math

# Haversine formula: distance in km along the sphere between two points on a sphere
# https://en.wikipedia.org/wiki/Haversine_formula
def haversine(
    lat1: float,
    lon1: float,
    lat2: float,
    lon2: float,
) -> float:
    '''
    Returns the distance in km along the sphere between two points on a sphere
    from their latitude and longitude coordinates in degrees.
    '''
    # convert from degrees to radians
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    # delta
    delta_lon = lon2 - lon1
    delta_lat = lat2 - lat1
    a = np.sin(delta_lat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(delta_lon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    length = 6367 * c # in km
    return length

def get_distance(lat_lon, lat_lon_reference):
    # result in lat_lon units
    # return np.sqrt((lat_lon[0]-lat_lon_reference[0])**2 + (lat_lon[1]-lat_lon_reference[1])**2)
    # result as length in km
    return haversine(lat_lon[0], lat_lon[1], lat_lon_reference[0], lat_lon_reference[1])

def get_angle_degree(
    lat1: float,
    lon1: float,
    lat2: float,
    lon2: float,
) -> float:
    return np.degrees(np.arctan(((lat2 - lat1)/(lon2 - lon1))))