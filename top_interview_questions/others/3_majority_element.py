from typing import List


class Solution:
    # The normal way, but can you make it better with O(1) space?
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0

        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        max_count = 1
        majority = nums[0]
        for num in freq:
            if freq[num] > max_count:
                max_count = freq[num]
                majority = num

        return majority

    def majorityConstantSpace(self, nums: List[int]) -> int:
        pass
