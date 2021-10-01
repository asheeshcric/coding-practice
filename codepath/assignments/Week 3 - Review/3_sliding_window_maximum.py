from typing import List

"""
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]


U:
- Given a list of numbers and length of a sliding window, return a list of max values from each window as the window slides from left to right
- 1 <= k <= len(nums)

M:
- We will need to use a queue that stores the numbers in a non-decreasing order
    - This means, the first element is always the max value
    - Also, add and pop() operations are O(1) from front and back of the queue

P:
1. Keep adding to the queue until we find a number that is great than the last element in the queue
2. While the number is greater than queue[-1], keep popping from the queue
3. Once the right pointer reaches the min_length (i.e. the length of the window), start adding to the result
    - Also, now we can start moving the left pointer too (to make sure the window shifts to the left)

"""
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()  # stores the indices of the nums rather than the actual indices
        left, right = 0, 0
        result = []
        while right < len(nums):
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()

            # Now append to the queue now that we've ensured that it'll be non-decreasing
            queue.append(right)

            # Remove from the left of the window, i.e. popleft() from the queue
            # If the window size gets bigger than k
            if left > queue[0]:
                queue.popleft()

            # Also, check if the window is at least of size k to start adding to the result
            if right + 1 >= k:
                # This means we've reached the length of the window now
                result.append(nums[queue[0]])
                left += 1

            right += 1

        return result
