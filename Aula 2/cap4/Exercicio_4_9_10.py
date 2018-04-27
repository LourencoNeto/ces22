# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 08:43:25 2018

@author: Lourenço Neto
"""

import turtle


def draw_star(t, sz, angle):
    """Function responsable to draw a single star"""
    for i in range(5):
        t.forward(sz) #Picking the size, the turtle t will walk sz units
        t.right(angle) #Then, it will spins angle degrees to the right to keep going with th drawing

def draw_n_star(t, sz, angle, n):
    """Function responsable to draw n (given by the user) stars"""
    for i in range(n):      
        draw_star(t, sz, angle)           
        t.penup()
        t.forward(350) #Here, the turtle will walk 350 units, but this proceed won't be drawn.
        t.right(angle) #Then, the turtle will spins angle degrees to the right to adjust the drawing of the following stars
        t.pendown()
    

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Exercicio 4.9.9")


alex = turtle.Turtle()
alex.color("hotpink")
alex.pensize(3)
draw_n_star(alex, 100, 144, 5) #Calling the function, the user must provide the size of each side of the star. the angle for the turtle spins and the number of stars (In this case, will be 5)
wn.mainloop()