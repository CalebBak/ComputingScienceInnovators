#!/usr/bin/env python3

"""
File: rps.py
Name:

A rock-paper-scissors game against the CPU
Concepts covered: Random, IO, if/else, printing
"""

import random
import sys

VALID_CHOICES = {"r": "s", "p": "r", "s": "p"}

def main():
    player_stats = {
        "wins": 0,
        "losses": 0,
        "ties": 0
    }

    while True:
        try:
            choice = input("Select [r]ock, [p]aper, or [s]cissors. Type 'q' " +
                           "to quit and 'i' for game info. ").lower()[0]
        except IndexError:
            # This is dealt with later
            pass

        # Validate input
        if choice == "q":
            return
        elif choice == "i":
            showStats(player_stats)
            continue
        elif choice not in list(VALID_CHOICES.keys()):
            print("'%s'is not a valid choice" % choice)
            continue

        ai_choice = random.choice(list(VALID_CHOICES.keys()))
        
        checkWin(choice, ai_choice, "You", "The computer", player_stats)


def checkWin(p1, p2, p1_name, p2_name, stats):
    if p1 == p2:
        print("Tie")
        stats["ties"] += 1
    elif p2 == VALID_CHOICES[p1]:
        print("%s won" % p1_name)
        stats["wins"] += 1
    elif p1 == VALID_CHOICES[p2]:
        print("%s won" % p2_name)
        stats["losses"] += 1

def showStats(stats):
    print("Wins:\t%4d" % stats["wins"])
    print("Losses:\t%4d" % stats["losses"])
    print("Ties:\t%4d" % stats["ties"])


if __name__ == "__main__":
    main()
