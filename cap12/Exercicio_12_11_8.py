# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 22:04:15 2018

@author: Lourenço Neto
"""
import sys
import wordtools as wdt

def test(did_pass):
    """ Print the result of a test """
    linenum = sys._getframe(1).f_lineno    #Get the caller's line number
    if did_pass:
        msg = "Test at line {0} ok." .format(linenum)
    else:
        msg = ("Test at line {0} FAILED. ".format(linenum))
    print(msg)
    

def test_suite(): #Few tests of "add_vectors" function
    test(wdt.cleanword("what?") == "what")
    test(wdt.cleanword("'now!'") == "now")
    test(wdt.cleanword("?+='w-o-r-d!,@$()'") ==  "word")
        
    test(wdt.has_dashdash("distance--but"))
    test(not wdt.has_dashdash("several"))
    test(wdt.has_dashdash("spoke--"))
    test(wdt.has_dashdash("distance--but"))
    test(not wdt.has_dashdash("-yo-yo-"))

    test(wdt.extract_words("Now is the time!  'Now', is the time? Yes, now.") == ['now','is','the','time','now','is','the','time','yes','now'])
    test(wdt.extract_words("she tried to curtsey as she spoke--fancy") == ['she','tried','to','curtsey','as','she','spoke','fancy'])

    test(wdt.wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
    test(wdt.wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
    test(wdt.wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
    test(wdt.wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

    test(wdt.wordset(["now", "is", "time", "is", "now", "is", "is"]) == ["is", "now", "time"])
    test(wdt.wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) == ["I", "a", "am", "is"])
    test(wdt.wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) == ["a", "am", "are", "be", "but", "is", "or"])

    test(wdt.longestword(["a", "apple", "pear", "grape"]) == 5)
    test(wdt.longestword(["a", "am", "I", "be"]) == 2)
    test(wdt.longestword(["this","supercalifragilisticexpialidocious"]) == 34)
    test(wdt.longestword([ ]) == 0)

test_suite()