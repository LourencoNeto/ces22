# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 21:39:11 2018

@author: Lourenço Neto
"""

def cleanword(word):
    punctuation = "?!'+-*/=,$#%&@();_."
    cleaned_word = ""
    for letter in word:
        if letter not in punctuation:
            cleaned_word += letter
    return cleaned_word

def has_dashdash(word):
    dashdash = "--"
    if dashdash in word:
        return True
    else:
        return False
    
def extract_words(word):
    punctuation = "?!'+-*/=,$#%&@();_."
    for letter in punctuation:
        if letter in word:
            word = word.replace(letter, " ")
    final_word = word.lower()
    return final_word.split()

def wordcount(word, expression):
    counter = 0
    for element in expression:
        if element == word:
            counter += 1
    return counter

def wordset(expression):
    distinct_words = []
    for word in expression:
        if word not in distinct_words:
            distinct_words.append(word)
    
    return sorted(distinct_words)

def longestword(expression):
    size = 0
    for word in expression:
        if len(word) > size:
            size = len(word)         
    return size

print()