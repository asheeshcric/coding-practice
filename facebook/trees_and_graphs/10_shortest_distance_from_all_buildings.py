from typing import List

"""
Algorithm:

1. For each empty cell (grid[i][j] equals 0), start a BFS:
    - In the BFS, traverse all 4-directionally adjacent cells that are not blocked or visited and keep track of the distance from the start cell.
        - Each iteration adds 1 to the distance.
    - Every time we reach a house, increment houses reached counter housesReached by 1, 
        - and increase the total distance distanceSum by the current distance (i.e., the distance from the start cell to the house).
    - If housesReached equals totalHouses, then return the total distance.
    - Otherwise, the starting cell (and every cell visited during this BFS) cannot reach all of the houses. 
        - So set every visited empty land cell equal to 2 so that we do not start a new BFS from that cell and return INT_MAX.

2. Each time a total distance is returned from a BFS call, update the minimum distance (minDistance).

3. If it is possible to reach all houses from any empty land cell, then return the minimum distance found. Otherwise, return -1.
"""


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        total_buildings = 0
        rows, cols = len(grid), len(grid[0])
        min_dist = float("inf")

        # First find out the total number of buildings in the grid
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    total_buildings += 1

        def bfs(row, col, total_buildings):
            steps, dist_sum = 0, 0
            reached = 0
            queue = [(row, col)]
            visited = {(row, col)}
            while len(queue) > 0 and reached != total_buildings:
                # We count the steps based on the number of levels we traverse through BFS
                # So, we need to keep track of how many nodes are in the current level and increase steps based on that
                next_queue = []
                for r, c in queue:
                    if grid[r][c] == 1:
                        # Reached a building
                        reached += 1
                        dist_sum += steps
                        continue

                    # Otherwise, it can be an empty land or obstacle
                    for ri, ci in [
                        (row - 1, col),
                        (row + 1, col),
                        (row, col - 1),
                        (row, col + 1),
                    ]:
                        if (
                            (ri, ci) not in visited
                            and 0 <= ri < rows
                            and 0 <= ci < cols
                            and grid[ri][ci] != 2
                        ):
                            # We add this empty land to the queue
                            visited.add((ri, ci))
                            next_queue.append((ri, ci))

                # Now, look into the next level
                queue = next_queue
                steps += 1

            # When the BFS is done and if we could not reach all the buildings, we know that all empty lands on that path
            # cannot reach the building. So, we just add obstacles to those lands so that we never go there again
            if reached != total_buildings:
                for row in range(rows):
                    for col in range(cols):
                        if grid[row][col] == 0 and (row, col) in visited:
                            grid[row][col] = 2

                # Since all buildings cannot be reached from the starting cell, we return "inf" as the distance sum
                return float("inf")

            # Since all buildings could be reached, return the distance sum
            return dist_sum

        for row in range(rows):
            for col in range(cols):
                # Only do BFS from an empty cell
                if grid[row][col] == 0:
                    dist = bfs(row, col, total_buildings)
                    min_dist = min(dist, min_dist)

        return -1 if min_dist == float("inf") else min_dist
