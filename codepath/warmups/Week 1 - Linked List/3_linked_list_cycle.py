# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
Can also use a hashSet to check if you encounter any previously visited node in the list
"""


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
