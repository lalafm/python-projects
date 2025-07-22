# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataframes
crime = pd.read_csv('data/crimes.csv', dtype={"TIME OCC": str})
print(crime.info())

# Question 1: find the hour with the highest frequency of crimes and store in int variable 'peak_crime_hour'
# Select hour part of time string and convert to integer
crime['HOUR'] = crime['TIME OCC'].str[:2].astype(int)
# Count the number of entries for each day hour (descending result)
peak_crime_hour = crime.value_counts('HOUR').index[0]
print(f'Peak crime hour is: {peak_crime_hour}h')
plt.figure(1)
ax = sns.countplot(x='HOUR', data=crime)
ax.set_title("Count of crimes commited versus hour of the day")

# Question 2: find area with the largest frequency of night crimes (crimes committed between 10pm and 3:59am) and save in variable 'peak_night_crime_location'
# Filter dataframe to include only night-time crimes
night_crime = crime[(crime['HOUR'] >= 22) | (crime['HOUR'] < 4)]
# Find the count of crimes per area (descending result)
peak_night_crime_location = night_crime.value_counts('AREA NAME').index[0]
print(f'The area with highest occurence of night crime is: {peak_night_crime_location}')
plt.figure(2)
ax2 = sns.countplot(x='AREA NAME', data=night_crime)
ax2.set_title("Count of night-time crimes commited in each city area")
plt.xticks(rotation=45)

# Question 3: identify the number of crimes committed against victims of different age groups and save it in panda series 'victim_ages'
# Set bins for age ranges, upper value of each bin is inclusive
age_bins = [0, 17, 25, 34, 44, 54, 64, crime['Vict Age'].max()]
# Set the age group labels
age_labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]
# Create new column for age category and count the entries for each group
crime['Age Category'] = pd.cut(crime['Vict Age'], labels=age_labels, bins=age_bins)
victim_ages = crime['Age Category'].value_counts()
print('\n Crime count per age category:')
print(victim_ages)

plt.show()