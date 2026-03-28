import pandas as pd
import numpy as np

# Load data
df_reviews = pd.read_csv('data/airbnb_last_review.tsv', sep = '\t')
df_price = pd.read_csv('data/airbnb_price.csv')
excel_room = pd.ExcelFile('data/airbnb_room_type.xlsx')
df_rooms = excel_room.parse(0)

# Safety check - Are there any duplicates in each dataframe? Ideally 0 duplicates
print("Any duplicates in reviews dataframe?", df_reviews.duplicated().any())
print("Any duplicates in price dataframe?", df_price.duplicated().any())
print("Any duplicates in rooms dataframe?", df_rooms.duplicated().any())

# Merge dataframes
temp = df_reviews.merge(df_rooms, on='listing_id')
df_airbnb = temp.merge(df_price, on='listing_id')

# Check data
print(df_airbnb.head())
print(df_airbnb.info())

# 1- Find the earliest and latest reviews
df_airbnb['last_review'] = pd.to_datetime(df_airbnb['last_review']).dt.date
earliest_review = df_airbnb['last_review'].min()
latest_review = df_airbnb['last_review'].max()
print(f"The earlies review was added on {earliest_review}, while the latest was added on {latest_review}")

# 2- Find the number of listing with "private room" type
#print(df_airbnb['room_type'].value_counts()) # Check if categories need cleaning - yes!
df_airbnb['room_type'] = df_airbnb['room_type'].str.lower()
no_private_rooms = (df_airbnb['room_type'].values == 'private room').sum()
print(f"There are {no_private_rooms} private rooms listed")

# 3- Find the average listing price rounded to 2 decimal places
df_airbnb['price'] = df_airbnb['price'].str.lower()
# Are there any occurences not in dollars?
print(f"Number of prices not in dollar currency: {(df_airbnb['price'].str.contains('dollars').values == False).sum()}") 
# Separate price and currency and convert numerical value to float
df_airbnb[["price", "currency"]] = df_airbnb['price'].str.split(" ", expand=True)
df_airbnb['price'] = df_airbnb['price'].astype('float')
avg_price = round(df_airbnb['price'].mean(), 2)
print(f"The average rental price is {avg_price} dollars")

# 4- Combine the new variables into one DataFrame (review_dates) with 4 columns 
# in the following order: first_reviewed, last_reviewed, nb_private_rooms, and avg_price
review_dates_dict = {'first_reviewed': earliest_review, 'last_reviewed': latest_review, 'nb_private_rooms': no_private_rooms, 'avg_price': avg_price}
review_dates = pd.DataFrame([review_dates_dict])
print(review_dates)

