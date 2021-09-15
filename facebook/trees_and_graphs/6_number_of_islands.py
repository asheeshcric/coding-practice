from typing import List

"""
1. Go through each cell in the grid
2. For each cell, check if it's a land (== "1") & not visited.
3. Apply BFS from that cell and increase the number of islands by 1
4. Inside the BFS function:
    - Start by adding that cell to the queue and mark it as visited.
    - Add the neighbors to the queue and repeat until the queue is empty
    - This way, we will find all connected lands to the first cell which called the BFS function
    - And, this makes us sure that we only visit the lands that are connected to the same island
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        # Implement a BFS to traverse neighboring cells
        def bfs(row, col):
            queue = [(row, col)]
            visited.add((row, col))
            while len(queue) > 0:
                r, c = queue.pop(0)
                # Check if the r, c position is in bounds of the grid
                for ri, ci in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if (
                        (ri, ci) not in visited
                        and 0 <= ri < rows
                        and 0 <= ci < cols
                        and grid[ri][ci] == "1"
                    ):
                        # This means we can visit that cell
                        queue.append((ri, ci))
                        visited.add((ri, ci))

        # We go through each cell in the grid
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    # Then, we do a BFS from that cell
                    bfs(row, col)
                    islands += 1

        return islands
