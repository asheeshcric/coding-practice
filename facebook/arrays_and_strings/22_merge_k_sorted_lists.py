from typing import List, Optional
from heapq import heappush, heappop


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = dict()
        min_heap = []
        for i, node in enumerate(lists):
            if not node:
                continue
            nodes[i] = node
            heappush(min_heap, (node.val, i))

        dummyHead = ListNode(val=None)
        head = dummyHead
        while min_heap:
            min_node, idx = heappop(min_heap)
            new_node = ListNode(val=min_node)
            head.next = new_node
            if nodes[idx].next:
                nodes[idx] = nodes[idx].next
                heappush(min_heap, (nodes[idx].val, idx))

        return dummyHead.next
