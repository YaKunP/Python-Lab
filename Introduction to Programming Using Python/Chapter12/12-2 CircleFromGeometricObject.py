from GeometricObject import GeometricObject
import math    # math.pi is used in the class

class Circle(GeometricObject):
    def __init__(self, radius):
        super().__init__()
        self.__raius = radius

    def getRadius(self):
        return self.__raius

    def setRadius(self, radius):
        self.__raius = radius

    def getArea(self):
        return self.__raius * self.__raius * math.pi

    def getDiameter(self):
        return 2 * self. __raius

    def getPerimeter(self):
        return 2 * self.__raius * math.pi

    def printCircle(self):
        print(self.__str__() + " radius: " + str(self.__raius))