# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataframes
lego_sets = pd.read_csv('data/lego_sets.csv')
themes = pd.read_csv('data/parent_themes.csv')
print(lego_sets.head())
print(themes.head())

# Question 1: 