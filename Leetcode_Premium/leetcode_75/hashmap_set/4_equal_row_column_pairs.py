"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

"""

from typing import List
from collections import Counter


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        pairs = 0
        row_counter = Counter([tuple(row) for row in grid])
        # Since the grid is of size n*n, the length of each column is also n
        for col_num in range(len(grid)):
            col = [grid[r][col_num] for r in range(len(grid))]
            # If the current column matches any of the rows in the row counter,
            # we add its count value to our result
            pairs += row_counter.get(tuple(col), 0)

        return pairs
