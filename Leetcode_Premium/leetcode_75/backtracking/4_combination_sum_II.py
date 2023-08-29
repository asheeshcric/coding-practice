"""
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort the candidates to have all duplicate numbers together
        candidates.sort()
        result = []

        def backtrack(combination, pos, total):
            if total == target:
                result.append(combination[:])
                return

            if total > target or pos >= len(candidates):
                return

            # Left
            combination.append(candidates[pos])
            backtrack(combination, pos + 1, total + candidates[pos])

            # Right
            combination.pop()
            while pos + 1 < len(candidates) and candidates[pos] == candidates[pos + 1]:
                pos += 1

            backtrack(combination, pos + 1, total)

        backtrack(combination=[], pos=0, total=0)

        return result
