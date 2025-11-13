#import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- Load and clean the data ---

# Load the survey data from a CSV file into a DataFrame
# Specify dtype=str to ensure all data is initially read as strings
df = pd.read_csv("surveyb2.csv", dtype=str)

# Clean the data by stripping leading/trailing spaces and standardizing text casing
# Apply this transformation to all string values in the DataFrame
df = df.applymap(lambda x: x.strip().title() if isinstance(x, str) else x)

# Convert the "nap" column to numeric values
# Invalid or non-convertible entries will be set to NaN
df["nap"] = pd.to_numeric(df["nap"], errors="coerce")

# Calculate the number of dishes each respondent listed
# Identify all columns that start with "dish" (e.g., "dish1", "dish2", etc.)
dish_cols = [c for c in df.columns if c.startswith("dish")]

# Count non-null values across the identified dish columns for each row
# Store the count in a new column called "dish_count"
df["dish_count"] = df[dish_cols].notna().sum(axis=1)

data = pd.read_csv('surveyb2.csv')
df = pd.DataFrame(data)

#head of the dataframe
print(df.head())

#tail of the dataframe
print(df.tail())
#summary of the dataframe
print(df.info())

#lets make some charts
#BAR CHART - most popular pies
df['pie'].value_counts().plot(kind='bar', color="#ffcc99")
plt.title("Most Popular Pies")
plt.xlabel("Pie Type")
plt.ylabel("Number of Responses")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Scatter
plt.scatter(df['dish1'], df['nap'])
plt.title("First choice vs. naps")
plt.xlabel("First Choice")
plt.ylabel("Nap level")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()