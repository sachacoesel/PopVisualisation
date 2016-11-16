# import packages
import zipfile
import pandas as pd
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
import numpy as np


def get_deepDOM_data():
	"""
	extract deepDOM data into a dataframe
	"""
	zf = zipfile.ZipFile('stat-v2.csv.zip')
	file_handle = zf.open('stat-v2.csv')
	return pd.read_csv(file_handle)

def population_abundance_per_day():
    """
    use DatetimeIndex to make pivot table grouped by day and population
    """
    data = get_deepDOM_data()
    # Use DatetimeIndex to make a datetime column
    datetime = pd.DatetimeIndex(data['time'])
    # Group data by date and population using a pivot table
    return data.pivot_table('abundance', aggfunc='sum', index = [datetime.date, datetime.hour], columns='pop')

def plot_populations_per_day():
    """
    Plot the population numbers per day against time 
    """
    data = population_abundance_per_day()
    fig, ax = plt.subplots(4, figsize=(14,8), sharex=True)
    data['prochloro'].plot(ax=ax[0], title='prochloro')
    data['synecho'].plot(ax=ax[1], title='synecho')
    data['picoeuk'].plot(ax=ax[2], title='picoeuk')
    data['unknown'].plot(ax=ax[3], title='other')
    fig.savefig('population_abundance_per_day.png')

def population_abundance_per_hour():
    """
    use DatetimeIndex to make pivot table grouped by day and population
    """
    data = get_deepDOM_data()
    # Use DatetimeIndex to make a datetime column
    datetime = pd.DatetimeIndex(data['time'])
    # Group data by date and population using a pivot table
    return data.pivot_table('abundance', aggfunc='mean', index = datetime.hour, columns='pop')

def plot_populations_per_hour():
    """
    Plot the population numbers per hour against time 
    """
    data = population_abundance_per_hour()
    fig, ax = plt.subplots(4, figsize=(14,8), sharex=True)
    data['prochloro'].plot(ax=ax[0], title='prochloro')
    data['synecho'].plot(ax=ax[1], title='synecho')
    data['picoeuk'].plot(ax=ax[2], title='picoeuk')
    data['unknown'].plot(ax=ax[3], title='other')
    fig.savefig('population_abundance_per_hour.png')
