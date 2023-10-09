import math

class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        x1 = math.hypot(abs(self.__x) - x)
        y1 = math.hypot(abs(self.__y) - y)
        return x1, y1

    def distance_from_point(self, point):
        z = point.getx(), point.getx()
        return z

point1 = Point(0, 0)
point2 = Point(3, 4)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))