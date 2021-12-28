# Given a year, report if it is a leap year.
def leap_year(year):
    """
    A leap year occups:
    - On every year that is evenly divisible by 4
    - Except every year that is evenly divisible by 100
    - Unless the year is also evenly divisible by 400"""
    if year % 4 is 0:
        if year % 100 is not 0 or year % 400 is 0:
            return True  
    return False
