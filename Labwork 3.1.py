#Labwork 3.1 - Emirhan Baran 010210548
import math
a1 = int(input("Please enter the X value of first point: "))
a2 = int(input("Please enter the Y value of first point: "))
b1 = int(input("Please enter the X value of second point: "))
b2 = int(input("Please enter the Y value of second point: "))
disSq = abs(((a1-b1)**2)+((a2-b2)**2))
distance = math.sqrt(disSq)*100
print("The distance between given point is %1.2f cm" %distance)