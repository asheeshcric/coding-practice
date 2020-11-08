class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.head = None

    def add(self, data):
        # Add an item to the end of the queue
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = new_node

    def remove(self):
        # Remove the first item in the queue
        if self.head is None:
            return False
        else:
            top_node = self.head
            self.head = self.head.next
            return top_node.data

    def peek(self):
        return self.head.data

    def is_empty(self):
        return self.head is None
