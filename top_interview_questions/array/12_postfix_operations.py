class Solution:
    def post_fix(self, expr: str) -> int:
        stack = []
        operand = ""
        for char in expr:
            if char == " ":
                stack.append(int(operand))
                operand = ""
            elif char in "+-*/":
                # reduce the operation
                try:
                    result = self.evaluate(op=char, num2=stack.pop(), num1=stack.pop())
                except Exception:
                    return "Invalid Expression!"
                stack.append(result)
            else:
                operand += char

        return result

    def evaluate(self, op, num2, num1):
        if op == "+":
            return num1 + num2
        elif op == "-":
            return num1 - num2
        elif op == "*":
            return num1 * num2
        elif op == "/":
            return num1 / num2


x = Solution()
print(x.post_fix("6 5 1 + /"))
