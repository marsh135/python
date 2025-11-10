import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a sample DataFrame
data = pd.read_csv('survey.csv')
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