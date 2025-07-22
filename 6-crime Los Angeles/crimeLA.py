# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataframes
crime = pd.read_csv('data/crimes.csv')
print(crime.head())

# Question 1: find the hour with the highest frequency of crimes and store in int variable 'peak_crime_hour'
