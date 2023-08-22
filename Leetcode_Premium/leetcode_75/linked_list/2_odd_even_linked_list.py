"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, 
and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        """
        head will remain the head of the new list (and the odd list since the odd list comes first)
        odd --> form the odd list
        even --> form the even list
        evenHead --> head of the even list
        """
        odd, even = head, head.next
        evenHead = even
        while even and even.next:
            odd.next = even.next
            even.next = even.next.next
            even = even.next
            odd = odd.next

        odd.next = evenHead
        return head
