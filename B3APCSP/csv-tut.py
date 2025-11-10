#import all necessary libraries - PD, PLT, and NP
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#create our dataframe using our csv
#our data is going to come from a cs.
#we will call our data "data" and load it from our csv
data =  pd.read_csv('apcspb3.csv')  #nevermind, makes sense
#turn the data into a dataframe(df)

df= pd.DataFrame(data)

#Validation
print("-_"*40)
print("Head of the data frame:") 
#HotDf =  first five lines
print(df.head())

print("-_"*40)
print("Tail of the data frame:") 
#TotDF = last five lines
print(df.tail())

print("-_"*40)
print("Information about the data frame:") 
#info =  file types in DF
print(df.info())

#statistical summary:
print(round(df.describe(),1))


#see value counts on pie choices
print("Pie Value Counts")
print(df['DISH1'].value_counts()+df['DISH2'].value_counts())

print(df.groupby('PIE')['NAP'].mean())