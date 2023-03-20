#Labwork 3.2 - Emirhan Baran 010210548
import math # We have to use import math commant in order to use math. functions
angle_degree = float(input("Please enter an agnle(degree):"))
angle_rad = math.radians(angle_degree) # We have to convert angle degree to radian 
print("Sine of the angle", angle_degree, "is", math.sin(angle_rad))
print("Cosine of the angle", angle_degree, "is", math.cosin(angle_rad))
print("Tangent of the angle", angle_degree, "is", math.tan(angle_rad))