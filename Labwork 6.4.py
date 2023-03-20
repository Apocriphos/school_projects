import math
class Circle():
    pi = math.pi
    def __init__(self, radius):
        self.radius = radius
    def get_circumference(self):
        return self.radius*self.pi*2
    def get_area(self):
        return self.pi*(self.radius)**2