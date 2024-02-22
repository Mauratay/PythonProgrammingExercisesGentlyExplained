#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 19:40:20 2024

@author: pancho

Write two functions, isOdd() and isEven(), with a single numeric parameter named number. The isOdd() function returns True if number is odd and False if number is even. The isEven() function returns the True if number is even and False if number is odd. Both functions return False for numbers with fractional parts, such as 3.14 or -4.5. Zero is considered an even number. 
"""

def isOdd(number):
    if type(number) == float:
        return False
    elif number == 0:
        return False
    else:
        return not number % 2 == 0

def isEven(number):
    if type(number) == float:
        return False
    elif number == 0:
        return True
    else:
        return number % 2 == 0


assert isOdd(42) == False 
assert isOdd(9999) == True 
assert isOdd(-10) == False 
assert isOdd(-11) == True 
assert isOdd(3.1415) == False 
assert isEven(42) == True 
assert isEven(9999) == False 
assert isEven(-10) == True 
assert isEven(-11) == False 
assert isEven(3.1415) == False