import pandas as pd

# Load and view data
client_details = pd.read_csv('data/client_details.csv')
subscription_records = pd.read_csv('data/subscription_records.csv', parse_dates = ['start_date','end_date'])
economic_indicators = pd.read_csv('data/economic_indicators.csv', parse_dates = ['start_date','end_date'])
print('Client details:')
print(client_details.info())
print('\nSubscription records:')
print(subscription_records.info())
print(subscription_records.nunique())
print('\nEconomic indicators:')
print(economic_indicators.info())

# Merge the client and subscription data into one dataframe
df_client_sub = client_details.merge(subscription_records, on='client_id', how='outer')
# Merge client and subscription with economic indicators (in a way to obtain the inflation rate at the renewal time (end of subscription))
df_client_sub.sort_values(by=['end_date'], inplace=True)
df_records = pd.merge_asof(df_client_sub, economic_indicators, left_on='end_date', right_on='start_date', direction='backward', suffixes=('_subs', '_economy'))
df_records.drop(['Unnamed: 0', 'end_date_economy'], axis=1, inplace=True)
df_records.rename(columns={'start_date':'start_date_subs'}, inplace=True)
print('\nClient and Subscription records:')
print(df_records.head())
print(df_records.info())

#1 Find the total number of Fintech and Crypto clients and store in total_fintech_crypto_clients
print('\nIndustry categories:')
industries_count = df_records.value_counts('industry')
print(industries_count)
total_fintech_crypto_clients = len(df_records[(df_records['industry'] == 'Fintech') | (df_records['industry'] == 'Crypto')])
print(f'{total_fintech_crypto_clients} of the clients are part of Fintech or Crypto industries')

#2 Store the name of industry with the highest renewal rate in top_industry
renewal_rate = df_records.groupby('industry').agg({'renewed':'mean'}).sort_values('renewed', ascending=False)
print('\nRenewal rate for different industries:')
print(renewal_rate)
top_industry = renewal_rate.index[0]
print(f'The industry with highest renewal rate is {top_industry}')

#3 Store the average inflation rate when clients renewed their subscription in variable average_inflation_for_renewals
df_renewed = df_records[df_records['renewed']==True]
average_inflation_for_renewals = df_renewed['inflation_rate'].mean()
print(f'\nThe average inflation rate for renewals is {average_inflation_for_renewals:.3f}')
