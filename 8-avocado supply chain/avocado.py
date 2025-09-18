import pandas as pd

def process_file(filepath, columns, relevant_file_path):
    # Read data file 
    df = pd.read_csv(filepath, sep = '\t', usecols=columns)

    # Read txt file to select relevant categories
    with open(relevant_file_path, 'r') as file:
        relevant_categories = file.read().splitlines()
        file.close()

    # Fix categories_tags field with multiple (comma-separated) values
    df['categories_tags'] = df['categories_tags'].str.split(',')

    # Remove rows with missing values for relevant columns
    df.dropna(subset=['categories_tags', 'origins_tags'], inplace=True)

    # Select only rows included in relevant categories list and where the county is uk
    df = df[df['categories_tags'].apply(lambda x: any([i for i in x if i in relevant_categories]))]
    df = df[df['countries'] == 'United Kingdom']

    # Fix the multiple nomenclature for italy
    df['origins_tags'] = df['origins_tags'].replace(['en:produced-in-italy', 'en:produce-of-italy'], 'en:italy')

    # Get the country/countries of origin with higher count
    print(df['origins_tags'].value_counts())

    top_origin_country = []
    origin_count = df['origins_tags'].value_counts() 
    max = origin_count.iloc[0]
    # In case there is more than one value at the top
    for i in range(len(origin_count)):
        if origin_count.iloc[i] == max:
            top_origin_country.append(origin_count.index[i].lstrip('en:').replace('-', ' '))
        else:
            break

    return top_origin_country

pd.set_option("display.max_rows", None)
used_columns = ['code', 'lc', 'product_name_en', 'quantity', 'serving_size', 'packaging_tags', 'brands', 'brands_tags', 'categories_tags', 'labels_tags', 
                'countries', 'countries_tags', 'origins', 'origins_tags']

top_avocado_origin= process_file('data/avocado.csv', used_columns, 'data/relevant_avocado_categories.txt')
top_olive_oil_origin= process_file('data/olive_oil.csv', used_columns, 'data/relevant_olive_oil_categories.txt')
top_sourdough_origin= process_file('data/sourdough.csv', used_columns, 'data/relevant_sourdough_categories.txt')

print('Top country of origin for avocado:', top_avocado_origin)
print('Top country of origin for olive oil:', top_olive_oil_origin)
print('Top country of origin for sourdough:', top_sourdough_origin)