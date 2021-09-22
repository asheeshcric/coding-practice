"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

U:
- Check a few examples and see how positions change when you rotate a matrix by 90 degrees clockwise

M:
- Transpose the matrix
- Reverse each row
- Also, make sure you don't swap the cells that have already been processed

P:
- if r != c:
    = Swap (r,c) and (c, r)
- Reverse each row in the matrix
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return matrix

        # Since it is a square matrix
        rows = cols = len(matrix)

        processed = set()

        # First transpose the matrix in-place
        for row in range(rows):
            for col in range(cols):
                if row == col or (col, row) in processed:
                    continue

                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
                processed.add((row, col))

            # Once you're done processing a row, you can reverse it
            matrix[row] = matrix[row][::-1]
