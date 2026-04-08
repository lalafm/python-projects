# 13- Analysing Flight Delays and Cancelations

A prominent airline company in the Pacific Northwest has accumulated extensive data related to flights and weather patterns and needs to understand the factors influencing the departure delays and cancellations to benefit both airlines and passengers. As the data analyst on the team, you decide to embark on this analytical project.

The aviation industry is dynamic with various variables impacting flight operations. To ensure the relevance and applicability of your findings, you choose to focus solely on flights from the 'pnwflights2022' datasets available from the ModernDive team exported as CSV files. These datasets provide comprehensive information on flights departing in the first half of 2022 from both of the two major airports in this region: SEA (Seattle-Tacoma International Airport) and PDX (Portland International Airport)

The data: 

flights2022.csv contains information about about each flight including
dep_time	Departure time (in the format hhmm) where NA corresponds to a cancelled flight
dep_delay	Departure delay, in minutes (negative for early)
origin	Origin airport where flight starts (IATA code)
airline	Carrier/airline name
dest	      Destination airport where flight lands (IATA code)

flights_weather2022.csv contains the same flight information as well as weather conditions such as
visib	      Visibility (in miles)
wind_gust	Wind gust speed (in mph)

Tasks:

1. Load the two CSV files into separate DataFrames. Explore the data and create any new columns that might benefit your analysis.

2. For routes, calculate the average departure delays and highest number of canceled flights and store this as a DataFrame called routes_delays_cancels, resetting the index after calculating.

3. For airlines, determine the average departure delays and the highest number of canceled flights and store this as a DataFrame called airlines_delays_cancels, resetting the index after calculating.

4. Produce two bar graphs to show (1) the top 9 highest number of cancellations by route in a plot called top9_route_cancels_bar and (2) the top 9 highest average departure delays by airline in a plot called top9_airline_delays_bar.

5. Determine if 10 mile per hour wind gusts or more have a larger average departure delay for both of SEA and PDX, setting wind_response to True if so and False if not.