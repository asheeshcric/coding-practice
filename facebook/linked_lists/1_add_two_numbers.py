from typing import Optional


class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        prev = None
        while l1 or l2:
            d1 = 0 if l1 is None else l1.val
            d2 = 0 if l2 is None else l2.val
            add = d1 + d2 + carry
            carry = add // 10
            digit = add % 10
            new_node = ListNode(val=digit)
            if prev:
                prev.next = new_node
            else:
                head = new_node

            prev = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # At the end, if there's a carry left, we'll add that as an extra digit to the number
        if carry != 0:
            prev.next = ListNode(val=carry)

        return head
