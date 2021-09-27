"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.


Method 1:
    - Keep adding and removing items in a set as you traverse along the array
    - At the end, you will have the single element left in the set
    - O(n) and O(n)

Method 2:
    - Use XOR operation on all items in the list

    a XOR 0 = a
    a XOR a = 0
    So, a XOR b XOR a = (a XOR a) XOR b = 0 XOR b = b

    - O(n) and O(1)
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number = 0
        for num in nums:
            number ^= num

        return number
