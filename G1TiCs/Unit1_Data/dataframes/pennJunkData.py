import pandas as pd
import random

fNames = ["Mac", "Danielle", "Aiden", "Ben", "Van", "Kaden", "Lucian", "Andrew", "Benedict", "Keaton", "Joe", "Noah", "Roman", "Kyan", "Elijah", "Alexis", "Katerina", "Jill", "Jane", "Emmy", "Emma", "Eliana", "Rachel", "Marge", "Lisa" ]
lNames = ["Smith", "Jones", "Johnson", "Willaims", "Brown", "Garcia", "Davis",  "Miller", "Wilson", "Moore", "Foster", "Anderson", "Manukyan", "DeFreitas", "Fogarty"]
years = ["Freshman", "Sophomore", "Junior", "Senior", "Victory Lap"]
pathways = ["Early College", "Engineering", "Computer Science", "Business", "Marketing", "Early Childhood Education", "Culinary", "Criminal Justice", "Construction", "Bio Med"]
names = []
race = ["White", "Hispanic", "Black", "Asian", "Other"]
councelors = ["Mr. Smith", "Ms. Johnson", "Mrs. Williams", "Mr. Brown", "Ms. Jones"]
cEmails = ["smith@example.com", "johson@example.com", "williams@example.com","brown@example.com", "jones@example.com"]
deans = ["Mr. White", "Ms. Green", "Mrs. Black", "Mr. Blue", "Ms. Red"]
dEmails = ["white@example.com", "green@example.com", "black@example.com","blue@example.com", "red@example.com"]
dataPoints= 2000
for i in range(dataPoints):
    names.append(f"{random.choice(fNames)} {random.choice(lNames)}")

data = {
    "Student Name": names,
    "Entity": ["Penn High School"] * dataPoints,
    "% Enr": ["Full Time"] * dataPoints,
    "Student Type": ["High School"] * dataPoints,
    "Race": random.choices(race, k=dataPoints),
    "Days Absent": random.choices(range(0, 20), k=dataPoints),
    "Days Present": random.choices(range(150, 180), k=dataPoints),
    "Days Possible": 180,
    "Percent Atnd": random.choices([f"{i}%" for i in range(80, 100)], k=dataPoints),
    "Ave Dly Attend": random.choices([f"{i}%" for i in range(80, 100)], k=dataPoints),
    "Days Excused": random.choices(range(0, 10), k=dataPoints),
    "Days Unexc": random.choices(range(0, 10), k=dataPoints),
    "Ave Dly Mbr": 10,
    "Calendar": "Gold/Black",
    "Hisp/Lat": random.choices(["Yes", "No"], k=dataPoints),
    "Current Date":  pd.Timestamp.now().strftime("%m/%d/%Y"),
    "Student Number": random.choices(range(100000, 999999), k=dataPoints),
    "Current Grade": random.choices(years, k=dataPoints),
    "Guardian Name": [f"{random.choice(fNames)} {random.choice(lNames)}" for _ in range(dataPoints)],
    "Guardian Phone": [f"219-555-{random.randint(1000, 9999)}" for _ in range(dataPoints)],
    "Counselor": random.choices(councelors, k=dataPoints),
    "Counselor Email": random.choices(cEmails, k=dataPoints),
    "Dean Name": random.choices(deans, k=dataPoints),
    "Dean Email": random.choices(dEmails, k=dataPoints)

}

pennData = pd.DataFrame(data)

pennData.to_csv("pennJunkData.csv", index=False)
