import numpy as np

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def perimeter(self):
        return np.pi * 2 * self.radius
    
    def area(self):
        return np.pi * (self.radius)**2


