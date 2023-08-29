"""
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""
from typing import List

"""
At each decision tree level, we choose one candidate at the left hand side and make sure that 
it is not available to choose at the right child of the current node
This way we make sure that the combinations don't repeat.

"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(idx, combination, total):
            # idx -> index of the current candidate that we're choosing
            # combination -> current combination of numbers that we have looked so far
            # total -> sum of the current combination

            # Base cases
            if total == target:
                # This means the current combination a valid combination
                result.append(combination.copy())
                return

            if total >= target or idx >= len(candidates):
                # Either we already moved past the target or are out of candidates to choose from
                return

            # 1. Choose a candidate at idx and move forward (left branch)
            # 2. Avoid candidate at idx and move forward (right branch)

            # LEFT BRANCH:
            combination.append(candidates[idx])
            backtrack(idx, combination, total + candidates[idx])
            # Remove that candidate from the combination and move to the right branch
            # RIGHT BRANCH:
            combination.pop()
            backtrack(idx + 1, combination, total)

        # We start with the first candidate, no combination, and a zero sum
        backtrack(0, [], 0)

        return result
