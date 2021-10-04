from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Steps:
        1. Start from the end of the array and loop until you stop finding a strictly
        decreasing sequence
        2. Record the index from where the decreasing sequence starts. After that, find the number that is just greater
        than the number at index (i-1) in the array nums[i:]
        3. Swap the current number with the number just greater and then reverse the part of the list starting from index i.
        4. The final array is the desired one
        """
        len_nums = len(nums)
        if len_nums < 2:
            return

        i = len_nums - 1
        while i > 0:
            # Loop until you find the start of a strictly decreasing sequence
            if nums[i - 1] < nums[i]:
                break
            i -= 1

        # i is the index that points to the number starting the decreasing sequence
        print(i)
        if i == 0:
            nums.reverse()
        else:
            # Now find the number in the array just larger than the current number
            # To do this, start from the end of the array again and stop when you find the first
            # number that is greater than the current one
            j = len_nums - 1
            while j > i:
                if nums[j] > nums[i - 1]:
                    break
                j -= 1
            # Now, at j, you just found the number that is just greater than the one at i
            # swap numbers at indices j and i
            nums[j], nums[i - 1] = nums[i - 1], nums[j]
            # Finally, reverse the list from i
            nums[i:] = nums[i:][::-1]
