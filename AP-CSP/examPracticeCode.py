#create a list that conatins five integer values of minutes of screen time per day
#without procedures
'''
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





'''

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
screenTimeAnalyzer(my_times)


