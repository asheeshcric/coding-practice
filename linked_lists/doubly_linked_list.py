class Node:

    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class DLinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data=data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            new_node.prev = current
            current.next = new_node
