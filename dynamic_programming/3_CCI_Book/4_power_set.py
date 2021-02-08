"""
Write a method to return all subsets of a set

1. You first create an empty subset and add that to the list
    - power_set = [[]]

2. Now, for each number, keep adding that number to all the subsets in the current power_set 
(including the previous results)
    - for new_num in nums:
        power_set += [subset + [new_num] for subset in power_set]

"""
from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # You start with a list that contains one empty list (null subset)
        power_set = [[]]
        for num in nums:
            power_set += [subset + [num] for subset in power_set]

        return power_set
