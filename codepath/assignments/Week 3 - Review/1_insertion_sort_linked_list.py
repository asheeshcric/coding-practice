# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
U: Given is a singly-linked list that contains integers in random order
    - Need to sort the list in ascending order and return the head of the sorted list

M:
- Use pointers: dummy_head, current, prev, and next to manipulate the list and sort it

P:
1. Create a dummy_head that will point to the new list
2. Use prev as dummy_head that will help us traverse the new list
3. Use current to traverse the original given list
4. Use nxt to keep track of the next node in the original list

5. For each node in the current list, find where it can be inserted in the new sorted list
6. Once you find that position, insert it there and move to the next node



"""


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(None)
        current = head
        while current is not None:
            prev = dummy_head

            # First find where we can put the current element in the sorted list
            while prev.next and prev.next.val < current.val:
                # This means the current value is greater than the current number in the sorted list
                # So, check for the next one
                prev = prev.next

            # Once we know where we need to put in the current value, first store the next node in the original list
            nxt = current.next

            # Add the current value to the sorted list
            current.next = prev.next
            prev.next = current

            # Now, we move to the next node in the original list
            current = nxt

        return dummy_head.next
