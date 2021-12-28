#Import math library
import math
# Write a function that returns the earned points in a single toss of a Darts game.
def score(x, y):
    """
    The outer circle has a radius of 10 units
    The middle circle has a radius of 5 units and the inner circle a radius of 1 unit
    The inner circle has a radius of 1 unit
    They are all centered to the same point defined by the coordinates (0, 0).
    Outside: No points
    Outer circle: 1 point
    Middle circle: 5 points
    Inner circle: 10 points    
    """
    position = math.sqrt(pow(x,2) + pow(y,2))
    if position <= 1.0:
      return 10
    if position <= 5.0:
      return 5
    if position <= 10.0:
        return 1
    return 0
