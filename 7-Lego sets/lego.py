# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataframes
lego_sets = pd.read_csv('data/lego_sets.csv')
themes = pd.read_csv('data/parent_themes.csv')

# Clean data
lego_sets.dropna(subset=['set_num'], inplace=True)
print(lego_sets.info())

# Question 1: find the percentage of all licensed sets ever released that were Star Wars theme and save it in an int variable called the_force
# Join the dataframes to have a column with the license information
lego = lego_sets.merge(themes,left_on='parent_theme', right_on='name', suffixes=('_set', '_parent')).drop(['id', 'name_parent'], axis=1)

# Filter dataframe to have total of licensed
lego_licensed = lego[lego['is_licensed']]
the_force = len(lego_licensed[lego_licensed['parent_theme']=='Star Wars']) * 100 // len(lego_licensed)
print(f'{the_force}% of the licensed sets are Star Wars')