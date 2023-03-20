import math

# Taking Inputs
print("Program for Electrometric Tacheometry Computation")
print("-"*49)
a_0548 = input("Enter the stationary traverse ID                  : ")

b_0548 = input("Enter the referenced traverse ID                  : ")

print("Enter the Y coordinates of", b_0548, "(m)               :", end=" ")
c_0548 = float(input())

print("Enter the X coordinates of", b_0548, "(m)               :", end=" ")
d_0548 = float(input())

print("Enter the Y coordinates of", a_0548, "(m)               :", end=" ")
f_0548 = float(input())

print("Enter the X coordinates of", a_0548, "(m)               :", end=" ")
g_0548 = float(input())

print("Enter the height of", a_0548, "(m)                      :", end=" ")
h_0548 = float(input())

i_0548 = input("Enter the point ID of detail point                : ")

print("Enter the horizontal direction of point", i_0548, "(grad)  :", end=" ")
j_0548 = float(input())

print("Enter the vertical angle of point", i_0548, "(grad)        :", end=" ")
verticalangle_0548 = float(input())

print("Enter the slope distance between", a_0548, "and", i_0548, "(m)   :", end=" ")
slopedistance_0548 = float(input())

insheight_0548 = float(input("Enter the height of instrument (m)                : "))

reflectorheight_0548 = float(input("Enter the height of reflector (m)                 : "))

# Taking Inputs

# Calculation of horizontal distance
hor_dist_0548 = (slopedistance_0548 * math.sin(verticalangle_0548 * math.pi / 200))
# Calculation of height difference (delta h)
delta_H_0548 = (slopedistance_0548 * math.cos(verticalangle_0548 * math.pi / 200)) - insheight_0548 + reflectorheight_0548
# Calculation of elevation
elevation_0548 = h_0548 + delta_H_0548


# Defining first azimuth

def first_azimuth(y1, x1, y2, x2):
    dy = y2 - y1
    dx = x2 - x1
    if x1 == x2 and y1 > y2:
        azimuth = 300
    elif x1 == x2 and y1 < y2:
        azimuth = 100
    elif y1 == y2 and x1 > x2:
        azimuth = 200
    elif y1 == y2 and x1 < x2:
        azimuth = 0
    else:
        azimuth = math.atan(abs(dy / dx)) * 200 / math.pi
    if dy > 0 and dx > 0:
        azimuth = azimuth
    elif dy > 0 and dx < 0:
        azimuth = 200 - azimuth
    elif dy < 0 and dx < 0:
        azimuth = 200 + azimuth
    else:
        azimuth = 400 - azimuth
    return azimuth

# Defining first azimuth function


# Defining next azimuth function

def next_azimuth(azimut, horizontal):
    K_0548 = float(azimut + horizontal)
    if K_0548 < 200:
        K_0548 += 200
    elif K_0548 > 200 and K_0548 < 600:
        K_0548 -= 200
    elif K_0548 > 600:
        K_0548 -= 600
    return K_0548

# Defining next azimuth function

# Calculation of first azimuth
azim_0548 = first_azimuth(f_0548, g_0548, c_0548, d_0548)
# Calculation of first azimuth

# Calculation of next azimuth
azim2_0548 = next_azimuth(azim_0548, j_0548)
# Calculation of next azimuth

# Calculation of X coordinate
xcoord = g_0548 + slopedistance_0548 * math.cos(azim2_0548 * math.pi / 200)
# Calculation of X coordinate

# Calculation of Y coordinate
ycoord = f_0548 + slopedistance_0548 * math.sin(azim2_0548 * math.pi / 200)
# Calculation of Y coordinate


# Printing and Making table

titleid = "Point ID"
titleid2 = "Point ID"
titledist = "Hor. Dist."
titledelth = "Delta H"
title_elev = "Elevation"
title_coordy = "Coord.(Y)"
title_coordx = "Coord.(X)"

# Data to be placed under headings
id = a_0548
id2 = i_0548
dist = format(hor_dist_0548,".3f")
delt = format(delta_H_0548,".3f")
elev = format(elevation_0548, ".3f")
coordy = format(ycoord, ".3f")
coordx = format(xcoord, ".3f")

# Tabbed print statements
print("-"*105)
print("%-15s %-15s %-15s %-15s %-15s %-15s %s" %(titleid, titleid2, titledist,titledelth,title_elev,title_coordy,title_coordx))
print("-"*105)
print("%-15s %-15s %-15s %-15s %-15s %-15s %s" %(id, id2, dist,delt,elev,coordy,coordx))
print("-"*105)