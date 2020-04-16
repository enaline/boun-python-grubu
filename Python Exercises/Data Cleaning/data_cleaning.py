# -*- coding: utf-8 -*-
"""
Author: Cihan
Edited for PEP-8: Berk
"""

# ##Getting Started

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime as dt
import missingno as msno

# Read in the dataset
airbnb = pd.read_csv(
    'https://github.com/adelnehme/python-for-spreadsheet-users-webinar/blob/master/datasets/airbnb.csv?raw=true',
    index_col='Unnamed: 0')

# ##Diagnosing data cleaning problems using simple pandas and visualizations

# Print the header of the DataFrame
airbnb.head()

# Print data types of DataFrame
airbnb.dtypes

# Print info of DataFrame
airbnb.info()

# Print number of missing values
airbnb.isna()
airbnb.isna().sum()

# Print description of DataFrame
airbnb.describe()

# Visualize the distribution of the rating column
sns.distplot(airbnb['rating'], bins=20)
plt.title('Distribution of listing ratings')
plt.show()

# Find number of unique values in room_type column
airbnb['room_type'].unique()

# How many values of different room_types do we have?
airbnb['room_type'].value_counts()

# ##Cleaning Data

# Reminder of the DataFrame
airbnb.head()

# #Task 1: Split coordinates into 2 columns and convert them to float

# Remove "(" and ")" from coordinates
airbnb['coordinates'] = airbnb['coordinates'].str.replace("(", "")
airbnb['coordinates'] = airbnb['coordinates'].str.replace(")", "")

# Print the header of the column
airbnb.coordinates.head()

# Split column into two
lat_long = airbnb['coordinates'].str.split(",", expand=True)
lat_long.head()

# Assign correct columns to latitude and longitude columns in airbnb
airbnb['latitude'] = lat_long[0]
airbnb['longitude'] = lat_long[1]

# Print the header and confirm new column creation
airbnb.head()

# Print out dtypes again
airbnb.dtypes

# Convert latitude and longitude to float
airbnb['latitude'] = airbnb['latitude'].astype('float')
airbnb['longitude'] = airbnb['longitude'].astype('float')

# Print dtypes again
airbnb.dtypes

# Drop coordinates column
airbnb.drop('coordinates', axis=1, inplace=True)

# #Task 2: Remove $ from price and convert it to float

# Calculate mean of price without conversion
airbnb.price.mean()

# Remove $ from price before conversion to float
airbnb.price = airbnb.price.str.strip('$')

# Print header to make sure change was done
airbnb.price.head()

# Convert price to float
airbnb.price = airbnb.price.astype('float')

# Calculate mean of price after conversion
airbnb.price.mean()

# Visualize distribution of prices
sns.distplot(airbnb['price'], bins=20)
plt.show()

# #Task 3: Convert listing_added and last_review columns to datetime

# Print header of two columns
airbnb[['listing_added', 'last_review']].head()

# Convert both columns to datetime
airbnb['listing_added'] = pd.to_datetime(airbnb['listing_added'], format='%Y-%m-%d')
airbnb['last_review'] = pd.to_datetime(airbnb['last_review'], format='%Y-%m-%d')

# Print header and datatypes of both columns again
airbnb[['listing_added', 'last_review']].head()
airbnb[['listing_added', 'last_review']].dtypes

# #Task 4: We need to collapse room_type into correct categories

# Print unique values of `room_type`
airbnb.room_type.unique()

# Deal with capitalized values
airbnb['room_type'] = airbnb['room_type'].str.lower()

# Deal with trailing spaces
airbnb['room_type'] = airbnb['room_type'].str.strip()

# Replace values to 'Shared room', 'Entire place', 'Private room' and 'Hotel room' (if applicable).
mappings = {'private room': 'Private Room',
            'private': 'Private Room',
            'entire home/apt': 'Entire Place',
            'shared room': 'Shared Room',
            'home': 'Entire Place'}

# Replace values and collapse data
airbnb['room_type'] = airbnb['room_type'].replace(mappings)
airbnb.room_type.unique()

# #Task 5: Divide neighbourhood_full into 2 columns and making sure they are clean

# Print header of column
airbnb.neighbourhood_full.head()

# Split neighbourhood_full
borough_neighbourhood = airbnb.neighbourhood_full.str.split(",", expand=True)

# Create borough and neighbourhood columns
airbnb['borough'] = borough_neighbourhood[0]
airbnb['neighbourhood'] = borough_neighbourhood[1]

# Print header of columns
airbnb[['borough', 'neighbourhood']].head()

# Drop neighbourhood_full column
airbnb.drop('neighbourhood_full', axis=1, inplace=True)

# Print out unique values of borough and neighbourhood
airbnb['borough'].unique()
airbnb['neighbourhood'].unique()

# Strip white space from neighbourhood column
airbnb.neighbourhood = airbnb.neighbourhood.str.strip()

# Print unique values again
airbnb['neighbourhood'].unique()

# #Task 6: Make sure we set the correct maximum for rating column out of range values

# Visualize the rating column again
sns.distplot(airbnb.rating, bins=20)
plt.show()

# Isolate rows of rating > 5.0
airbnb[airbnb['rating'] > 5]

# Drop these rows and make sure we have effected changes
airbnb.drop(airbnb[airbnb['rating'] > 5].index, inplace=True, axis=0)

# Visualize the rating column again
sns.distplot(airbnb.rating, bins=20)
plt.show()

# Get the maximum
airbnb.rating.max()

# #Task 7: Understand the type of missing data, and deal with the missing data in most of the remaining columns.

# Visualize the missing data
msno.matrix(airbnb)
plt.show()

# Visualize the missing data on sorted values
msno.matrix(airbnb.sort_values(by='rating'))
plt.show()

# Missing data bar plot
msno.bar(airbnb)
plt.show()

# Understand DataFrame with missing values in rating, number_of_stays, 5_stars, reviews_per_month
airbnb[airbnb['rating'].isna()].describe()

# Understand DataFrame with missing values in rating, number_of_stays, 5_stars, reviews_per_month
airbnb[-airbnb['rating'].isna()].describe()

# Impute missing data
airbnb = airbnb.fillna({'reviews_per_month': 0,
                        'number_of_stays': 0,
                        '5_stars': 0})

# Create is_rated column
is_rated = np.where(airbnb['rating'].isna() == True, 0, 1)
airbnb['is_rated'] = is_rated

# Investigate DataFrame with missing values in price
airbnb[airbnb['price'].isna()].describe()

# Investigate DataFrame with missing values in price
airbnb[-airbnb['price'].isna()].describe()

# Visualize relationship between price and room_type
sns.boxplot(x='room_type', y='price', data=airbnb)
plt.ylim(0, 400)
plt.show()

# Get median price per room_type
airbnb.groupby('room_type').median()['price']

# Impute price based on conditions
airbnb.loc[(airbnb['price'].isna()) & (airbnb['room_type'] == 'Private Room'), 'price'] = 70
airbnb.loc[(airbnb['price'].isna()) & (airbnb['room_type'] == 'Entire Place'), 'price'] = 163
airbnb.loc[(airbnb['price'].isna()) & (airbnb['room_type'] == 'Shared Room'), 'price'] = 50

# Confirm price has been imputed
airbnb.isna().sum()

# # Task 8: Do we have consistent date data?


# Doing some sanity checks on date data
today = dt.date.today()
today
# Are there reviews in the future?
airbnb[airbnb['last_review'].dt.date > today]

# Are there listings in the future?
airbnb[airbnb['listing_added'].dt.date > today]

# Drop these rows since they are only 4 rows
# Omitted in exercise

# Are there any listings with listing_added > last_review
# Omitted in exercise

# Drop these rows since they are only 2 rows
airbnb.drop(inconsistent_dates.index, inplace=True)

# #Task 9: Let's deal with duplicate data

# Print the header of the DataFrame again
airbnb.head()

# Find duplicates
duplicates = airbnb.duplicated(subset='listing_id', keep=False)
print(duplicates)

# Find duplicates
airbnb[duplicates].sort_values('listing_id')

# Remove identical duplicates
airbnb = airbnb.drop_duplicates()

# Find non-identical duplicates
duplicates = airbnb.duplicated(subset='listing_id', keep=False)

# Show all duplicates
airbnb[duplicates].sort_values('listing_id')

# Get column names from airbnb
column_names = airbnb.columns
column_names
# airbnb.groupby('listing_id').agg({'price':'mean','rating':'mean','listing_added':'max','host_id':'first'})

# Create dictionary comprehension with 'first' as value for all columns not being aggregated
aggregations = {column_name: 'first' for column_name in
                column_names.difference(['listing_id', 'listing_added', 'rating', 'price'])}
aggregations['price'] = 'mean'
aggregations['rating'] = 'mean'
aggregations['listing_added'] = 'max'

# Remove non-identical duplicates
airbnb = airbnb.groupby('listing_id').agg(aggregations).reset_index()

# Make sure no duplication happened


# Print header of DataFrame
airbnb.head()
