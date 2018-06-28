# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 01:15:09 2018

@author: Lourenço Neto
"""

"""
Estrutura de Árvore:
    Drawing -> Shape -> [Triangle, Square, Line, Circle]
"""

import abc

class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw(self, color):
        pass

class Triangle(Shape):
    def draw(self, color):
        print("Drawing Triangle with color " + color)

class Square(Shape):
    def draw(self, color):
        print("Drawing Square with color " + color)

class Line(Shape):
    def draw(self, color):
        print("Drawing Line with color " + color)

class Circle(Shape):
    def draw(self, color):
        print("Drawing Circle with color " + color)

class Drawing(Shape):
    def __init__(self):
        self.shapes = []

    def draw(self, color):
        for sh in self.shapes:
            sh.draw(color)

    def add(self, sh):
        self.shapes.append(sh)

    def remove(self, sh):
        self.shapes.remove(sh)

    def clear(self):
        print("Clearing all the shapes from drawing")
        self.shapes = []

if __name__ == '__main__':
    tri1 = Triangle()
    tri2 = Triangle()
    cir  = Circle()
    line1 = Line()
    line2 = Line()
    sq1 = Square()
    sq2 = Square()
    sq3 = Square()
    
    
    drawing = Drawing()
    drawing.add(tri1)
    drawing.add(tri2)
    drawing.add(cir)
    drawing.add(line1)
    drawing.add(sq2)

    drawing.draw("Red")

    drawing.clear()

    drawing.add(sq1)
    drawing.add(tri1)
    drawing.add(cir)
    drawing.add(sq3)
    drawing.add(line2)
    drawing.draw("Green")