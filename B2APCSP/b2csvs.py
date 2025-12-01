
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



df = pd.read_csv("B2APCSP/surveyb2.csv", dtype=str)
df = df.applymap(lambda x: x.strip().title() if isinstance(x, str) else x)
df["nap"] = pd.to_numeric(df["nap"], errors="coerce")
dish_cols = [c for c in df.columns if c.startswith("dish")]
df["dish_count"] = df[dish_cols].notna().sum(axis=1)



#head of the dataframe
print(df.head())

#tail of the dataframe
print(df.tail())
#summary of the dataframe
print(df.info())

#lets make some charts
#BAR CHART - most popular pies
df['dish_count'].value_counts().sort_values().plot(kind='bar', color="#ffcc99")
plt.title("Most Popular Pies")
plt.xlabel("Pie Type")
plt.ylabel("Number of Responses")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Scatter
plt.scatter(df['dish_count'], df['nap'])
plt.title("First choice vs. naps")
plt.xlabel("First Choice")
plt.ylabel("Nap level")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()