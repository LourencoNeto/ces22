# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 23:40:35 2018

@author: Lourenço Neto
"""

class Point:
    """ A class to register points"""
    
    def _init_(self, x, y):
        """" Initialize Point at x and y"""
        self.x = x
        self.y = y

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)
                  
def detect_collision(rectangle_1, rectangle_2):
    
    if rectangle_1.corner == rectangle_2.corner: #They have the same corner
        return True
    
    """ The next following lines refers to the edges of the first rectangle """
    ref_corner_1 = rectangle_1.corner
    below_corner_1 = Point(rectangle_1.corner.x + rectangle_1.width, rectangle_1.corner.y)
    above_corner_1 = Point(rectangle_1.corner.x, rectangle_1.corner.y + rectangle_1.height)
    opposite_corner_1 = Point(below_corner_1.x, below_corner_1.y + rectangle_1.height)

    """ Then, we make a list of these points for futher use """
    list_point_1 = [ref_corner_1, below_corner_1, above_corner_1, opposite_corner_1]
    
    """ The next following lines refers to the edges of the first rectangle """
    ref_corner_2 = rectangle_2.corner
    below_corner_2 = Point(rectangle_2.corner.x + rectangle_2.width, rectangle_2.corner.y)
    above_corner_2 = Point(rectangle_2.corner.x, rectangle_2.corner.y + rectangle_2.height)
    opposite_corner_2 = Point(below_corner_2.x, below_corner_2.y + rectangle_2.height)    
    
    """ Then, we make a list of these points for futher use """
    list_point_2 = [ref_corner_2, below_corner_2, above_corner_2, opposite_corner_2]
    
    """ Now, we check if any point from the second rectangle is within the first rectangle """
    for point in list_point_2:
        if point.x <= ref_corner_1.x + rectangle_1.width and point.x >= ref_corner_1.x:
            if point.y <= ref_corner_1.y + rectangle_1.height and point.y >= ref_corner_1.y:
                return True
    
    """ At last, check if any point from the first rectangle is within the second rectangle """
    for point in list_point_1:
        if point.x <= ref_corner_2.x + rectangle_2.width and point.x >= ref_corner_2.x:
            if point.y <= ref_corner_2.y + rectangle_2.height and point.y >= ref_corner_2.y:
                return True
    
    return False #If none of the previous cases occurred, then the rectangles didn't collide

