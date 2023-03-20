#Labwork 5.2 - Emirhan Baran 010210548
import math
def calc_horizontal(slope_dist, zenith):
    zenith_radians = zenith*(math.pi/200)
    horz_dist = slope_dist*math.sin(zenith_radians)
    print("Horizontal distance (meters):", format(horz_dist, ".3f"))
calc_horizontal(127.834, 98.421)