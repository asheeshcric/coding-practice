from typing import List


class Solution:

    def num_paths(self, grid, row, col):
        if grid[row][col] == 1:
            # Obstacle found, no path
            return 0

        if row < 0 or col < 0:
            # Can't move to this direction
            return 0

        if row == 0 and not any([grid[0][k] for k in range(col)]):
            # Final path found
            return 1

        if col == 0 and not any([grid[k][0] for k in range(row)]):
            # Path found
            return 1

        if self.dp[row][col] is not None:
            return self.dp[row][col]

        self.dp[row][col] = self.num_paths(
            grid, row-1, col) + self.num_paths(grid, row, col-1)
        return self.dp[row][col]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0]) if rows > 0 else 0
        self.dp = [[None for col in range(cols+1)] for row in range(rows+1)]
        return self.num_paths(obstacleGrid, rows-1, cols-1)
