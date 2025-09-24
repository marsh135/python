from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

gNames = ["Emma", "Olivia", "Ava", "Isabella", "Sophia", "Mia", "Charlotte", "Amelia", "Harper", "Evelyn"]
gFreq = [18688, 17921, 14924, 13084, 12903, 12345, 11903, 11575, 11286, 10898]
gDataSet = list(zip(gNames, gFreq))

bNames = ["Noah", "Liam", "William", "James", "Oliver", "Benjamin", "Elijah", "Lucas", "Mason", "Logan"]
bFreq = [19144, 18267, 14516, 13011, 12803, 12160, 11951, 11538, 11297, 10875]
bDataSet = list(zip(bNames, bFreq))

top10 = ["Noah", "Emma", "Liam", "Olivia", "William", "Ava", "James", "Isabella", "Oliver", "Sophia"]
top10Freq = [19144, 18688, 18267, 17921, 14516, 14924, 13011, 13084, 12803, 12903]
top10DataSet = list(zip(top10, top10Freq))



gDF = DataFrame(data=gDataSet, columns=['Name', 'Frequency'])
bDF = DataFrame(data=bDataSet, columns=['Name', 'Frequency'])
top10DF = DataFrame(data=top10DataSet, columns=['Name', 'Frequency'])
top10DF.to_csv('top10_baby_names_2023.csv', index=False)

#combinedDF = pd.concat([gDF, bDF], ignore_index=True)
print(top10DF)  

top10DF.plot.bar(x='Name', y='Frequency', rot=0, title='Top 10 Baby Names in 2023', legend=False)
plt.xlabel('Name')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()