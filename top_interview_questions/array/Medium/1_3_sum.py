from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        # First sort the list
        nums.sort()
        # For each number, find a two sum that equals the negative of that number
        for i, num in enumerate(nums):
            two_sums = self.twoSum(nums[i + 1 :], -num)
            if not two_sums:
                continue

            for sums in two_sums:
                result.add((num, sums[0], sums[1]))

        return [list(sums) for sums in result]

    def twoSum(self, nums, target):
        # Here, nums is always sorted in ascending order.
        # So, to find two sum, we can use left-right pointer approach
        left, right = 0, len(nums) - 1
        sums = set()
        while left < right:
            add = nums[left] + nums[right]
            if add == target:
                sums.add((nums[left], nums[right]))
                left += 1
                right -= 1
            elif add < target:
                left += 1
            else:
                right -= 1

        return sums
