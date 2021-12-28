"""
Determine if a triangle is equilateral, isosceles, or scalene.
"""
# First determinate if it is a triangle
def triangle(sides):
    return sides[0] + sides[1] > sides[2] and sides[1] + sides[2] > sides[0] and sides[0] + sides[2] > sides[1]
    
def equilateral(sides):
    return triangle(sides) and len(set(sides)) is 1

def isosceles(sides):
    return triangle(sides) and len(set(sides)) in [1,2]

def scalene(sides):
    return triangle(sides) and len(set(sides)) is 3
