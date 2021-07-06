"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Solution:

1. Whenever we encounter a land, we do a BFS on it if it hasn't been already visited
2. After doing BFS, we increase the number of islands by 1
3. We go through each row, col and repeat the process
"""


def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(row, col):
        queue = [(row, col)]
        while len(queue) > 0:
            r, c = queue.pop(0)
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                n_r, n_c = r + dr, c + dc
                if (
                    n_r in range(rows) and n_c in range(cols) and grid[n_r][n_c] == "1"
                ) and (n_r, n_c) not in visited:
                    queue.append((n_r, n_c))
                    visited.add((n_r, n_c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                bfs(r, c)
                islands += 1

    return islands


if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(num_islands(grid))
