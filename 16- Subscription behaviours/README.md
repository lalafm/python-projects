# 16- Understanding subscription behaviours

A SaaS company seeks to uncover what drives its clients to renew subscriptions. They’ve collected data on client details, subscription records, and economic indicators and would like to connect them to better understand its clients’ behavior.

They’ve tasked you with analyzing these datasets to identify the key factors influencing clients’ decisions to renew their subscriptions.

Your analysis will provide them with insights into which customers are renewing their products and the reasons behind their renewals. The company can leverage these insights to make informed decisions to increase renewal rates and improve customer loyalty, helping them stay competitive and ensure long-term growth.

The Data:

The company have provided you with three datasets for your analysis. A summary of each data is provided below.

client_details.csv
Column	        Description
client_id	    Unique identifier for each client.
company_size	Size of the company (Small, Medium, Large).
industry	    Industry to which the client belongs (Fintech, Gaming, Crypto, AI, E-commerce).
location	    Location of the client (New York, New Jersey, Pennsylvania, Massachusetts, Connecticut).

subscription_records.csv
Column	            Description
client_id	        Unique identifier for each client.
subscription_type	Type of subscription (Yearly, Monthly).
start_date	        Start date of the subscription - YYYY-MM-DD.
end_date	        End date of the subscription - YYYY-MM-DD.
renewed	            Indicates whether the subscription was renewed (True, False).

economic_indicators.csv
Column	            Description
start_date	        Start date of the economic indicator (Quarterly) - YYYY-MM-DD.
end_date	        End date of the economic indicator (Quarterly) - YYYY-MM-DD.
inflation_rate	    Inflation rate in the period.
gdp_growth_rate	    Gross Domestic Product (GDP) growth rate in the period.


Tasks:

1. How many total Fintech and Crypto clients does the company have? Store as an integer variable called total_fintech_crypto_clients.

2. Which industry has the highest renewal rate? Store as a string variable called top_industry.

3. For clients that renewed their subscriptions, what was the average inflation rate when their subscriptions were renewed? Store as a float variable called average_inflation_for_renewals.