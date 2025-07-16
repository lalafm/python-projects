import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

workout = pd.read_csv("data/workout.csv")
keywords = pd.read_csv("data/three_keywords.csv")
geo = pd.read_csv("data/workout_geo.csv")

# 1: Year of peak interest on "workout" 
workout['year'] = workout['month'].str.split('-').str[0]
search_summary = workout.groupby('year')['workout_worldwide'].agg(['max', 'mean']).sort_values(by='max', ascending=False).reset_index()
print('Popularity of search for "workout" keyword')
print(search_summary)
year_str = search_summary['year'].iloc[0]
print('The year interest in word "workout" reached its peak was', year_str)
# For graphical visualisation
search_summary.sort_values(by='year', inplace=True)
fig1, [ax1, ax2] = plt.subplots(nrows=2, ncols=1)
fig1.set_size_inches(12, 9)
ax1.bar(search_summary['year'], search_summary['mean'])
ax1.set_title('Mean interest in keyword "workout" per year')

workout['month'] = pd.to_datetime(workout['month'])#np.asarray(workout['month'], dtype='datetime64[s]')
ax2.plot(workout['month'], workout['workout_worldwide'])
ax2.set_ylabel('Index for popularity of word "workout"')
ax2.tick_params(rotation=90)
ax2.set_title('Evolution of search index for "workout" along the years')

# 2: Find most popular keyword during covid and now


# 3: Find country with highest interest for workouts among: United States, Australia and Japan


# 4: Find, between Philippines and Malaysia which country has highest interest in home workouts
 
 
plt.show()
