import pandas as pd
import matplotlib.pyplot as plt

game_df = pd.read_csv("super_bowls.csv")
tv_df = pd.read_csv("tv.csv")
music_df = pd.read_csv("halftime_musicians.csv")

# Analasying TV viewership: Has TV viewership increased over time?
#print(tv_df.head())
max_viewership = tv_df[tv_df["avg_us_viewers"] == tv_df["avg_us_viewers"].max()]
print(max_viewership.head())
viewership_increased = (max_viewership["super_bowl"] > 10).item()
if(viewership_increased):
    print("TV viewership increased over time")
else:
    print("TV viewership decreased over time")

# Analysing matches: How many matches finished with a point difference greater than 40?
#print(game_df.head())
difference = len(game_df[game_df["difference_pts"] > 40])
print("Number of matches finished with difference greater than 40 points:", difference)

# Analysing musical acts: Who performed the most songs in Super Bowl halftime shows?
music_df_clean = music_df.dropna()
musician_ranking = music_df_clean.groupby("musician")["num_songs"].sum().sort_values(ascending=False)
most_songs = musician_ranking.index[0]
print(most_songs, "performed most songs in Superbowls")

plt.figure(1)
plt.plot(tv_df["super_bowl"], tv_df["avg_us_viewers"])
plt.xlabel("Superbowl edition")
plt.ylabel("Average US Viewers")
plt.title("Viewership across Superbowl editions")
plt.show()