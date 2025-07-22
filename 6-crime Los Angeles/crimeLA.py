# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataframes
crime = pd.read_csv('data/crimes.csv', dtype={"TIME OCC": str})

# Question 1: find the hour with the highest frequency of crimes and store in int variable 'peak_crime_hour'
crime['hour'] = crime['TIME OCC'].str[:2].astype(int)
peak_crime_hour = crime.value_counts('hour').index[0]
print(f'Peak crime hour is: {peak_crime_hour}h')