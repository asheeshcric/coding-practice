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

    def delete(self, data):
        if self.head.data == data:
            second_node = self.head.next
            second_node.prev = None
            self.head = second_node
        else:
            current = self.head
            while current.next is not None:
                if current.next.data == data:
                    if current.next.next is None:
                        # Checking if it is the last node
                        current.next = None
                    else:
                        current.next = current.next.next
                        current.next.next.prev = current
                    break

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()