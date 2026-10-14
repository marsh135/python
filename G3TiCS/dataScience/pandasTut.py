
import pandas as pd

scores = pd.DataFrame(
    [
        [85, 91, 78, 92],
        [88, 76, 95, 89],
        [90, 87, 84, 93]
    ],
    index=["Alex", "Vihaan", "Jordan"],
    columns=["Assignment 1", "Assignment 2",
             "Assignment 3", "Assignment 4"]
)


data = pd.read_csv("G3TiCS/dataScience/pennData500.csv")
print(data)


print(data.head())
print(data.tail())
print(data.shape)
print(data.columns)
print(data.dtypes)

print(data.describe()) #- SUMMARY STATS OF ENTIRE DATAFRAME



print("MEAN:",data["GPA"].mean())
print("MEDIAN:",data["GPA"].median())
print("MIN:",data["GPA"].min())
print("MAX:",data["GPA"].max())



print(data["GPA"])

print(data["GPA"], data["Pathway"])


filtered_data=data[data["GPA"]>3.0]
print()
print("-"*25)
print(filtered_data)


filtered_data2=data[data["Pathway"]== "Business"]
print()
print("-"*25)
print(filtered_data2)

print(filtered_data[["GPA", "Pathway"]])


#CHALLENGE 1
#C1: Rows: 500
#C1: Columns: 6
#data = pd.read_csv("G3TiCS/dataScience/pennData500.csv")
#print(data)


#CHALLENGE 2
