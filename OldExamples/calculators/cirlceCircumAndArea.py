#create a Python program that calculates the
#circumference of a circle from the diameter
#then, calculate the area.
#return those to the user rounded to 2 decimals
#formulas: C = 2*pi*r <-> pi*d
#Area = pi*r*r

import math 
dia = float(input("Please enter a diameter in inches: "))
circ = dia* math.pi
rad = dia/2
area =  rad * rad * math.pi

print("The circumference of a circle with diameter " + str(dia) + 
      " is " +  str(round(circ, 2)) + " inches.  The area is " 
      + str(round(area,2)) + " inches squared.")

print(f"The area is {area:.2f} and the circumference is {circ:.2f} inches squared.")