import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
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


'''
data= pd.read_csv('survey.csv')
df = pd.DataFrame(data)
print("Head of the DataFrame:")
print(df.head()) #the head of the df shows the first 5 lines in the dataframe


print("End of DataFrame:")
print(df.tail()) #the last five lines of the df

print("\n-_"*40)
print("Dataframe information")
print(df.info())
#df.describe()
#df[]


#BAR CHART
df['pie'].value_counts().plot(kind='bar', color="#99ff99", edgecolor="black")
plt.title("Most Popular Thanksgiving Pies!")
plt.xlabel("PIE TYPE")
plt.ylabel("Number of Responses")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




#PIE CHART
df['pie'].value_counts().plot(kind='pie')
plt.title("Most Popular Thanksgiving Pies!")
plt.legend(loc='best')
plt.tight_layout()
plt.show()




#SCATTER PLOT


plt.scatter(df['dish1'], df['nap'])
plt.show()






