"""
You are given an integer array nums. 

You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

"""
from typing import List

"""
The idea is to start from the goal position (i.e. end of the array)
- Starting from the end, check if you can reach the goal with the number available to us
- If we can reach the goal from index i, we can shift our goal to that position
- Else we keep looking forward
- At the end, if our goal does not shift to the starting position, then there's no way we can reach the end -- so return False
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False
