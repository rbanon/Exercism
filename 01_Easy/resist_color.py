"""
The goal of this exercise is to create a way:

to look up the numerical value associated with a particular color band
to list the different band colors
"""
# First, generate a list
color_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

# Call index
def color_code(color):
        return color_list.index(color)

# List colors
def colors():
    return color_list
