# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 18:36:05 2018

@author: Lourenço Neto
"""

import sys

def add_vectors(u, v):
    """ Return a list containing the sums of the corresponding elements of each given lists u and v """
    final_vector = []
    for i in range(len(u)):
        final_vector.append(u[i] + v[i])
    return final_vector

def test(did_pass):
    """ Print the result of a test """
    linenum = sys._getframe(1).f_lineno    #Get the caller's line number
    if did_pass:
        msg = "Test at line {0} ok." .format(linenum)
    else:
        msg = ("Test at line {0} FAILED. ".format(linenum))
    print(msg)
    

def test_suite(): #Few tests of "add_vectors" function
    test(add_vectors([1, 1], [1, 1]) == [2, 2])
    test(add_vectors([1, 2], [1, 4]) == [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
    
test_suite()