# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:34:08 2019

@author: GERALD
"""


def isWordGuessed(secretWord, lettersGuessed):
    numCorrect = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            numCorrect +=1
        else:
            return False
    return True
        