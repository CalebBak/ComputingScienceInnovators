#!/usr/bin/env python3

"""
File: madlibs.py
Name:

A madlibs adventure!
Concepts covered: Strings, IO, printing
"""

def main():
    name = input("Enter a name: ")
    location = input("Enter a location: ")
    adverb = input("Enter an adverb: ")
    vehicle = input("Enter a name of a vehicle: ")
    verb = input("Enter a verb: ")
    story = f"{name} went to visit their best friend at {location}. While he" +\
            f" was there, he saw a {adverb} {vehicle} {verb} down the " +\
            f"road! While unsure of what was going on at  first, {name} " +\
            "soon found out that it was a streetrace!"
    print(story)

if __name__ == "__main__":
    main()
