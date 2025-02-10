import math

from point import Point


class Circle(Point):
    def __init__(self, x = 0, y = 0, radius = 1):
        super().__init__(x, y)
        self.radius = radius

    @property
    def is_circle(self):
        return self.radius >= 0

    def aria(self):
        return math.pi * (self.radius ** 2)

    def diameter(self):
        return 2 * self.radius