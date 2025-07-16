# 4- Exploring NYC Public School Test Result Scores

Task: 
Help the fitness studio explore interest in workouts at a global and national level.

1. When was the global search for 'workout' at its peak? Save the year of peak interest as a string named year_str in the format "yyyy".

2. Of the keywords available, what was the most popular during the covid pandemic, and what is the most popular now? Save your answers as variables called peak_covid and current respectively.

3. What country has the highest interest for workouts among the following: United States, Australia, or Japan? Save your answer as top_country.

4. You'd be interested in expanding your virtual home workouts offering to either the Philippines or Malaysia. Which of the two countries has the highest interest in home workouts? Identify the country and save it as home_workout_geo.


The Data

You are provided with a number of CSV files in the "Files/data" folder, which offer international and national-level data on Google Trends keyword searches related to fitness and related products.

- workout.csv
Column	Description
'month'	Month when the data was measured.
'workout_worldwide'	Index representing the popularity of the keyword 'workout', on a scale of 0 to 100.

- three_keywords.csv
Column	Description
'month'	Month when the data was measured.
'home_workout_worldwide'	Index representing the popularity of the keyword 'home workout', on a scale of 0 to 100.
'gym_workout_worldwide'	Index representing the popularity of the keyword 'gym workout', on a scale of 0 to 100.
'home_gym_worldwide'	Index representing the popularity of the keyword 'home gym', on a scale of 0 to 100.

- workout_geo.csv
Column	Description
'country'	Country where the data was measured.
'workout_2018_2023'	Index representing the popularity of the keyword 'workout' during the 5 year period.

- three_keywords_geo.csv
Column	Description
'country'	Country where the data was measured.
'home_workout_2018_2023'	Index representing the popularity of the keyword 'home workout' during the 5 year period.
'gym_workout_2018_2023'	Index representing the popularity of the keyword 'gym workout' during the 5 year period.
'home_gym_2018_2023'	Index representing the popularity of the keyword 'home gym' during the 5 year period.