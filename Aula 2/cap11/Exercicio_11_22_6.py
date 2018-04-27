# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 18:46:06 2018

@author: Lourenço Neto
"""

import sys

def scalar_mult(s, v):
    """ Return the list containing the scalar multiple of the number s by the corresponding element of v """
    final_vector = []
    for i in range(len(v)):
        final_vector.append(s*v[i])
    return final_vector

def test(did_pass):
    """ Print the result of a test """
    linenum = sys._getframe(1).f_lineno    #Get the caller's line number
    if did_pass:
        msg = "Test at line {0} ok." .format(linenum)
    else:
        msg = ("Test at line {0} FAILED. ".format(linenum))
    print(msg)
    

def test_suite(): #Few tests of "scalar_mult" function
    test(scalar_mult(5, [1, 2]) == [5, 10])
    test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
    test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])    

test_suite()