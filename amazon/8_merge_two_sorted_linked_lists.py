class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    if l1.val < l2.val:
        head = l1
        temp_l1 = l1.next
        temp_l2 = l2
    else:
        head = l2
        temp_l1 = l1
        temp_l2 = l2.next

    curr = head
    while temp_l1 is not None and temp_l2 is not None:
        if temp_l1.val < temp_l2.val:
            curr.next = temp_l1
            curr = curr.next
            temp_l1 = temp_l1.next
        else:
            curr.next = temp_l2
            curr = curr.next
            temp_l2 = temp_l2.next

    curr.next = temp_l1 if temp_l2 is None else temp_l2

    return head
