# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 09:57:53 2018

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

def is_multiple(n, f):
    """ Return a bool informing if the number n is a multiple of f"""
    return is_factor(f, n) #So, it is checking if the number f is a factor of n: Call the previous is_factor function to verify
    
def test_suite():#Few tests of "is_multiple" function
    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))
    
test_suite()