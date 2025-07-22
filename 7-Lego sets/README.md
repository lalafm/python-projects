# 5- Examining the History of Lego Sets

Task: The team responsible for the Star Wars partnership has asked for specific information in preparation for their meeting:

1. What percentage of all licensed sets ever released were Star Wars themed? Save your answer as a variable the_force, as an integer (e.g. 25).

2. In which year was the highest number of Star Wars sets released? Save your answer as a variable new_era, as an integer (e.g. 2012).

# The data
You have been provided with two datasets to use. A summary and preview are provided below.

lego_sets.csv
Column          Description
"set_num"	    A code that is unique to each set in the dataset. This column is critical, and a missing value indicates the set is a duplicate or invalid!
"name"	        The name of the set.
"year"	        The date the set was released.
"num_parts"	    The number of parts contained in the set. This column is not central to our analyses, so missing values are acceptable.
"theme_name"	The name of the sub-theme of the set.
"parent_theme"	The name of the parent theme the set belongs to. Matches the name column of the parent_themes csv file.

parent_themes.csv
Column	            Description
"id"	            A code that is unique to every theme.
"name"	            The name of the parent theme.
"is_licensed"	    A Boolean column specifying whether the theme is a licensed theme.