from circle import Circle
from point import Point
from line import Line


if __name__ == '__main__':
    p1 = Point(2, 3)
    p2 = Point(5, 7)
    p3 = p1 + p2
    print(f"Coordonatele punctului adunat ({p3.x}, {p3.y})")

    line = Line(p1, p2)
    print(f"Distanta dintre cele doua puncte este: {line.distance: }")

    circle = Circle(2, 1, 5)
    print(f"Aria cercului este: {circle.aria(): }")
    print(f"Diametrul cercului: {circle.diameter(): }")
    print(f"Este cercul bun? {'\nDa' if Circle.is_circle else '\nNu'}")