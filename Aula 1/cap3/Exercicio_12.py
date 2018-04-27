# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 14:39:22 2018

@author: Lourenço Neto
"""

#Importing the turtle library
import turtle

#Setting up the turtle Screen and customizing it
wn = turtle.Screen()
wn.title("Exercicio 12")
wn.bgcolor("lightgreen")

#Create a turtle and assign to alex variable
alex = turtle.Turtle()
alex.shape("turtle") #Shape of Turtle
alex.color("blue") #Color of the Turtle
alex.pensize(3) #Width of the Pen
alex.penup() #We have to start with the pen up

#Now, we must write the function to write the required clock
angle = 30 #The clock have 12 points, so the angle must be 360 divide by 12
hidden_size_1 = 80 #Chosen size until the trace
hidden_size_2 = 15 #Chosen size from the trace to the turtle stamp
shown_size = 15 #Chosen size of the trace

for i in range(12):
    alex.right(angle)
    alex.forward(hidden_size_1)
    alex.pendown()
    alex.forward(shown_size)
    alex.penup()
    alex.forward(hidden_size_2)
    alex.stamp()
    alex.backward(hidden_size_1 + shown_size + hidden_size_2)
    
wn.mainloop()