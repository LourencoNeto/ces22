# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 09:53:58 2018

@author: Lourenço Neto
"""
import math

class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def to_string(self):
        return "({0}, {1})".format(self.x, self.y)
    
    def __str__(self):    # All we have done is renamed the method
        return "({0}, {1})".format(self.x, self.y)
        
    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)
    
    def slope_from_origin(self):
        """ Return the slope of the line joining the origin to the point """
        if not self.x == 0:
            return (self.y/self.x)
        else: #If the point is in the x axis, we cannot not calculate the slope, because the value is tend to infinite
            return math.inf
    def get_line_to(self, target):
        slope = (target.y - self.y)/(target.x - self.x)
        independent = self.y - slope*self.x
        return Point(slope, independent)

print(Point(4, 11).get_line_to(Point(6, 15)))