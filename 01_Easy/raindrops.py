"""
Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
"""
def convert(number):
    result = ""
    if not (number % 3):
        result = f"{result}Pling"
    if not (number % 5):
        result = f"{result}Plang"
    if not (number % 7):
        result = f"{result}Plong"
    return result or f"{number}"
