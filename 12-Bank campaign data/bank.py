import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data/bank_marketing.csv')

# Check imported data
print(df.info())

# Create client dataframe and clean it
df_client = df[['client_id', 'age', 'job', 'marital', 'education', 'credit_default', 'mortgage']]
df_client['job'] = df_client['job'].str.replace('.', '_')
df_client['education'] = df_client['education'].str.replace('.', '_')
df_client['education'].replace('unknown', np.NaN, inplace=True)
yes_dict = {'yes':True,}
for col in ['credit_default', 'mortgage']:
    df_client[col] = df_client[col].map(yes_dict).fillna(False).astype('boolean')
df_client.to_csv('data/client.csv', index=False)

# Create campaign dataframe and clean it
df_campaign = df[['client_id', 'number_contacts', 'contact_duration', 'previous_campaign_contacts', 
                  'previous_outcome', 'campaign_outcome']]
df['year'] = '2022'
df['day'] = df['day'].astype('str')
df_campaign['last_contact_date'] = df['year'] + '-' + df['month'] + '-' + df['day']
df_campaign['last_contact_date'] = pd.to_datetime(df_campaign['last_contact_date'], format="%Y-%b-%d")
df_campaign['previous_outcome'] = df_campaign['previous_outcome'].map({'success':True}).fillna(False).astype('boolean')
df_campaign['campaign_outcome'] = df_campaign['campaign_outcome'].map(yes_dict).fillna(False).astype('boolean')
df_campaign.to_csv('data/campaign.csv', index=False)

# Create economics dataframe and clean it
df_economics = df[['client_id', 'cons_price_idx', 'euribor_three_months']]
df_economics.to_csv('data/economics.csv', index=False)

# Original dataframe
for col in ["credit_default", "mortgage", "previous_outcome", "campaign_outcome"]:
    print(col)
    print("--------------")
    print(df[col].value_counts())