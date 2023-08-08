"""
You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
"""
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            # No flowers to add
            return True

        for i, pot in enumerate(flowerbed):
            # First, check if the current pot is empty
            # Then, check if it's the first pot. If not, is the pot before this empty or not
            # Finally, check if it's the last pot. If not, is the pot after this empty or not
            if (
                pot == 0
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            ):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True

        return False


sol = Solution()
print(sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2))
