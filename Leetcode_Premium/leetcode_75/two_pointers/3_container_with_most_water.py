"""
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0)
and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

"""
from typing import List

"""
1. Two pointers: Start and End
2. Calculate the max area for the current rectangle
3. Move start pointer ahead if left height < right height
4. Move end pointer to the left if left height > right height 
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        start, end = 0, len(height) - 1
        while start < end:
            max_area = max(max_area, min(height[start], height[end]) * (end - start))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_area
