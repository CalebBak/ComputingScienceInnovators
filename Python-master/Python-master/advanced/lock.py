#!/usr/bin/env python3

"""
File:
Name:

Description
Concepts covered: Classes, assertion
"""


class ComboLock:
    MAX = 100
    
    def __init__(self, key1, key2, key3):
        self.key1 = key1
        self.key2 = key2
        self.key3 = key3
        
        self.dial = 0
        self.attempt = []  # the current 3-number combo being entered into the lock
        self.lefts = 0

    # Sets the dial at zero
    def reset(self):
        self.dial = 0
        self.attempt = []

    # Turns the dial a number of ticks counter-clockwise and updates attempt
    def turn_left(self, ticks):
        # Add previous value.
        self.attempt.append(dial)
        
        self.dial += ticks
        # Roll over if over max value
        if self.dial > MAX:
            self.dial = self.dial - self.MAX

    # Turns the dial a number of ticks clockwise and updates attempt list
    def turn_right(self, ticks):
        # Add previous value if attempts are not empty
        if self.attempts != []:
            self.attempts.append(self.dial)
            
        self.dial -= ticks 
        if self.dial < 0:
        # Roll over if less than zero
            self.dial = self.MAX + self.dial

    def _checkFull():
        if len(self.

    # Returns true if the lock is open (attempt == keys), false otherwise
    def isopen(self):
        # Code here

    # String representation of the ComboLock class
    def __repr__(self):
        return 'ComboLock({}, {}, {})'.format(self.key1, self.key2, self.key3)


# WARNING: Don't touch this function, it is to be left as it is
def test1():
    lock = ComboLock(25, 10, 0)
    assert str(lock) == 'ComboLock(25, 10, 0)' # __repr__ 
    assert not lock.isopen()
    
    # lock should open - basic
    lock.reset()
    lock.turn_right(25)
    lock.turn_left(15)
    lock.turn_right(50)
    assert lock.isopen()
       
    # lock should open - basic with reset in the middle
    lock.reset()
    lock.turn_right(35)
    lock.turn_left(5)
    lock.reset()
    lock.turn_right(25)
    lock.turn_left(15)
    lock.turn_right(50)
    assert lock.isopen()

    # lock should open - advanced 
    # the user turns the dial more than one full rotation
    lock.reset()
    lock.turn_right(85)
    lock.turn_left(135)
    lock.turn_right(50)
    assert lock.isopen()   
    
    # lock should not open - wrong combination
    lock.reset()
    lock.turn_right(15)
    lock.turn_left(25)
    lock.turn_right(10)
    lock.turn_left(24)    
    assert not lock.isopen()
 
    
# WARNING: Don't touch this function, it is to be left as it is
def test2():    
    lock = ComboLock(40, 30, 5)
    assert str(lock) == 'ComboLock(40, 30, 5)' 
    assert not lock.isopen()
    
    # lock should open 
    lock.reset()
    lock.turn_right(40)
    lock.turn_left(10)
    lock.turn_right(35)
    assert lock.isopen()
    
    # lock should not open - wrong combination
    lock.reset()
    lock.turn_left(20)
    lock.turn_left(10)
    lock.turn_left(25)    
    assert not lock.isopen()
    
 
def test():
    test1()
    test2()
    print("Passed all test cases")
    
if __name__ == "__main__":
    test()