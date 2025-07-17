# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load dataframes
nobel = pd.read_csv('data/nobel.csv')

# Question 1: find the most commonly awarded gender and birth country
nobel_gender = nobel['sex'].value_counts(sort=True, ascending=False)
print('Nobel prize winners gender:')
print(nobel_gender)
top_gender = nobel_gender.index[0]
if nobel_gender['Male'] != nobel_gender['Female']:
    print('Top gender is:', top_gender)
else:
    print('Both genders won the same amount of times')
    top_gender = 'Male and Female'

nobel_country = nobel['birth_country'].value_counts(sort=True, ascending=False)
print('\nNobel prize winners birth countries distribution:')
print(nobel_country)
new_max = 0
top_country = ''
print('\nTop country:')
for i in range(len(nobel_country)):
    if(nobel_country.iloc[i] > new_max):
        if i > 0:
            top_country += ', ' 
        top_country += nobel_country.index[i]
        print(top_country)
        new_max = nobel_country.iloc[i]
    else:
        break

# Question 2
nobel['decade'] = np.floor(nobel['year'] / 10)
usa_winners = nobel[nobel['birth_country'] == 'United States of America']
ratios = (usa_winners['decade'].value_counts() / nobel['decade'].value_counts())
print(ratios)
max_decade_usa = int(ratios[ratios == ratios.max()].index[0])

# To visualize the proportions
fig1, ax1 = plt.subplots()
ax1.bar(ratios.index, nobel['decade'].value_counts().sort_index(), label='Total winners')
ax1.bar(ratios.index, usa_winners['decade'].value_counts().sort_index(), label='USA winners')
ax1.set_xlabel('Decade')
ax1.set_ylabel('Count')
ax1.legend()

# Question 3

# Question 4

# Question 5


plt.show()