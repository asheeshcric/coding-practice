from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = self.place_queens(row=0, n=n, queens=[])
        return [[''.join(['Q' if c == col else '.' for c in range(n)]) for col in queens] for queens in result]

    def place_queens(self, row: int, n: int, queens: List[int]) -> List[List[int]]:
        if row == n:
            return [queens]
        result = []
        for col in range(n):
            if self.could_place(row, col, queens):
                result += self.place_queens(row + 1, n, queens + [col])
                print(result)
        return result

    def could_place(self, row: int, col: int, queens: List[int]) -> bool:
        for r, c in enumerate(queens):
            if c == col or row - r == abs(col - c):
                return False
        return True


sol = Solution()
print(sol.solveNQueens(4))
