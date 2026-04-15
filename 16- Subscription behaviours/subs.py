import pandas as pd

# Load and view data
client_details = pd.read_csv('data/client_details.csv')
subscription_records = pd.read_csv('data/subscription_records.csv', parse_dates = ['start_date','end_date'])
economic_indicators = pd.read_csv('data/economic_indicators.csv', parse_dates = ['start_date','end_date'])
print(client_details.info())
print(subscription_records.info())
print(economic_indicators.info())
print(subscription_records.nunique())

#1 
