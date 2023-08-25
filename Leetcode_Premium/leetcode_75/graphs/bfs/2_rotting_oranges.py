"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
If this is impossible, return -1.
"""

from typing import List
from collections import deque

"""
1. Find the positions of the rotten oranges. Also, count the number of fresh oranges in the grid
2. Do a DFS from each rotten orange and count the number of steps (minutes) for all fresh
oranges to get rotten. If all don't get rotten, ignore that result.
3. Record the one with the minimum steps

"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.rows, self.cols = len(grid), len(grid[0])

        # Find positions for all rotten oranges. Also, count the num
        # of fresh oranges
        rotten = []
        self.num_fresh = 0
        self.min_steps = float("inf")
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 2:
                    rotten.append((row, col))

                if grid[row][col] == 1:
                    self.num_fresh += 1

        if self.num_fresh == 0:
            # No fresh oranges at the beginning
            return 0

        for row, col in rotten:
            self.bfs(row, col, list(grid))

        return -1 if self.min_steps == float("inf") else self.min_steps

    def bfs(self, row, col, grid):
        steps, fresh_rotten = 0, 0
        queue = deque([(row, col)])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            row, col = queue.popleft()
            steps += 1
            for dr, dc in dirs:
                next_row, next_col = row + dr, col + dc

                # Check if valid cell
                if (
                    0 <= next_row < self.rows
                    and 0 <= next_col < self.cols
                    and grid[next_row][next_col] == 1
                ):
                    # A valid cell with a fresh orange
                    fresh_rotten += 1

                    # Replace the cell with a rotten orange
                    grid[next_row][next_col] = 2

                    if fresh_rotten == self.num_fresh:
                        # This means all fresh oranges have been rotten
                        self.min_steps = min(self.min_steps, steps)
                        # Since it's a BFS, we will reach the min steps level first
                        return

                    queue.append((next_row, next_col))
