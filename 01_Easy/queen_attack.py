"""
Given the position of two queens on a chess board,
indicate whether or not they are positioned so that they can attack each other.
"""
class Queen:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        if 0>self.row:
            # if the row parameter is negative
            raise ValueError("row not positive")
        if 7<self.row:
            # if the row parameter is not on the defined board
            raise ValueError("row not on board")
        if 0>self.column:
            # if the column parameter is negative
            raise ValueError("column not positive")
        if 7<self.column:
            # if the column parameter is not on the defined board
            raise ValueError("column not on board")

    def can_attack(self, another_queen):
        if self.row is another_queen.row and self.column is another_queen.column:
            # if both the queens are on the same location
            raise ValueError("Invalid queen position: both queens in the same square")
        elif (self.row is another_queen.row or self.column is another_queen.column) or abs(self.row - another_queen.row) is abs(self.column - another_queen.column):
            return True
        return False
