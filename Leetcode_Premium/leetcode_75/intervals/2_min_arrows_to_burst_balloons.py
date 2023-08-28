"""
There are some spherical balloons taped onto a flat wall that represents the XY-plane. 
The balloons are represented as a 2D integer array points 
where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. 
You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. 
A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. 
There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, 
bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
"""

from typing import List

"""
Find all overlapping balloons sets. The number of such sets is the minimum number of 
arrows required to be shot since each set of balloons can be burst by only one arrow.

Implementation:
For a balloon at (x1, x2), all the overlapping balloons must start from < x2
If x_start > x2, then they do not overlap and hence a new arrow is required
"""


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort the points based on x_end
        points = sorted(points, key=lambda p: p[1], reverse=False)

        right_limit = -float("inf")
        arrows = 0
        for x_start, x_end in points:
            if right_limit < x_start:
                # A new arrow is needed
                arrows += 1
                right_limit = x_end

        return arrows
