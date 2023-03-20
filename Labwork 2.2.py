#Labwork 2.2 Emirhan Baran - 010210548#
import math
x = float(input("Please enter an angle(degree): ")) #Angle input and conversion from str to float
a = x*(math.pi/180) #Conversion of input from degree to radian
b = math.sin(a) #Calculation of Sin(a)
c = math.cos(a) #Calculation of Cos(a)
d = math.tan(a) #Calculation of Tan(a)
print("Sine of the angle {} is {}".format(x,b))
print("Cosine of the angle {} is {}".format(x,c))
print("Tangent of the angle {} is {}".format(x,d))