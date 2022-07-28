"""
 shapes.py

 This file contains classes that calculate area's of different shapes
 Contains rules to calculate area for circle's, squares and rectangles
    
 TODO:
 add extra functionality
 (perimeter)
 (length/size finding) pythagoras
 (more shapes)

 everything seems to need instance vars (self.var) ??
"""
# 

import math

# small class to implement user input for size
class Input:
    def __init__(self):
        pass

    def get_size(self):
        self.size = int(input("Enter size: "))
        return self.size

class Circle(Input):
    def __init__(self):
        pass 

    def radius(self):
        return self.radius = super().get_size()

    def diameter(self):
        return self.diameter = super().get_size()

    def area_algo(self, rad):
        self.rad = rad
        self.area = math.pi * (rad * rad)
        return self.area

    def perim_algo(self, diameter):
        self.diameter = diameter
        self.perim = (math.pi * diameter)
        return self.perim

    def get_area(self):
        self.area = self.area_algo(radius())
        print("area = ", self.area)
        return self.area

    def get_perim(self):
        self.perim = self.perim_algo(diameter())
        print("perimeter = ", self.perim)
        return self.perim

class Square(Input):
    def __init__(self):
        pass

    def sq_length(self):
        return self.length = super().get_size()

    def area_algo(self, length):
        self.length = length
        self.area = (length * length)
        return self.area

    def perim_algo(self, length):
        self.length = length
        self.perim = (length * 4)
        return self.perim

    def get_area(self):
        self.area = self.area_algo(sq_length())
        print("area = ", self.area)
        return self.area

    def get_perim(self):
        self.perim = self.perim_algo(sq_length())
        print("perimeter = ", self.perim)
        return self.perim


class Rectangle(Input):
    def __init__(self):
        pass

    def length(self):
        return self.length = super().get_size()

    def height(self):
        return self.height = super().get_size()

    def area_algo(self, length, height):
        self.length = length
        self.height = height
        self.area = (length * height)
        return self.area

    def perim_algo(self, length, height):
        self.length = length
        self.height = height
        self.perim = ((length * 2) + (height * 2))
        return self.perim

    def get_area(self):
        self.area = self.area_algo(length(), height())
        print("area = ", self.area)
        return self.area

    def get_perim(self):
        self.perim = self.perim_algo(length(), height())
        print("perimeter = ", self.perim)
        return self.perim

