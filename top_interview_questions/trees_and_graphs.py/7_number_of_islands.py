"""

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

U:
- An island is surrounded by water on all sides
- So, if you encounter a piece of land, mark all the other pieces that are connected to it
- This way, we make sure that we only count an island once

"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        self.grid = grid
        self.rows, self.cols = len(grid), len(grid[0])
        self.visited = set()  # Contains (r, c) for a visited position in the grid
        num_islands = 0

        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == "1" and (row, col) not in self.visited:
                    self.bfs(row, col)
                    num_islands += 1

        return num_islands

    def bfs(self, row, col):
        queue = [(row, col)]
        while queue:
            row, col = queue.pop(0)
            self.visited.add((row, col))
            for r, c in [
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ]:
                # First check if the position is in-bounds
                if (
                    0 <= r < self.rows
                    and 0 <= c < self.cols
                    and self.grid[r][c] == "1"
                    and (r, c) not in self.visited
                ):
                    # Add all the neighbors
                    queue.append((r, c))
                    self.visited.add((r, c))
