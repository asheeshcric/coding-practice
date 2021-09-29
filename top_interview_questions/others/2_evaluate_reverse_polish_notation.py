from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-/*":
                # Pop two numbers from the stack and perform the operation
                result = self.calculate(
                    num2=int(stack.pop()), num1=int(stack.pop()), token=token
                )
                stack.append(int(result))
            else:
                stack.append(token)

        if stack:
            return stack[-1]

        return result

    def calculate(self, num2, num1, token):
        if token == "+":
            return num1 + num2
        elif token == "-":
            return num1 - num2
        elif token == "/":
            return num1 / num2
        elif token == "*":
            return num1 * num2
        else:
            return None
