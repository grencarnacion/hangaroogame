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

def getGuessedWord(secretWord, lettersGuessed):
    wordGuessed = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            wordGuessed = wordGuessed + letter 
        else:
            wordGuessed = wordGuessed + '_ '
            
    return wordGuessed


def getAvailableLetters (lettersGuessed):
    import string
    fullstring = string.ascii_lowercase
    availableLetters = ''
    for letter in fullstring:
        if letter not in lettersGuessed:
            availableLetters = availableLetters + letter
    return availableLetters


def hangaroo(secretWord):
    lettersGuessed = []
    guess = str
    mistakesMade = 4
    wordGuessed = False
    
    print('Welcome to HANGAROO!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.' )
    print('-----------')

    while mistakesMade > 0 and mistakesMade <= 4 and wordGuessed is False:
        if secretWord == getGuessedWord(secretWord, lettersGuessed):
            wordGuessed = True
            break
        print ('You have ' + str(mistakesMade) + ' live/s left.')
        print('Available Letters: ' + getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ').lower()
        if guess in secretWord:
            if guess in lettersGuessed:
                print("Uhm... You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                print ('///////////////')
            else:
                lettersGuessed.append(guess)
                print("Hmm.. Good guess: " + getGuessedWord(secretWord, lettersGuessed))
                print ('///////////////')
        else:
            if guess in lettersGuessed:
                print("Uhm... You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                print ('///////////////')
            else:
                lettersGuessed.append(guess)
                mistakesMade -= 1
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                print ('///////////////')

    if wordGuessed == True:
        return print ('Congratulations, you won!')
    elif mistakesMade == 0:
        print ("Sorry, you ran out of lives. The word was " + str(secretWord))



hangaroo('spongebob')