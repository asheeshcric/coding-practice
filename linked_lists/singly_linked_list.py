class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data=data)
        # Check if there's a head node or not
        if new_node is None:
            # If no head, the new node is the head
            self.head = new_node
        else:
            # If list is not empty, traverse to the end and add the new node
            current = self.head
            while current.next is not None:
                current = current.next
            
            current.next = new_node
