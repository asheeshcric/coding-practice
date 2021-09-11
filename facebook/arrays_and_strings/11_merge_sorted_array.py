from typing import List
"""
nums1 = [1, 2, 5, 0, 0, 0, 0]
nums2 = [2, 4, 6, 7]

You need to change nums1 (in place) to [1, 2, 2, 4, 5, 6, 7]

1. Idea is to start merging from the last place in nums1
2. Keep going until one of the arrays gets proccessed
3. At the end, if there's something left in nums2, just add them directly to the beginning of nums1
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i1, i2 = m-1, n-1
        i = m+n-1
        while i1 >= 0 and i2 >= 0:
            if nums1[i1] > nums2[i2]:
                nums1[i] = nums1[i1]
                i1 -= 1
            else:
                nums1[i] = nums2[i2]
                i2 -= 1
            i -= 1

        # Now, we might have some leftover values in nums2 in some cases
        # So, add them to beginning of nums1
        while i2 >= 0:
            nums1[i] = nums2[i2]
            i -= 1
            i2 -= 1
