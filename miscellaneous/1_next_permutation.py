from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = len(nums) - 1
        pivot_idx = right

        # Start from the right and find the index where the consecutive numbers decrease
        while right > 0:
            if nums[right] > nums[right-1]:
                pivot_idx = right - 1
                pivot_num = nums[pivot_idx]
                break
            right -= 1

        # From that index, move to the right and find a number that is just greater than the decreased (pivot) number
        tmp_idx = pivot_idx + 1
        larger_digit = float('inf')
        swap_idx = pivot_idx
        while tmp_idx < len(nums):
            if nums[tmp_idx] > pivot_num and nums[tmp_idx] <= larger_digit:
                swap_idx = tmp_idx
                larger_digit = nums[tmp_idx]
            tmp_idx += 1

        # If you found the pivot number, swap it with the one just larger than it and reverse that part of the array
        if swap_idx != pivot_idx:
            nums[swap_idx], nums[pivot_idx] = nums[pivot_idx], nums[swap_idx]
            nums[pivot_idx+1:] = nums[pivot_idx+1:][::-1]
            return nums
        else:
            return nums.sort()
