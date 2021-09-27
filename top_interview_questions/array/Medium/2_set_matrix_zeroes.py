from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        seen_rows, seen_cols = set(), set()
        rows, cols = len(matrix), len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                if row in seen_rows and col in seen_cols:
                    continue

                if matrix[row][col] == 0:
                    seen_rows.add(row)
                    seen_cols.add(col)

        for row in range(rows):
            for col in range(cols):
                if row in seen_rows or col in seen_cols:
                    matrix[row][col] = 0
