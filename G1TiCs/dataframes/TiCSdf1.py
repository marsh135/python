import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

#load our dataframe
df = pd.read_csv('dataframes/pennData.csv')
pennData =  pd.DataFrame(df)
print("-_"*20)
print("Head of the Dataframe")  #first five rows of the dataframe
print(pennData.head())

print("-_"*20)
print("Tail of the Dataframe")  #final five rows of the dataframe
print(pennData.tail())

print("-_"*20)
print("Summary of the Dataframe")  #first five rows of the dataframe
print(pennData.info())

print("-_"*20)
print("Statistical Analysis")  #first five rows of the dataframe
print(round(pennData.describe()))


print("-_"*20)
print("Counts of Students in Pathways")  #first five rows of the dataframe
print(pennData['Pathway'].value_counts())

print("-_"*20)
print("Average GPA Per Year")  #first five rows of the dataframe
print(pennData.groupby('Year')['GPA'].mean())

print("-_"*20)
print("Top 3 Students by GPA")  #first five rows of the dataframe
print(pennData.sort_values(by='GPA', ascending=False).head(3))

print("-_"*20)
print("Students with GPA > 3.5")  #first five rows of the dataframe
print(pennData[pennData['GPA']>3.5])

print("-_"*20)
print("First Student Data")  #first five rows of the dataframe
print(pennData.iloc[0] )