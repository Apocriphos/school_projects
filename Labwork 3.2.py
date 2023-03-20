#Labwork 3.2 - Emirhan Baran 010210548
import math
measurements = [120.05, 119.97, 120.03, 119.98]
sum_list = sum(measurements)
average_points = sum_list/4
rms_e = math.sqrt((((float((average_points-measurements[0])**2))+(float((average_points-measurements[1])**2))+(float((average_points-measurements[2])**2))+(float((average_points-measurements[3])**2)))/(len(measurements)-1)))
print("RMS Error is +-{:.2f}".format(rms_e))