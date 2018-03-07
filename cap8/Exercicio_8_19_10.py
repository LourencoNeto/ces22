# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 17:52:27 2018

@author: Lourenço Neto
"""
import sys

def reverse(word):
    """Return the string word reversed"""
    start = -2 #Since we will pick the last letter separatly, the start of pick the letter in the reverse direction at the penultimate letter
    end = -1 #And it end in the letter before the penultimate. Setting this, we should carry the "window" that check the current letter until its found the first one
    reversed_word = ""
    reversed_word += word[-1:] #First of all, we pick the last letter of the string
    for i in range(len(word) - 1): #Then, pass for each letter of the word from the right to the left, pick the letter and add to the reversed_word variable
        reversed_word += word[start:end]
        start -= 1
        end -= 1
    return reversed_word

def is_palindrome(word):
    """Return if the string word is a palindrome"""
    reversed_word = reverse(word)
    if(reversed_word == word):
        return True
    else:
        return False

def test(did_pass):
    """ Print the result of a test """
    linenum = sys._getframe(1).f_lineno    #Get the caller's line number
    if did_pass:
        msg = "Test at line {0} ok." .format(linenum)
    else:
        msg = ("Test at line {0} FAILED. ".format(linenum))
    print(msg)

def test_suite(): #Few tests of "is_palindrome" function
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    
test_suite()
