# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

# Question 2: find the decade with the highest ratio of US-born Nobel Prize winners to total winners in all categories
nobel['decade'] = (np.floor(nobel['year'] / 10) * 10).astype(int)
usa_winners = nobel[nobel['birth_country'] == 'United States of America']
ratios = (usa_winners['decade'].value_counts() / nobel['decade'].value_counts())
print('\nRatio of US-born winners over the decades:')
print(ratios)
max_decade_usa = ratios[ratios == ratios.max()].index[0]

# To visualize the proportions
fig1, ax1 = plt.subplots()
ax1.bar(ratios.index, nobel['decade'].value_counts().sort_index(), label='Total winners', width=5)
ax1.bar(ratios.index, usa_winners['decade'].value_counts().sort_index(), label='USA winners', width=5)
ax1.set_xlabel('Decade')
ax1.set_ylabel('Count')
ax1.legend()

# Question 3: find the decade and Nobel Prize category combination with the highest proportion of female laureates
nobel['female_winners'] = nobel['sex']=='Female'
nobel_grouped = nobel.groupby(['decade', 'category'], as_index=False)['female_winners'].mean().sort_values(by='female_winners', ascending=False)
max_female_dict = {nobel_grouped['decade'].iloc[0]:nobel_grouped['category'].iloc[0]}
print(f'\nThe decade-category with highest prportion of female winners is  {next(iter(max_female_dict.items()))}')

# Question 4: find the first woman to receive a Nobel Prize and in which category
# Filter the dataframe to have only females and sort by year
nobel_fem_filter = nobel[nobel['sex'] == 'Female'].sort_values(by='year')
first_woman_name = nobel_fem_filter['full_name'].iloc[0]
first_woman_category = nobel_fem_filter['category'].iloc[0]
print(f'\nThe first female winner was {first_woman_name} in the category {first_woman_category}')

# Question 5: find which individuals or organizations have won more than one Nobel Prize throughout the years
repeat_list = []
nobel_winners_count = nobel.value_counts('full_name').sort_values(ascending=False)
for i in range(len(nobel_winners_count)):
    if nobel_winners_count[i] > 1:
        repeat_list.append(nobel_winners_count.index[i])
    else:
        break
print("\nCompanies or individuals that won a Nobel prize more than once:")
print(repeat_list)

plt.show()