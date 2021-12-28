"""
In this exercise you are going to create a helpful program so that you don't have to remember the values of the bands.
The program will take color names as input and output a two digit number, even if the input is more than two colors!
"""
color_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
def value(colors):
    return color_list.index(colors[0])*10 + color_list.index(colors[1])
