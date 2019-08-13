#!/usr/bin/env python3

"""
File: dice.py
Name:

Rolls a dice and outputs the result
Concepts covered: Random, printing
"""

import random

def main():
    while True:
        size = input("Select the dice size: ")
        
        print(random.randint(1, 6))
        
        again = input("Would you like to roll again? [y/N]").lower()
        if again != "y":
            break

if __name__ == "__main__":
    main()
