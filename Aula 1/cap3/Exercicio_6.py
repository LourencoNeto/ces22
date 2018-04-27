# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 13:58:13 2018

@author: Lourenço Neto
"""
#Importing the turtle library
import turtle

#Setting up the turtle Screen and customizing it
wn = turtle.Screen()
wn.title("Exercicio 6")
wn.bgcolor("lightgreen")

#Create a turtle and assign to alex variable
alex = turtle.Turtle()
alex.shape("turtle") #Shape of Turtle
alex.pencolor("blue")#Color of the pen
alex.pensize(3)#Width of the pen

#Now, this part is a loop to draw the required poligons , right after the other
size = 50 #The chosen size of the side
poligon = 3 #The first poligon is a triangle
for i in range(4):
    for side in range(poligon):
        angle = 360/poligon #The external angle of a n(In our case, the variable is poligon) sides' poligon
        alex.forward(size)
        alex.left(angle)
    if i == 0: #The first transiction should be to a triangle to a square
        poligon = poligon + 1
    else:
        poligon = poligon + 2
    size = size + 20 #Increase the size of the poligon to be easier to see every poligons

wn.mainloop()