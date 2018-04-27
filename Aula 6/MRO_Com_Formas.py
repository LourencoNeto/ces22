# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 02:01:27 2018

@author: Lourenço Neto
"""

class Shape:
    geometric_type = "Generic Shape"
    
    def area(self):
        raise NotImplementedError
    
    def get_geometric_type(self):
        return self.geometric_type
    
class Plotter:
    
    def plot(self, ratio, topleft):
        
        print('Plotting ar {}, ratio {}.' .format(topleft, ratio))
        
class Linear_Figures(Shape, Plotter):
    geometric_type = "Figures made with segments of line"
    
class Polygon(Linear_Figures):
    geometric_type = "Polygon"
    
class Convex_Polygon(Polygon):
    geometric_type = "Convex Polygon"
    def __init__(self):
        self.AnyTwoLinesInsidePolygon = True

class Regular_Polygon(Convex_Polygon):
    geometric_type = "Regular Polygon"
    
    def __init__(self, side):
        super().__init__()
        self.side = side
        
class Square(Regular_Polygon):
    geometric_type = "Regular Polygon"
    
    def __init__(self, side):
        super().__init__(side)
        self.intern_angle = 90
    
    def area(self):
        return self.side*self.side
    
class Isosceles_Triangle_Rectangle(Square): #Half Square
    geometric_type = "Triangle"
    
    def __init__(self, side):
        super().__init__(side)
        self.intern_angle = 45
        self.center_angle = 90
        
    def area(self):
        return super().area() / 2

triangle = Isosceles_Triangle_Rectangle(6)
print(triangle.geometric_type)
print(triangle.area())
print(triangle.__class__.__mro__)