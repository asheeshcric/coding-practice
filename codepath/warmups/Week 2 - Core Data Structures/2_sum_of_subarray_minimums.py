"""
In this problem, we will require a monotonic non-decreasing stack to keep track of the number of items on the left of the current number

For a particular number n, the total subarray sum value is: 
    = n * (no. of numbers greater than n on the right + 1) * (no. of numbers greater than n on the left + 1)

We need to find the above sum value for each number in the list and add them all to get the result
"""


from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        result = 0
        # Stack contains the indices of each number in the list
        stack = []
        arr = [float("-inf")] + arr + [float("-inf")]
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                curr = stack.pop()
                result += arr[curr] * (i - curr) * (curr - stack[-1])

            stack.append(i)

        return result % (10 ** 9 + 7)
