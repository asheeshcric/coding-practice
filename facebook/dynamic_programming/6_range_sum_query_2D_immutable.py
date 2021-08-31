"""
Problem: Given a 2D matrix and locations of a smaller matrix as (row1, col1, row2, col2), find the sum of the elements that fall within the given submatrix
"""
from typing import List


class NumMatrix:
    def __init__(self, matrix: List[int]) -> None:
        # Your NumMatrix object will be instantiated and called as such:
        # obj = NumMatrix(matrix)
        # param_1 = obj.sumRegion(row1,col1,row2,col2)
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.sum_matrix = self.get_sum_matrix(list(matrix))

    def check_bounds(self, r, c):
        return True if r < self.rows and c < self.cols else False

    def get_sum_matrix(self, matrix):
        for row in range(self.rows):
            for col in range(1, self.cols):
                matrix[row][col] += matrix[row][col - 1]

        for row in range(1, self.rows):
            for col in range(self.cols):
                matrix[row][col] += matrix[row - 1][col]

        return matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # First check if the indices are out of bound or not
        if not self.check_bounds(row1, col1) and self.check_bounds(row2, col2):
            return 0

        # Basically the sum matrix contains the total sum from (0, 0) to each (row, col) position
        # To get sum of a particular region, we will have to compute as

        total = self.sum_matrix[row2][col2]
        extras = 0
        if self.check_bounds(row1 - 1, col2):
            extras += self.sum_matrix[row1 - 1][col2]
        if self.check_bounds(row2, col1 - 1):
            extras += self.sum_matrix[row2][col1 - 1]
        if self.check_bounds(row1 - 1, col1 - 1):
            extras -= self.sum_matrix[row1 - 1][col1 - 1]
        return total - extras
