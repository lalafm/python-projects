import pandas as pd
import matplotlib.pyplot as plt

# Load data
df_flights = pd.read_csv('data/flights2022.csv') 
df_weather = pd.read_csv('data/flights_weather2022.csv') 
# Explore data
print(df_flights.info())
print(df_weather.info())