import pandas as pd
import matplotlib.pyplot as plt

schools = pd.read_csv("schools.csv")

# Information about dataframe
print(schools.head())
print(schools.info())

# Question 1: which schools have the best math result
best_result = 0.8 * 800
best_math_schools = schools[schools["average_math"] >= best_result][["school_name", "average_math"]].sort_values("average_math", ascending = False)
print("\nThese are the schools with best math results:")
print(best_math_schools)

# Question 2: the top 10 schools based on combined SAT scores
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]
top_10_schools = schools[["school_name", "total_SAT"]].sort_values("total_SAT", ascending = False).iloc[:10,]
print("\nThese are the top10 schools based on total SAT score")
print(top_10_schools)

# Question 3: which borough has largest standard deviation in combined SAT score
schools_boroughs = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)
print("\nStatistics for each borough")
print(schools_boroughs)

largest_std_dev = schools_boroughs[schools_boroughs["std"] == schools_boroughs["std"].max()]
largest_std_dev = largest_std_dev.rename(columns = {"count":"num_schools", "mean":"average_SAT", "std":"std_SAT"}).reset_index()
print("\n Borough with largest standard deviation of total score")
print(largest_std_dev)

