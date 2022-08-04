"""
 shapes.py

 This file contains classes that calculate area's of different shapes
 Contains rules to calculate area for circle's, triangles, squares and
 rectangles.

"""
import math

# user input for sizes
class Input:
    def __init__(self):
        pass
    
    @classmethod
    def get_size(self):
        return int(input("Enter size: "))

    def ask_again(self):
        self.again = input("would you like to continue? (y/n)\n")
        return self.again

    def get_shape(self):
        self.shape = input("what shape? (cir, tri, sq, rec)\n")
        return self.shape

    def get_algo(self):
        self.algo = input("area or perim?\n")
        return self.algo

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

# methods w instances of shape classes
# simpler testing
class Test:
    def __init__(self):
        pass

    def test_cir(self):
        print("___area of cir___")
        self.cir = Circle()
        self.cir.get_area()
        self.cir.get_perim()

    def test_tri(self):
        print("___area of tri___")
        self.tri = Triangle()
        self.tri.get_area()

    def test_sq(self):
        print("___area of sq___")
        self.sq = Square()
        self.sq.get_area()
        self.sq.get_perim()

    def test_rec(self):
        print("___area of rec___")
        self.rec = Rectangle()
        self.rec.get_area()
        self.rec.get_perim()
