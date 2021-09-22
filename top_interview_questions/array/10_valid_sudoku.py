"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


U:
Three checks needed:
a. Check cell_validation x 9
b. Check row_validation x 9
c. Check column_validation x 9

"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board

        return (
            self.hasValidColumns() and self.hasValidRows() and self.hasValidSubBoxes()
        )

    def hasValidRows(self) -> bool:
        for row in range(self.rows):
            seen = set()
            for col in range(self.cols):
                if self.board[row][col] == ".":
                    # Ignore the empty cells
                    continue

                if self.board[row][col] in seen:
                    return False
                seen.add(self.board[row][col])

        return True

    def hasValidColumns(self) -> bool:
        for col in range(self.cols):
            seen = set()
            for row in range(self.rows):
                if self.board[row][col] == ".":
                    # Ignore the empty cells
                    continue

                if self.board[row][col] in seen:
                    return False
                seen.add(self.board[row][col])

        return True

    def hasValidSubBoxes(self) -> bool:
        for row in range(0, self.rows, 3):
            for col in range(0, self.cols, 3):
                # (row, col) is the starting cell position (top-left) of each sub-box
                seen = set()
                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        if self.board[r][c] == ".":
                            continue

                        if self.board[r][c] in seen:
                            return False

                        seen.add(self.board[r][c])

        return True
