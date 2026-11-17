import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('surveydata.csv')
df = pd.DataFrame(data)


#head of data frame
print(df.head())
#tail of dataframe
print(df.tail())
#summary of data frame
print(df.info())

#add charts
#bar chart - most popular pies
df['Turkey'].value_counts().sort_index().plot(kind='bar', color="#ffcc99")
plt.title("Turkey Rated out of 5")
plt.ylabel("Number of Responses")

plt.xlabel("Rating out of 5")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()