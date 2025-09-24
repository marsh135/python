from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib

Location = 'top10_baby_names_2023.csv'
df = pd.read_csv( Location, names=['Name', 'Births'], header=0, dtype={'Name': 'string', 'Births': 'int32'}
)
print(df)
print(df.describe())    
print(df.info())
df.plot(kind='bar', x='Name', y='Births', title='Top 10 Baby Names in 2023')
plt.show()
print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)
print('Done')

#https://nbviewer.org/url/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/01%20-%20Lesson.ipynb