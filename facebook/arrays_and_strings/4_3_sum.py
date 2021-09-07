from typing import List


class Solution:
    def two_sum_II(self, nums: List[int], target: int) -> List[int]:
        """
        This works when the input array is sorted
        Use two pointers left and right and check if adding both of them gives the target value
        If the sum > target, move the right pointer
        Elif move the left pointer
        Else move both the pointers
        """
        two_sums = set()
        left, right = 0, len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                pair = (nums[left], nums[right])
                if pair not in two_sums:
                    two_sums.add((nums[left], nums[right]))
                left += 1
                right -= 1
            elif total < target:
                # Move the left pointer
                left += 1
            else:
                # Move the right pointer
                right -= 1

        return two_sums

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i, num in enumerate(nums):
            # We also want to make sure that we do not use the same value again
            # in case there are duplicates in the array
            if i > 0 and nums[i-1] == num:
                continue

            two_sums = self.two_sum_II(nums[i+1:], target=-num)
            print(num, two_sums)
            if i < len(nums) - 2 and len(two_sums) > 0:
                # This means we found a 3 sum combination
                for two_sum in two_sums:
                    result.append([num] + list(two_sum))

        return result
