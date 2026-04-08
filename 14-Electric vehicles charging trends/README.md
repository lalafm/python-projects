# 14- Electric Vehicles Charging Trends

The US Government's Alternative Fuels Data Center collects records of elecntric vehicle (EV) charging infrastructure, including charging ports and station locations, as well as sales of electric vehicles. With the EV market rapidly evolving, understanding trends in charging facilities and sales is essential to inform strategic planning.

As a data scientist working for a leading EV charging network operator, you recognize the potential in this data and start wrangling and visualizing the aggregated yearly data.

This yearly data captured in December of each year encompasses a record of EV charging port installations and station localities spanning roughly ten years, capturing both public and private charging environments.

The Data:

private_ev_charging.csv
Variable	                Description
year	                    Year of data collection
private_ports	            The number of available charging ports owned by private companies in a given year
private_station_locations	The number of privately owned station locations for EV charging

public_ev_charging.csv
Variable	                Description
year	                    Year of data collection
public_ports	            The number of available charging ports under public ownership in a given year
public_station_locations	The number of publicly owned station locations for EV charging

The sales information is available for each model and year in the ev_sales.csv file:
Variable	Description
Vehicle	    Electric vehicle model
year	    Year of data collection
sales	    The number of vehicles sold in the US

Tasks:
Does increased electric vehicle sales lead to more public or private charging ports?

1. How many vehicles were sold in 2018 in total? Save the answer as a numeric variable called ev_sales_2018.
2. Plot trends for private ports, public ports, and sales, saving this as fig, ax objects.
3. Did vehicle sales and number of private and public ports show the same trend (either increasing or decreasing) between the years 2015 and 2018? Save your answer as 'same' or 'different' to a variable called trend.