import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load and clean dataframes
workout = pd.read_csv("data/workout.csv")
keywords = pd.read_csv("data/three_keywords.csv")
geo = pd.read_csv("data/workout_geo.csv")
words_geo = pd.read_csv("data/three_keywords_geo.csv")
# Remove rows without valid data
geo.dropna(inplace=True)
words_geo.dropna(inplace=True)

# 1: Year of peak interest on "workout" 
workout['year'] = workout['month'].str.split('-').str[0]
search_summary = workout.groupby('year')['workout_worldwide'].agg(['max', 'mean']).sort_values(by='max', ascending=False).reset_index()
print('Popularity of search for "workout" keyword per year')
print(search_summary)
year_str = search_summary['year'].iloc[0]
print('The year interest in word "workout" reached its peak was', year_str)
# For graphical visualisation
search_summary.sort_values(by='year', inplace=True)
fig1, [ax1, ax2] = plt.subplots(nrows=2, ncols=1)
fig1.set_size_inches(12, 9)
ax1.bar(search_summary['year'], search_summary['mean'])
ax1.set_title('Mean interest in keyword "workout" per year')

workout['month'] = pd.to_datetime(workout['month'])
ax2.plot(workout['month'], workout['workout_worldwide'])
ax2.set_ylabel('Index for popularity of word "workout"')
ax2.tick_params(rotation=90)
ax2.set_title('Evolution of search index for "workout" along the years')

# 2: Find most popular keyword during covid and now
keywords['month'] = pd.to_datetime(keywords['month'])
fig2, ax3 = plt.subplots()
ax3.plot(keywords['month'], keywords['home_workout_worldwide'], label='home workout')
ax3.plot(keywords['month'], keywords['gym_workout_worldwide'], label='gym workout')
ax3.plot(keywords['month'], keywords['home_gym_worldwide'], label='home gym')
ax3.set_title('Popularity of keywords over period of time')
ax3.legend()
# Covid pandemic period according to WHO: 30/01/2020 to 05/05/2023
# Analysing the graphs we can conclude:
peak_covid = 'home workout'
current = 'gym workout'

# 3: Find country with highest interest for workouts among: United States, Australia and Japan
# Filter the selected countries
selected_countries = ['United States', 'Australia', 'Japan']
geo = geo[geo['country'].isin(selected_countries)]
# Find row
top_country = geo[(geo['workout_2018_2023'] == geo['workout_2018_2023'].max())]['country'].tolist()[0]
print('\nCountry with highest interest in workouts is', top_country)
print(geo)

# 4: Find, between Philippines and Malaysia which country has highest interest in home workouts
 

plt.show()
