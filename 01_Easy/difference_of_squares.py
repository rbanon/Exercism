"""
Find the difference between the square of the sum and the sum of the squares of the first N natural numbers.
"""

def square_of_sum(number):
    return pow(sum(i for i in range(number + 1)), 2)
    
def sum_of_squares(number):
    return sum(i*i for i in range(number + 1))
def difference_of_squares(number):
     return square_of_sum(number) - sum_of_squares(number)
