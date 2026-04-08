import pandas as pd
import matplotlib.pyplot as plt

# Load data
df_sales = pd.read_csv('data/ev_sales.csv')
df_private = pd.read_csv('data/private_ev_charging.csv')
df_public = pd.read_csv('data/public_ev_charging.csv')
print(df_sales.info())

#1 Find number of vehicles sold in 2018
df_sales_year = df_sales.groupby('year')['sales'].sum()
ev_sales_2018 = int(df_sales_year.loc[2018])
print(df_sales_year)
print(f'{ev_sales_2018} vehicles were sold in 2018')

# Join private and public dataframes with df_sales_year
df_pri_publ = df_public.merge(df_private, on='year', how='outer')
df_pri_publ_sales = df_sales_year.reset_index().merge(df_pri_publ, on='year', how='outer')
print(df_pri_publ_sales.to_string())

#2 Plot trends
private_sales_fig, ax = plt.subplots()
df_plot_private = df_pri_publ_sales[(df_pri_publ_sales['year'] > 2013) & (df_pri_publ_sales['year'] < 2020)]
ax.plot(df_plot_private['year'], df_plot_private['private_ports'], label='private_ports')
ax.plot(df_plot_private['year'], df_plot_private['sales']/10, label='sales/10')
ax.set_xlabel('Year')
ax.set_title('Evolution of sales and number of charging ports \n owned by private companies over the years')
ax.legend()
plt.tight_layout()

public_sales_fig, ax = plt.subplots()
df_plot_public = df_pri_publ_sales[(df_pri_publ_sales['year'] > 2012) & (df_pri_publ_sales['year'] < 2020)]
ax.plot(df_plot_public['year'], df_plot_public['public_ports'], label='public_ports')
ax.plot(df_plot_public['year'], df_plot_public['sales']/10, label='sales/10')
ax.set_xlabel('Year')
ax.set_title('Evolution of sales and number of charging ports \n under public ownership over the years')
ax.legend()
plt.tight_layout()

public_priv_fig, ax = plt.subplots()
df_plot_publ_priv = df_pri_publ_sales.dropna()
ax.plot(df_plot_publ_priv['year'], df_plot_publ_priv['sales'], label='sales')
ax.plot(df_plot_publ_priv['year'], df_plot_publ_priv['public_ports'], label='public_ports')
ax.plot(df_plot_publ_priv['year'], df_plot_publ_priv['private_ports'], label='private_ports')
ax.set_xlabel('Year')
ax.set_title('Evolution of sales and number of charging ports over the years')
ax.legend()
plt.tight_layout()
plt.show()

# Did vehicle sales and number of private and public ports 
# show the same trend (either increasing or decreasing) between the years 2015 and 2018? 
# Set at 'same' or 'different' after analysis of graphics
trend = 'same'