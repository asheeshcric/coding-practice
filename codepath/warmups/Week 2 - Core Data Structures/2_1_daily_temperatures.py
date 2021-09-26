"""
This is a prerequisite problem for problem "2_sum_of_subarray_minimums.py".
This problem explains the concept of a "Monotonic non-decreasing Stack"

Problem:
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.


Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        # The stack contains tuples as: (temp, idx) of the temperatures from the list
        stack = []
        for i, temp in enumerate(temperatures):
            # So, whenever you encounter a temp that is greater than the temp at the top of the stack, you pop from the stack and update its
            # dailyTemperature index in the answer list
            while stack and temp > stack[-1][0]:
                _, idx = stack.pop()
                answer[idx] = i - idx

            stack.append((temp, i))

        return answer
