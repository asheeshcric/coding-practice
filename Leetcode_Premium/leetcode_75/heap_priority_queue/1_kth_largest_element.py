"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

"""
from typing import List
from heapq import heappush, heappop


"""
NOTE: Each heap operation (push or pop) is O(logk), where k is size of the heap
Here, size of nums is n. If we manage to keep the size of the heap to equal to "k",
we can perform each operation at O(logk) and for iterating through nums, the total
time complexity is n*O(logk)

1. Keep adding to the heap until it has k elements
2. Once the size of the heap == k, add a new one and pop the min from it
3. This way we pop (n-k) elements at the end of the loop
4. Finally, we'll have the (n-k)th minimum or the kth largest element at the top
of the heap
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)

        return heap[0]


sol = Solution()
print(sol.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
