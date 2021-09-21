# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
Traverse through the list:
Keep changing the pointers direction for each pair
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head
        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev
