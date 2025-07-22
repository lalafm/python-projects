# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load dataframes
lego_sets = pd.read_csv('data/lego_sets.csv')
parent_themes = pd.read_csv('data/parent_themes.csv')

# Clean data
lego_sets.dropna(subset=['set_num'], inplace=True)

# Question 1: find the percentage of all licensed sets ever released that were Star Wars theme and save it in an int variable called the_force
# Join the dataframes to have a column with the license information
lego = lego_sets.merge(parent_themes,left_on='parent_theme', right_on='name', suffixes=('_set', '_parent')).drop(['id', 'name_parent'], axis=1)
# Filter dataframe to have total of licensed and total of Star Wars sets
lego_licensed = lego[lego['is_licensed']]
lego_star_wars = lego_licensed[lego_licensed['parent_theme']=='Star Wars']
the_force = len(lego_star_wars) * 100 // len(lego_licensed)
print(f'{the_force}% of the licensed sets are Star Wars')

lego_licensed['parent_theme'].value_counts().plot(kind="bar")
plt.title("Licensed Lego sets produced")

# Question 2: find in which year was the highest number of Star Wars sets released, save it in an int variable called new_era
new_era = lego_star_wars['year'].value_counts().index[0]
print(f'{new_era} was the year with the highest number of Lego Star Wars sets released')

plt.show()
