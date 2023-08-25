"""
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') 
and walls (represented as '+'). You are also given the entrance of the maze, 
where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. 
You cannot step into a cell with a wall, and you cannot step outside the maze. 
Your goal is to find the nearest exit from the entrance. 
An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

"""
from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row, col = entrance
        m, n = len(maze), len(maze[0])
        # Since we cannot exit from the entrance cell, marking it as a wall
        maze[row][col] = "+"

        # Only four directions are possible [UP, DOWN, LEFT, RIGHT]
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        queue = deque([(row, col, 0)])
        while queue:
            row, col, steps = queue.popleft()
            # We now increase steps by 1 since we are checking all the neighbors of the current cell
            steps += 1
            for dr, dc in dirs:
                next_row, next_col = row + dr, col + dc

                # Check if the cell is valid
                if (
                    0 <= next_row < m
                    and 0 <= next_col < n
                    and maze[next_row][next_col] != "+"
                ):
                    # We also check if it's an exit cell
                    if (
                        next_row == 0
                        or next_row == m - 1
                        or next_col == 0
                        or next_col == n - 1
                    ):
                        # the first exit cell we reach is going to the be the nearest cell
                        # since we are doing BFS (going by each level)
                        return steps

                    # Also, mark this cell as visited by placing a wall there
                    maze[next_row][next_col] = "+"
                    queue.append((next_row, next_col, steps))

        # No such path exists, so return -1
        return -1
