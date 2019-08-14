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
        try:
            size = int(input("Select the dice size: "))
            num = int(input("Select the number of dice: "))
        except ValueError:
            print("Not a valid value")
            continue
        
        print("Rolling %dd%d" % (num, size))
        for i in range(num):
            print(random.randint(1, size))
        
        again = input("Would you like to roll again? [y/N]").lower()
        if again != "y":
            break

if __name__ == "__main__":
    main()
