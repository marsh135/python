import math 

dia = float(input("Please enter a diameter in inches: "))
circ = dia* math.pi
rad = dia/2
area =  rad * rad * math.pi

print("The circumference of a circle with diameter " + str(dia) + " is " + 
      str(round(circ, 2)) + " inches.  The area is " + str(round(area,2)) + " inches squared.")