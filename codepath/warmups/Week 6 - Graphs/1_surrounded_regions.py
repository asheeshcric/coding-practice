from typing import List

"""
U:
- Given a matrix containing "X" and "O", capture all regions that are 4-directionally surrounded by "X"
    - By capturing, it means flipping all "O"s into "X"s in that surrounded region

- First, for all "O" that are at the boundary, we will convert them to "*" and apply a DFS from there until we hit all "X" on all four sides
- At the end, all "O"s that cannot be flipped will be changed to "*" and everything else will be "X"s

M:
- DFS traversal

"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return board

        rows, cols = len(board), len(board[0])

        def dfs(row, col):
            board[row][col] = "*"
            stack = [(row, col)]
            while stack:
                row, col = stack.pop()
                # Check if in bounds
                for r, c in [
                    (row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1),
                ]:
                    if 0 <= r < rows and 0 <= c < cols and board[r][c] == "O":
                        board[r][c] = "*"
                        stack.append((r, c))

        # Only check for "O"s at the boundaries of the board
        for col in range(cols):
            if board[0][col] == "O":
                dfs(0, col)
            if board[rows - 1][col] == "O":
                dfs(rows - 1, col)

        for row in range(rows):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][cols - 1] == "O":
                dfs(row, cols - 1)

        # Finally, set all "*" to "O" and make everything else "X"
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "*":
                    board[row][col] = "O"
                else:
                    board[row][col] = "X"

        return board
