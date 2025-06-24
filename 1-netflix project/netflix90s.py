# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# For dataframe analysis
#print(netflix_df.info())
#print(netflix_df.head())

# Filter movies released in the 90s
movies90s_df = netflix_df[netflix_df["release_year"].between(1990, 1999)]

# Finding the most frequent movie duration
duration = movies90s_df["duration"].mode()[0]
print("Most frequent movie duration:", duration)

plt.figure(1)
plt.hist(movies90s_df["duration"])
plt.title("Distribution of movies durations in the 1990s")
plt.xlabel("Movie duration")
plt.ylabel("Count")
plt.show()

# Count the number of short action movies (with length lower than 90 minutes)
action_movies = movies90s_df[movies90s_df["genre"] == "Action"]
short_movie_count = action_movies[action_movies["duration"] < 90].shape[0]
print("There are", short_movie_count, "short action movies")

# Most prolific directors in the 90s
print(movies90s_df["director"].value_counts().head(10))