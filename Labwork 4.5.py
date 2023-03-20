#Labwork 3.2 - Emirhan Baran 010210548
x1 = float(input("Please enter the X value of first point: ")) # we have to convert the data to float type 
y1 = float(input("Please enter the Y value of first point: ")) # We can't start variants with uppercase letters 
x2 = float(input("Please enter the X value of second point: "))
y2 = float(input("Please enter the Y value of second point: "))
s = ((((x1-x2)**2) + ((y1-y2)**2))**0.5)*100 #Made times 100 to convert meter to cantimeter
print("the distance between given points is", s, "cantimeter")