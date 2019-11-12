# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 22:55:40 2019

@author: GERALD
"""

def getGuessedWord(secretWord, lettersGuessed):
    wordGuessed = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            wordGuessed = wordGuessed + letter 
        else:
            wordGuessed = wordGuessed + '_ '
            
    return wordGuessed
    