import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

v1_0548 = Vector(1390.000, 2580.000)
v2_0548 = Vector(1490.000, 2580.000)

v1_theta = math.atan2(v1_0548.y, v1_0548.x)
v2_theta = math.atan2(v2_0548.y, v2_0548.x)

r = (v2_theta - v1_theta) * (180.0 / math.pi) * (math.pi/200)

if r < 0:
    r += 360.0

math.radians(r)
print(format(r, ".4f"))