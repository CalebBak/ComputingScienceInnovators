#!/usr/bin/env python3

"""
File: hangman.py
Name:
A python implementation of hangman
Concepts covered: Strings, if/else, while, functions
"""

import random
import sys

words = ["test", "hello", "world", "authentication", "email", "order", "shell", "faculty", "science"]

def main():
    # Select a word
    word = random.choice(words)
    
    guesses = 6
    correct_letters = []
    incorrect_letters = set()
    
    # Fill correct letters
    for letter in word:
        correct_letters.append([letter, "_"])
    
    while guesses > 0:
        if len(incorrect_letters) > 0:
            # Display incorrect letters
            print("Incorrect guesses: " + str(incorrect_letters).replace("'", "").replace("{", "").replace("}", ""))
            
        print("Guesses remaining: %d" % guesses)
            
        incomplete = False
        for letter in correct_letters:
            if letter[1] == '_':
                incomplete = True
            print(letter[1], end=" ")
        print()
        if not incomplete:
            print("You won!")
            return
        
        guess = input("Guess a letter: ")
        guessed_correctly = False
        for i in range(len(correct_letters)):
            if guess == correct_letters[i][0]:
                correct_letters[i][1] = guess
                if not guessed_correctly:
                    print("Correct")
                guessed_correctly = True

        # Guess was wrong
        if not guessed_correctly:
            print("Incorrect")
            incorrect_letters.add(guess)
            guesses -= 1
        print()

    print("You lost. The correct word was '%s'" % word)

if __name__ == "__main__":
    main()