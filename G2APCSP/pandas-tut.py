import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# --- Load and clean the data ---

# Load the survey data from a CSV file into a DataFrame
# Specify dtype=str to ensure all data is initially read as strings
df = pd.read_csv("G2APCSP/survey.csv", dtype=str)

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



print("Head of the DataFrame:")
print(df.head()) #the head of the df shows the first 5 lines in the dataframe


print("End of DataFrame:")
print(df.tail()) #the last five lines of the df

print("\n-_"*40)
print("Dataframe information")
print(df.info())
#df.describe()
#df[]

###BAR CHART - Most Popular Pies

plt.figure(figsize=(8,5))
df["pie"].value_counts().plot(kind="bar", color="#ffcc99", edgecolor="black")
plt.title("Most Popular Thanksgiving Pies", fontsize=14)
plt.xlabel("Pie Type")
plt.ylabel("Number of Responses")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Box Plot 0  Nap level by dinner time

plt.figure(figsize=(8,5))
df.boxplot(column="nap", by="time", grid=False, patch_artist=True,
           boxprops=dict(facecolor="#c2eabd", color="black"))
plt.title("Nap Level by Dinner Time", fontsize=14)
plt.suptitle("")  # remove automatic subtitle
plt.xlabel("Dinner Time")
plt.ylabel("Nap Level")
plt.tight_layout()
plt.show()

#Bar Chart-  Average nap level for cook vs. clean
avg_nap = df.groupby("cookOrClean")["nap"].mean().sort_values(ascending=False)

plt.figure(figsize=(6,4))
avg_nap.plot(kind="bar", color=["#ffb347", "#77dd77"], edgecolor="black")
plt.title("Average Nap Level: Cook vs Clean", fontsize=14)
plt.ylabel("Average Nap Score")
plt.xlabel("Preference")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#Scatter Plot - Number of Dishes vs. Nap Level

plt.figure(figsize=(7,5))
plt.scatter(df["dish_count"], df["nap"], alpha=0.7, color="#66b3ff", edgecolor="black")
plt.title("Relationship Between Dish Count and Nap Level", fontsize=14)
plt.xlabel("Number of Dishes")
plt.ylabel("Nap Level")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

#Stacked Bar Chart - Pie Choice by Dinner time
pie_time = pd.crosstab(df["time"], df["pie"])

pie_time.plot(kind="bar", stacked=True, figsize=(9,5), colormap="tab20")
plt.title("Pie Choice by Dinner Time", fontsize=14)
plt.xlabel("Dinner Time")
plt.ylabel("Count")
plt.legend(title="Pie Type", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show()

#Histogram  - Nap Level Distribution
plt.figure(figsize=(7,5))
plt.hist(df["nap"].dropna(), bins=np.arange(0.5, 6.5, 1), color="#ff9999", edgecolor="black")
plt.title("Distribution of Nap Levels", fontsize=14)
plt.xlabel("Nap Level (1–5)")
plt.ylabel("Number of Responses")
plt.tight_layout()
plt.show()