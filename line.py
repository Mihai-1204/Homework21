import math


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2


    @property
    def distance(self):
        distance_x = self.point2.x - self.point1.x
        distance_y = self.point2.y - self.point1.y
        return math.sqrt(distance_x**2 + distance_y**2)
