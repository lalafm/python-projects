import pandas as pd

sleep = pd.read_csv("data/sleep_health_data.csv")

# First research question: occupation with lowest sleep duration
lowest_sleep_occ = sleep.groupby("Occupation")["Sleep Duration"].mean().sort_values().index[0]
print(f"The occupation with lowest average sleep duration is {lowest_sleep_occ}")

# Second research question: occupation with lowest sleep quality
lowest_sleep_quality_occ = sleep.groupby("Occupation")["Quality of Sleep"].mean().sort_values().index[0]
print(f"The occupation with lowest average sleep quality is {lowest_sleep_quality_occ}")
same_occ = (lowest_sleep_quality_occ == lowest_sleep_occ)
print(f"Is the occupation with lowest sleep quality the same as the one with lowest sleep duration? {same_occ}")

# Third research question: What ratio of people in each BMI category have insomnia
# number of insomnia entries for each BMI category
len_normal_insom = len(sleep[(sleep["BMI Category"] == "Normal") & (sleep["Sleep Disorder"] == "Insomnia")])
len_overweight_insom = len(sleep[(sleep["BMI Category"] == "Overweight") & (sleep["Sleep Disorder"] == "Insomnia")])
len_obese_insom = len(sleep[(sleep["BMI Category"] == "Obese") & (sleep["Sleep Disorder"] == "Insomnia")])
# total for each BMI category
len_normal = len(sleep[(sleep["BMI Category"] == "Normal")])
len_overweight = len(sleep[(sleep["BMI Category"] == "Overweight")])
len_obese = len(sleep[(sleep["BMI Category"] == "Obese")])

bmi_insomnia_ratios = {
    "Normal" : round((len_normal_insom/len_normal), 2),
    "Overweight" : round((len_overweight_insom/len_overweight), 2),
    "Obese" : round((len_obese_insom/len_obese), 2)
}
print(f"The ratio of people with BMI Normal with insomnia is {bmi_insomnia_ratios["Normal"]}")
print(f"The ratio of people with BMI Overweight with insomnia is {bmi_insomnia_ratios["Overweight"]}")
print(f"The ratio of people with BMI Obese with insomnia is {bmi_insomnia_ratios["Obese"]}.")
