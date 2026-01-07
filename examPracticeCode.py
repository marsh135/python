#create a list that conatins five integer values of minutes of screen time per day
#without procedures
"""
mst = [62,37,92,55,54]
total =  0
cnt = 0

for x in mst:
    total =  total + x
    cnt+=1

avg =  total/cnt

if avg>= 180:
    print("High Usage!")
elif avg >=90 and avg < 179:
    print("Moderate Usage")
else:
    print("Low Usage")

"""

#with function/procedure


def screenTimeAnalyzer(mst):
    total =  0
    cnt = 0

    for x in mst:
        total =  total + x
        cnt+=1

    avg =  total/cnt

    if avg>= 180:
        print("High Usage!")
    elif avg >=90 and avg < 179:
        print("Moderate Usage!")
    else:
        print("Low Usage!")


my_times = [62,37,92,55,54]
my_times1 = [162,137,192,155,154]
my_times2 = [262,237,292,255,254]
my_times3 = [162,237,92,155,254]
my_times4 = [262,137,92,255,154]

print("My Times: ", end = "")
screenTimeAnalyzer(my_times)
print("")
print("My Times 1: ", end = "")
screenTimeAnalyzer(my_times1)
print("")
print("My Times 2: ", end = "")
screenTimeAnalyzer(my_times2)
print("")
print("My Times 3: ", end = "")
screenTimeAnalyzer(my_times3)
print("")
print("My Times 4: ", end = "")
screenTimeAnalyzer(my_times4)
print("")