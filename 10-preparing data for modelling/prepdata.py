import pandas as pd

customer = pd.read_csv("data/customer_train.csv")
print(customer.info())
#print(customer.memory_usage())

# First task: change gender, relevant_experience, job_change to boolean type
#gender_replace_map = {"Female":True, "Male":False}
rel_exp_replace_map = {"Has relevant experience":True, "No relevant experience":False}
customer["job_change"] = customer["job_change"].astype("boolean")
#customer["gender"].replace(gender_replace_map, inplace=True)
customer["relevant_experience"] = customer["relevant_experience"].replace(rel_exp_replace_map).astype("boolean")

# Second task: Columns containing only int should have type int32 (student_id, training_hours)
customer["student_id"] = customer["student_id"].astype("int32")
customer["training_hours"] = customer["training_hours"].astype("int32")

# Third task: Columns containing floats must be stored as float16 (city_development_index)
customer["city_development_index"] = customer["city_development_index"].astype("float16")

# Fourth task: Columns containing nominal categorical data must be stored as the category data type 
# (city, sex, major_discipline, company_type)
category_cols = ["city", "gender", "education_level", "major_discipline", "company_type"]
customer[category_cols] = customer[category_cols].astype("category")

# Fifth task: Columns containing ordinal categorical data must be stored as ordered categories
# (experience, enrolled_university, company_size, last_new_job)
enrolled_order = ["no_enrollment", "Part time course", "Full time course"]
edu_level_order = ["Primary School", "High School", "Graduate", "Masters", "Phd"]
exp_order = ['<1'] + [str(i) for i in range(1,21)] + ['>20']
comp_size_order = ["<10", "10-49", "50-99", "100-499", "500-999", "1000-4999", "5000-9999", "10000+"]
last_job_order = ["never"] + [str(i) for i in range(1,5)] + [">4"]

transf_dict = {"enrolled_university":enrolled_order, 
               "education_level":edu_level_order, 
               "experience":exp_order, 
               "company_size":comp_size_order, 
               "last_new_job":last_job_order}

for field, order_list in transf_dict.items():
    customer[field] = customer[field].astype("category")
    customer[field] = customer[field].cat.reorder_categories(
    new_categories = order_list,
    ordered = True
)

# Sixth task: Filter df to only contain students with 10+ years of experience at companies with at least 1000 employees
customer_filtered = customer[(customer["experience"] >= "10") & (customer["company_size"] >= "1000-4999")]

print(customer.info())