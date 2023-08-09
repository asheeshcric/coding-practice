"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # First generate an array that contains the product of all elements
        # to the left of the current element
        result = []
        prod = 1
        for num in nums:
            result.append(prod)
            prod *= num

        # Now, if you start from the end and multiply the above result array one at a time,
        # it will generate the desired result array
        prod = 1
        for k in range(len(nums) - 1, -1, -1):
            result[k] *= prod
            prod *= nums[k]
        return result


sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
