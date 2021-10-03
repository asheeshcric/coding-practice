"""
U:
- Starting at (0, 0), the goal is to reach (m-1, n-1)
- Find how many unique paths can you take to reach the goal
- Can only move to the right or down a cell in the grid

M:
- We start from the base case, i.e. the goal cell in the grid
    - Num of unique paths to reach from the goal cell to the goal cell is 1
- For every other cell, the total number of unique paths will be the sum of unique paths from the right and the down cells
- So, we gradually make our way towards the starting point and return the result at [0][0]
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.paths = [[0] * n for _ in range(m)]
        self.m, self.n = m, n
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row == m - 1 and col == n - 1:
                    self.paths[row][col] = 1
                    continue
                right, down = (row, col + 1), (row + 1, col)
                self.paths[row][col] = self.num_paths(right, down)

        return self.paths[0][0]

    def num_paths(self, right, down):
        total = 0
        for r, c in (right, down):
            if 0 <= r < self.m and 0 <= c < self.n:
                total += self.paths[r][c]

        return total
