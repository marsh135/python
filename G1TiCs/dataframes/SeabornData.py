import pandas as pd

# Example: Load a dataset from an online source
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

# Load the dataset into a pandas DataFrame
df = pd.read_csv(url)

# Display the first 5 rows of the DataFrame
print("First 5 rows of the dataset:")
print(df.head())

print("\nTotal Bill Greater than 20:")
print(df.query('(total_bill > 20) and (day == "Mon") and (size > 5)'))

print("\n Stats")
print("min: " + str(df['tip'].min()))
print("max: " + str(df['tip'].max()))
print("std: " + str(df['tip'].std()))
print("var: " + str(df['tip'].var()))
print("count: " + str(df['tip'].count()))
print("sum: " + str(df['tip'].sum()))

# Basic statistics of the dataset
print("\nSummary statistics:")
print(df.describe())

# Example: Group by 'day' and calculate the average total bill
average_bill_by_day = df.groupby('day')['total_bill'].mean()
print("\nAverage total bill by day:")
print(average_bill_by_day)