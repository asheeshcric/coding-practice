class MyQueue:
    def __init__(self):
        self.first_stack = []
        self.second_stack = []
        self.front = None

    def push(self, x: int) -> None:
        if len(self.first_stack) == 0:
            self.front = x

        while len(self.first_stack) > 0:
            self.second_stack.append(self.first_stack.pop())

        self.second_stack.append(x)

        while len(self.second_stack) > 0:
            self.first_stack.append(self.second_stack.pop())

    def pop(self) -> int:
        item = self.first_stack.pop()
        if len(self.first_stack) > 0:
            self.front = self.first_stack[-1]

        return item

    def peek(self) -> int:
        return self.front

    def empty(self) -> bool:
        return len(self.first_stack) == 0
