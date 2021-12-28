"""
This exercise stub and the test suite contain several enumerated constants.
Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).
"""
# Possible sublist categories.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    for value in range(len(list_two) - len(list_one) + 1):
        if list_two[value:value + len(list_one)] == list_one:
            return SUBLIST
    for value in range(len(list_one) - len(list_two) + 1):
        if list_one[value:value + len(list_two)] == list_two:
            return SUPERLIST
    return UNEQUAL
