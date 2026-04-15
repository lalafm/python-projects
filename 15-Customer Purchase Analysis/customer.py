import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Load and view data
shopping_data = pd.read_csv('data/online_shopping_session_data.csv')
print(shopping_data.head())
print(shopping_data.info())

#1 Find the purchase rate per customer type
shopping_data_nov_dec = shopping_data[(shopping_data['Month'] == 'Nov') | (shopping_data['Month'] == 'Dec')]
no_customers = shopping_data_nov_dec['CustomerType'].value_counts()
purchases = shopping_data_nov_dec.groupby('CustomerType').agg(no_purchases = ('Purchase', 'sum'))
print('\nPurchases in November and December:')
print(purchases)
rate_new_customers = purchases.loc['New_Customer']['no_purchases'] / no_customers['New_Customer']
rate_return_customers = purchases.loc['Returning_Customer']['no_purchases'] / no_customers['Returning_Customer']
purchase_rates = {"Returning_Customer": rate_return_customers, "New_Customer": rate_new_customers}
print('\nPurchase rates in November and December:')
print(purchase_rates)

#2 Find the strongest correlation in total time spent among different page types by returning customers in November and December
shopping_data_ret = shopping_data[(shopping_data['CustomerType'] == 'Returning_Customer')]
shopping_ret_nov_dec = shopping_data_ret[(shopping_data_ret['Month'] == 'Nov') | (shopping_data_ret['Month'] == 'Dec')]
admin_info_duration_cor = shopping_ret_nov_dec['Administrative_Duration'].corr(shopping_ret_nov_dec['Informational_Duration'])
admin_prod_duration_cor = shopping_ret_nov_dec['Administrative_Duration'].corr(shopping_ret_nov_dec['ProductRelated_Duration'])
info_prod_duration_cor = shopping_ret_nov_dec['Informational_Duration'].corr(shopping_ret_nov_dec['ProductRelated_Duration'])
top_correlation = {}
if (admin_info_duration_cor > admin_prod_duration_cor):
    if (admin_info_duration_cor > info_prod_duration_cor):
        top_correlation['pair'] = ('Administrative_Duration', 'Informational_Duration')
        top_correlation['correlation'] = admin_info_duration_cor
    else:
        top_correlation['pair'] = ('Informational_Duration', 'ProductRelated_Duration')
        top_correlation['correlation'] = info_prod_duration_cor
else:
    if (admin_prod_duration_cor > info_prod_duration_cor):
        top_correlation['pair'] = ('Administrative_Duration', 'ProductRelated_Duration')
        top_correlation['correlation'] = admin_prod_duration_cor
    else:
        top_correlation['pair'] = ('Informational_Duration', 'ProductRelated_Duration')
        top_correlation['correlation'] = info_prod_duration_cor

print(top_correlation)

#3 Find the likelihood of achieving at least 100 sales out of 500 online shopping sessions for the returning customers
# with a boosted purchase rate by 15%, saving it in variable prob_at_least_100_sales
new_purch_rate = 1.15 * rate_return_customers
print(f'\nBoosted purchase rate for returning customers: {new_purch_rate:.3f}')
n_sessions = 500
prob_100_sales_or_less = stats.binom.cdf(k = 100, n = n_sessions, p = new_purch_rate)
prob_at_least_100_sales = 1 - prob_100_sales_or_less
print(f'The probability of achieving at least 100 sales out of 500 sessions is {prob_at_least_100_sales:.3f}')

# Binomial probability distribution
k_values = np.arange(300) + 1
p_binom_values = [stats.binom.pmf(k, n_sessions, new_purch_rate) for k in k_values ] 
plt.bar(k_values, p_binom_values) 
plt.vlines(100, 0, 0.08, color='r', linestyle='dashed', label="sales=100")
plt.xlabel("Number of sales")
plt.ylabel("Probability")
plt.legend()
plt.show()