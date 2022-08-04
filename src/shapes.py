"""
 shapes.py

 This file contains classes that calculate area's of different shapes
 Contains rules to calculate area for circle's, triangles, squares and
 rectangles.

"""
import math

class Input:
    def __init__(self):
        pass
    
    # reuse method when getting args for shape sizes rather than inheritance
    @classmethod
    def get_size(self):
        return int(input("Enter size: "))
    
    def ask_again(self):
        return input("would you like to continue? (y/n)\n")

    def get_shape(self):
        return input("what shape? (cir, tri, sq, rec)\n")

    def get_algo(self):
        return input("area or perim?\n")

class Circle:
    def __init__(self):
        pass 
    
    def area_algo(self, rad):
        self.rad = rad
        return math.pi * (rad * rad)

    def perim_algo(self, diameter):
        self.diameter = diameter
        return math.pi * diameter

    def get_area(self):
        self.area = self.area_algo(Input.get_size())
        print("area = ", self.area)
        return self.area

    def get_perim(self):
        self.perim = self.perim_algo(Input.get_size())
        print("perimeter = ", self.perim)
        return self.perim

class Triangle:
    def __init__(self):
        pass

    def area_algo(self, base, height):
        self.base = base
        self.height = height
        return (base * height) / 2
    
    def get_area(self):
        self.area = self.area_algo(Input.get_size(), Input().get_size())
        print("area = ", self.area)
        return self.area

class Square:
    def __init__(self):
        pass

    def area_algo(self, length):
        self.length = length
        return length * length

    def perim_algo(self, length):
        self.length = length
        return length * 4

    def get_area(self):
        self.area = self.area_algo(Input.get_size())
        print("area = ", self.area)
        return self.area

    def get_perim(self):
        self.perim = self.perim_algo(Input.get_size())
        print("perimeter = ", self.perim)
        return self.perim

class Rectangle:
    def __init__(self):
        pass

    def area_algo(self, length, height):
        self.length = length
        self.height = height
        return length * height

    def perim_algo(self, length, height):
        self.length = length
        self.height = height
        return (length * 2) + (height * 2)

    def get_area(self):
        self.area = self.area_algo(Input.get_size(), Input.get_size())
        print("area = ", self.area)
        return self.area

    def get_perim(self):
        self.perim = self.perim_algo(Input.get_size(), Input.get_size())
        print("perimeter = ", self.perim)
        return self.perim
