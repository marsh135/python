import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- Load and clean the data ---

# Load the survey data from a CSV file into a DataFrame
# Specify dtype=str to ensure all data is initially read as strings
df = pd.read_csv("apcspb3.csv", dtype=str)

# Clean the data by stripping leading/trailing spaces and standardizing text casing
# Apply this transformation to all string values in the DataFrame
df = df.applymap(lambda x: x.strip().title() if isinstance(x, str) else x)

# Convert the "nap" column to numeric values
# Invalid or non-convertible entries will be set to NaN
df["NAP"] = pd.to_numeric(df["NAP"], errors="coerce")

# Calculate the number of dishes each respondent listed
# Identify all columns that start with "dish" (e.g., "dish1", "dish2", etc.)
dish_cols = [c for c in df.columns if c.startswith("DISH")]

# Count non-null values across the identified dish columns for each row
# Store the count in a new column called "dish_count"
df["dish_count"] = df[dish_cols].notna().sum(axis=1)



data= pd.DataFrame(df)
print(data.head())
print(data.tail())
print(data.info())

#lets actually code
#we are going to make some charts
#start with the ABSOLUTE MINIMUM

#Bar Chart - Most Popular Pies
data['PIE'].value_counts().plot(kind='barh')
#EXTRA
plt.title("Most Popular Pies")
plt.xlabel("Pie type")
plt.ylabel("Number of Responses")
plt.xticks(rotation=45)
plt.tight_layout()
#END EXTRA
plt.show()

#Bar Chart - Most Popular Pies
plt.scatter(data['DISH1'], data["NAP"])
#EXTRA
plt.title("Most Popular Pies")
plt.xlabel("Pie type")
plt.ylabel("Number of Responses")
plt.xticks(rotation=45)
plt.tight_layout()
#END EXTRA
plt.show()