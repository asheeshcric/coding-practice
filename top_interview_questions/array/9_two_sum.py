"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = dict()
        for i, num in enumerate(nums):
            complement = target - num
            if num in complements:
                return [complements[num], i]
            else:
                complements[complement] = i

        return []
