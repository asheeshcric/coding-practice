from typing import List

"""
U:
- Given a grid of cells containing either of the following:
    - 0: Empty cell
    - 1: Fresh orange
    - 2: Rotten orange

- Return the minimum number of minutes that must elapse until no cell has a fresh orange. If impossible, return -1

M:
- From every rotten orange, apply a dfs and keep track of the elapsed minutes
- Update the minutes if you find a lower value

- If any of the fresh oranges are left after all the traversals, return -1

P:

"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rows, cols = len(grid), len(grid[0])
        visited = dict()
        rotten_positions = [
            (r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 2
        ]

        def dfs(row, col):
            for r, c in [
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ]:
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] != 0:
                    grid[r][c] = 2
                    if visited.get((r, c), float("inf")) > visited[(row, col)] + 1:
                        # Minimizing the time for rotting the orange at this position
                        visited[(r, c)] = visited[(row, col)] + 1
                        dfs(r, c)

        for row, col in rotten_positions:
            visited[(row, col)] = 0
            dfs(row, col)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    # This means a fresh orange is left over
                    return -1

        return max(visited.values()) if visited else 0
