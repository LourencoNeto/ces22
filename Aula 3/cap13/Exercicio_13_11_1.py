# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 08:06:49 2018

@author: Lourenço Neto
"""

"""In this part, we must read all the lines of the file and keep as a list of lines to further use"""
f = open("test_file.txt", "r")
lines = f.readlines()
f.close()

"""Now, we should read the list from the right to the left until all lines were written in the reversed file"""
g = open("reversed_file.txt", "w")
size = len(lines)
for i in range(size):
    g.write(lines[size - 1 - i])
    if i == 0:
        g.write("\n")
g.close()