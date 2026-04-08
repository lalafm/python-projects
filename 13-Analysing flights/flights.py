import pandas as pd
import matplotlib.pyplot as plt

# Load data
df_flights = pd.read_csv('data/flights2022.csv') 
df_weather = pd.read_csv('data/flights_weather2022.csv') 
# Explore data
print(df_flights.info())
print(df_weather.info())
#1 Create route column from 'origin' and 'dest' and 'is_cancelled' to flag cancelled flights
df_flights['route'] = df_flights['origin'] + '-' + df_flights['dest']
df_flights['is_cancelled'] = df_flights['dep_delay'].isnull()
df_weather['wind_gust_cat'] = df_weather['wind_gust'].apply(lambda x: '>=10 mph' if x>=10 else '<10 mph')
print(df_flights.head())
print(df_weather.head())

#2 Save average departure delays and highest number of canceled flights for routes into dataframe 'routes_delays_cancels'
routes_delays_cancels = df_flights.groupby('route').agg(mean_dep_delay = ('dep_delay', 'mean'), 
                                                         total_cancellations = ('is_cancelled','sum')).reset_index()
print(routes_delays_cancels)

#3 Save average departure delays and highest number of canceled flights for airlines into dataframe 'airlines_delays_cancels'
airlines_delays_cancels = df_flights.groupby('airline').agg(mean_dep_delay = ('dep_delay', 'mean'), 
                                                           total_cancellations = ('is_cancelled', 'sum')).reset_index()
print(airlines_delays_cancels)  

#5 Analyse wind gust and delays relationship. 
# If higher values of wind_gust lead to higher delays for both SEA and PDX airportswind_response should be True
wind_gust = df_weather.groupby(['origin', 'wind_gust_cat']).agg(mean_dep_delay = ('dep_delay', 'mean'))
wind_response = False
if(wind_gust.loc['PDX', '>=10 mph']['mean_dep_delay'] > wind_gust.loc['PDX', '<10 mph']['mean_dep_delay'] and
   wind_gust.loc['SEA', '>=10 mph']['mean_dep_delay'] > wind_gust.loc['SEA', '<10 mph']['mean_dep_delay']):
    wind_response = True
print('Wind analysis') 
print(wind_gust)  
print(f'Wind response: {wind_response}')   

#4 Plot top 9 highest cancelations number per route and highest delays per airline
top9_route_cancels_bar, ax1 = plt.subplots()
top_routes_by_cancellations = routes_delays_cancels.sort_values('total_cancellations', ascending=False).head(9)
ax1.bar(top_routes_by_cancellations['route'], top_routes_by_cancellations['total_cancellations'])
ax1.set_xlabel('Route')
ax1.tick_params(axis='x', labelrotation = 45)
ax1.set_ylabel('Number of cancelled flights')
ax1.set_title('Top 9 highest number of cancelations per route')
plt.tight_layout()

top9_airline_delays_bar, ax2 = plt.subplots()
top_airlines_by_delay = airlines_delays_cancels.sort_values('mean_dep_delay', ascending=False).head(9)
ax2.bar(top_airlines_by_delay['airline'], top_airlines_by_delay['mean_dep_delay'])
ax2.set_xlabel('Airline')
ax2.tick_params(axis='x', labelrotation = 90)
ax2.set_ylabel('Average departure delay')
ax2.set_title('Top 9 highest departure delays per airline')
plt.tight_layout()

plt.show()