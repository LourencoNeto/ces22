# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 10:27:46 2018

@author: Lourenço Neto
"""

import turtle
import math

wn = turtle.Screen()
wn.title("Exercicio 7.26.12")

alex = turtle.Turtle()

instructions = [(90, 50), (-30, 50), (-120, 50), (-120, 50), (135, 50*math.sqrt(2)), (-135, 50), (-135, 50*math.sqrt(2)), (-135, 50)]
alex.hideturtle()
for command in instructions:
    (slope, size) = command
    if slope > 0:
        alex.left(slope)
    else:
        alex.right((-1)*slope)
    alex.forward(size)

wn.mainloop()