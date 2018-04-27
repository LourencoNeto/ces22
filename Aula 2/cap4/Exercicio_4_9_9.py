# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 08:43:25 2018

@author: Lourenço Neto
"""

import turtle

def draw_star(t, sz, angle):
    
    for i in range(5):
        t.forward(sz) #Picking the size, the turtle t will walk sz units
        t.right(angle) #Then, it will spins angle degrees to the right to keep going with th drawing

wn = turtle.Screen()
wn.title("Exercicio 4.9.9")


alex = turtle.Turtle()
alex.color("black")
alex.pensize(3)
draw_star(alex, 100, 144) #Calling the function, the user must provide the size of each side of the star and the angle for the turtle spins
wn.mainloop()