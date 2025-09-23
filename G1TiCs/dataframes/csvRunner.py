import pandas as pd
import random
import matplotlib.pyplot as plt

df =  pd.read_csv("dataframes/students_data10000.csv")
students_df = pd.DataFrame(df)
print("Head of the DataFrame:")
print(students_df.head()) #.head() shows the first 5 rows of the dataframe
print("-_"*40)
print("Tail of the DataFrame:")
print(students_df.tail()) #.tail() shows the last 5 rows of the dataframe
print("-_"*40)  
print("Summary of the DataFrame:")
print(students_df.info()) #.info() gives a summary of the dataframe
print("-_"*40)
print("Statistical Summary:")
print(round(students_df.describe(),1)) #.describe() gives statistical summary of numerical columns
print("-_"*40)
print("Counts of students in each major:")
print(students_df['Major'].value_counts()) # Count of students in each major
print("-_"*40)
print("Average GPA by year:")
print(students_df.groupby('Year')['GPA'].mean()) # Average GPA by year
print("-_"*40)
print("Top 3 students by GPA:")
print(students_df.sort_values(by='GPA', ascending=False).head(3)) # Top 3 students by GPA
print("-_"*40)
print("Students with GPA greater than 3.5:")
print(students_df[students_df['GPA'] > 3.5]) # Students with GPA greater than 3.5
print("-_"*40)
print("Studentsw/ Major")
print(students_df[['Name', 'Major']]) # Select specific columns
print("-_"*40)
print("First student details:")
print(students_df.iloc[0]) # Access first row by index
print("-_"*40)

print("Credits Completed statistics by Major:")
students_df.groupby('Major')['Credits_Completed'].agg(['mean','max','min'])
print("-_"*40)

print("DataFrame with new 'Absences' column:")
students_df['Abscences'] = [random.randint(0, 10) for _ in range(len(students_df))]
print(students_df.head())
print("-_"*40)



students_df['Major'].value_counts().plot(kind='bar', title='Number of Students per Major')
plt.xlabel('Major')
plt.ylabel('Number of Students')
plt.show()