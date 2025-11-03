import pandas as pd
import random

fNames = ["Joe", "Kelsey", "Abby", "Azria", "Alice", "Avery", "Emm", "Gavin", "Sujay", "Vihaan", "Manny", "Josh", "Sam", "Dutch", "Cal", "Nate"]
lNames = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"]
SID = 202500
frl = ['FR', 'R', 'FP']
ethicnity = ['Hispanic', 'Non-Hispanic']
gender = ['M', 'F']
names = []
hhi  = [25000, 50000, 75000, 100000, 125000, 150000]

for i in range(200):
    names.append(f"{random.choice(fNames)} {random.choice(lNames)}")

data = {
    "Name": names,
    "Age": [random.randint(3,5) for _ in names],
    "SID": [SID + i + 1 for i in range(len(names))],
    "FRL": [random.choice(frl) for _ in names],
    "Ethnicity": [random.choice(ethicnity) for _ in names],
    "Gender": [random.choice(gender) for _ in names],
    "Household_Income": [random.choice(hhi) for _ in names]
}

pennData = pd.DataFrame(data)

pennData.to_csv("NDSampleData.csv", index=False)
