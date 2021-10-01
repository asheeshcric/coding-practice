from typing import List

"""
U:
- Need to use a minimum array along with a stack to determine the pattern

M:
- Use stack and list to store the smallest and the middle numbers

P:
1. Create a min_array containing the min_number among all left numbers for each index
    - This helps in keeping track of a[i], as it is the smallest number in the pattern

2. Create a stack that stores all values eligible as a[k]
    a. First, it should be > a[i], i.e. a[k] > min_array[k]
    b. Then, it should be less than a[j], i.e. a[k] < a[j]

    - Basically, the stack is storing any eligible number that is greater than the min
3. In the process, if we find a number from the stack that is less than a[j], then we find the pattern
"""


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        min_array = [0] * n
        min_array[0] = nums[0]
        stack = []

        # First create an array that contains the min number until index i
        for i in range(1, n):
            min_array[i] = min(nums[i], min_array[i - 1])

        for j in range(n - 1, -1, -1):
            # First check if the current number is greater than the min at that position
            if nums[j] > min_array[j]:
                # This means we have found a j such that a[j] > a[i]
                while stack and stack[-1] <= min_array[j]:
                    # We will remove the numbers that is smaller than our a[i], as a[k] should be > a[i]
                    stack.pop()

                # If we find a number in the stack that is greater than the smallest a[i],
                # we still need to check that it is smaller than a[j], if yes: return True
                if stack and stack[-1] < nums[j]:
                    # This means we found a number that lies in between i and j
                    return True

                stack.append(nums[j])

        return False
