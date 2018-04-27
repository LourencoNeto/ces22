# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 09:50:12 2018

@author: Lourenço Neto
"""

import sys

def test(did_pass):
    """ Print the result of a test """
    linenum = sys._getframe(1).f_lineno    #Get the caller's line number
    if did_pass:
        msg = "Test at line {0} ok." .format(linenum)
    else:
        msg = ("Test at line {0} FAILED. ".format(linenum))
    print(msg)
    
def is_factor(f, n):
    """ Return a bool informing if the number f is a factor of n"""
    if n % f == 0:
        return True
    else:
        return False
    
def test_suite(): #Few tests of "is_factor" function
    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))
    
test_suite()