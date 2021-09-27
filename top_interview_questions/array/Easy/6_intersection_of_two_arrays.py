"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

U: 
Inp: two lists
Out: intersection of two lists in the form of a list

- Can contain duplicate numbers. Must return all numbers that intersect.
- If no intersection, return an empty list


M: Two pointers approach by sorting both the arrays

P:
1. Sort both arrays
2. Use two pointers to traverse, if you find the same items, append to the result


I:


"""

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1:
            return []
        if not nums2:
            return []

        if len(nums2) < len(nums1):
            # To make sure that length of nums1 is always <= nums2
            return self.intersect(nums2, nums1)

        i, j = 0, 0
        nums1.sort()
        nums2.sort()
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                # Intersection found
                result.append(nums1[i])
                i += 1
                j += 1
            else:
                # We have two conditions to decide which pointer to move
                # if nums1[i] < nums2[j], we move i else we move j
                if nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1

        return result
