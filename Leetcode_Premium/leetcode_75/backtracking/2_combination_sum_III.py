"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. 
The list must not contain the same combination twice, and the combinations may be returned in any order.
"""
from typing import List

"""
We have 9 different items to choose from

1. At each step, we can either choose one number (left branch) and move forward
OR: not choose that number and move forward

"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(combination, total, start):
            if len(combination) == k and total == n:
                result.append(combination.copy())
                return

            if total > n or len(combination) == k:
                return

            for num in range(start, 10):
                combination.append(num)
                backtrack(combination, total + num, start=num + 1)
                combination.pop()

        backtrack([], 0, 1)

        return result

    """
    This algorithm works if duplicates are allowed in the combinations
    """

    def combinationSum3withduplicates(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(combination, total, start):
            if len(combination) == k:
                if total == n:
                    result.append(combination.copy())

                return

            for num in range(start, 10):
                combination.append(num)
                backtrack(combination, total + num, start + 1)
                combination.pop()

        backtrack([], 0, 1)

        return result
