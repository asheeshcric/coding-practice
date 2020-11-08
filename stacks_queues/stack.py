class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top is None:
            print('Stack empty!')
            return None
        else:
            top = self.top
            self.top = self.top.next
            return top.data

    def peek(self):
        return self.top.data if self.top else None
