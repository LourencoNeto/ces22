# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 14:29:22 2018

@author: Lourenço Neto
"""

#Importing the turtle library
import turtle

#Setting up the turtle Screen and customizing it
wn = turtle.Screen()
wn.title("Exercicio 11")
wn.bgcolor("lightgreen")

#Create a turtle and assign to alex variable
alex = turtle.Turtle()
alex.shape("turtle") #Shape of Turtle
alex.pensize(3) #Width of the pen
alex.hideturtle() #Hiding the turtle, showing only the pen


side = 120 #The chosen side
angle = 144 #If you analyze the figure, we can see that in every point of the star the turtle should rotate 144 degrees to the right to continue writing the star
for i in range(5): #Five points, so 5 lines should be writen
    alex.forward(side)
    alex.right(angle)
    
wn.mainloop()