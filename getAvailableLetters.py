# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:03:29 2019

@author: GERALD
"""

def getAvailableLetters (lettersGuessed):
    import string
    fullstring = string.ascii_lowercase
    availableLetters = ''
    for letter in fullstring:
        if letter not in lettersGuessed:
            availableLetters = availableLetters + letter
    return availableLetters