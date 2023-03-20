#Labwork 5.1 - Emirhan Baran 010210548
import math
def horizontal_distance(X1, Y1, X2, Y2):
    distance = math.sqrt((X2-X1)**2 + (Y2-Y1)**2)
    print("Distance (m):", format(distance, ".2f"))
print("horizontal_distance(100, 110, 100, 120)")
horizontal_distance(100, 110, 100, 120)