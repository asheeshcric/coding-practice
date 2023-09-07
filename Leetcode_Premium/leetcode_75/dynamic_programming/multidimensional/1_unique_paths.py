"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

Given the two integers m and n, 
return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_paths = [[0 for col in range(n)] for row in range(m)]
        # Destination should be initialized with 1
        dp_paths[m - 1][n - 1] = 1

        # We start from the cells adjacent to the destination cell. So, we have two options: [RIGHT, DOWN]
        # Each moves constitutes a unique path
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row == m - 1 and col == n - 1:
                    # destination cell, do nothing
                    continue

                right = (row, col + 1)
                down = (row + 1, col)

                # Start with 0 unique paths to current cell
                unique_paths = 0
                for r, c in [right, down]:
                    if 0 <= r < m and 0 <= c < n:
                        unique_paths += dp_paths[r][c]

                dp_paths[row][col] = unique_paths

        return dp_paths[0][0]
