import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("dataScience/pennData500.csv")
'''
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
print("MAX:", data["GPA"].std())


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


#Histogram

plt.hist(data["GPA"], edgecolor="black", color="#154E1067")
plt.title("Distribution of GPA in Fake Data Set")
plt.xlabel("GPA")
plt.ylabel("# of Students")
plt.show()


'''

'''
#BAR CHART WOMP WOMP

#asking Pandas to count how many times each value occurs/appears
pathwayCounts = data["Pathway"].value_counts() #store it
print(pathwayCounts) #print it

#GRAPH IT
plt.bar(pathwayCounts.index, pathwayCounts.values)
plt.title("THIS IS A TITLE")
plt.xlabel("THIS IS AN X LABEL")
plt.ylabel("ALSO A LABEL FOR Y")
plt.show()


# DO IT AGAIN, but for YEARS

yearCounts = data["Year"].value_counts() #store it
print(yearCounts) #print it

#GRAPH IT
#plt.bar(yearCounts.index, yearCounts.values, edgecolor="black", color="green")
plt.pie(yearCounts.values)
plt.title("THIS IS A TITLE")
plt.xlabel("THIS IS AN X LABEL")
plt.ylabel("ALSO A LABEL FOR Y")
plt.show()
'''


#SCATTER PLOT
#TWO QUANTITATIVE VARS. TOGETHER

plt.scatter(data["Credits Completed"], data["GPA"])
plt.title("THIS IS A TITLE")
plt.xlabel("THIS IS AN X LABEL")
plt.ylabel("ALSO A LABEL FOR Y")
plt.show()






'''

plt.hist(data["GPA"])

plt.title("Distribution of GPA")
plt.xlabel("GPA")
plt.ylabel("Number of Students")

plt.show()

plt.hist(data["Credits Completed"])

plt.title("Distribution of Credits Completed")
plt.xlabel("Credits Completed")
plt.ylabel("Number of Students")

plt.show()

#Bar Charts

print(data["Pathway"].value_counts())

#Store

pathway_counts = data["Pathway"].value_counts()

plt.bar(pathway_counts.index, pathway_counts.values)

plt.title("Students by Pathway")
plt.xlabel("Pathway")
plt.ylabel("Number of Students")

plt.show()


year_counts = data["Year"].value_counts()

plt.bar(year_counts.index, year_counts.values)

plt.title("Students by Year")
plt.xlabel("Year")
plt.ylabel("Number of Students")

plt.show()


#Scatter Plots

plt.scatter(data["Credits Completed"], data["GPA"])

plt.title("Credits Completed vs. GPA")
plt.xlabel("Credits Completed")
plt.ylabel("GPA")

plt.show()

#Combining

seniors = data[data["Year"] == "Senior"]

plt.hist(seniors["GPA"])

plt.title("GPA Distribution of Seniors")
plt.xlabel("GPA")
plt.ylabel("Number of Students")

plt.show()

'''