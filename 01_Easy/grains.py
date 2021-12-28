# Import math library
import math

"""
There are 64 squares on a chessboard (where square 1 has one grain, square 2 has two grains, and so on).
Write code that shows:
- how many grains were on a given square, and
- the total number of grains on the chessboard

"""

# How many grains were on a given square
def square(number):
    if number >= 1 and number <= 64:
        return math.pow(2,number-1)
    else:
        raise ValueError("square must be between 1 and 64")

# The total number of grains on the chessboard
def total():
    total = 0
    for i in range(64):
        total += 2**(i)
    return total