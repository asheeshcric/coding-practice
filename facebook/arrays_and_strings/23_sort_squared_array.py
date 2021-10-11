from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        mid = 0
        while mid < len(nums) and nums[mid] < 0:
            mid += 1

        if mid == 0:
            # no negative elements
            return [x ** 2 for x in nums]

        if mid == len(nums):
            return [x ** 2 for x in nums[::-1]]

        result = []
        left = mid - 1
        right = mid
        while left >= 0 and right < len(nums):
            if abs(nums[left]) < abs(nums[right]):
                result.append(nums[left] ** 2)
                left -= 1
            else:
                result.append(nums[right] ** 2)
                right += 1

        if left < 0:
            # Add remaining elements on the right
            result += [x ** 2 for x in nums[right:]]

        if right == len(nums):
            result += [x ** 2 for x in nums[: left + 1][::-1]]

        return result
