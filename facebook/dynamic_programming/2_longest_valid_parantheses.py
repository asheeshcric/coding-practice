class Solution:
    """
    The idea is to use stack for this as well (as we did for finding if the parantheses is valid or not), but will be used differently
    Steps:
    1. Add -1 to the stack
    2. Run a loop through the string
    3. If the bracket is open, i.e "(":
        - push the index of that char to the stack
       Else:
        - pop from the stack
        - Check if the stack is empty or not
        - If stack is empty:
            - The substring until now is not a valid parantheses condition
            - Need to push the current index to the stack as the starting index for being valid
        - Else:
            - Find the length of the valid parantheses until now
            - len = current_index (i) - index on top of the stack

    4. Update the max length of valid parantheses
    5. Return the answer after the loop

    """

    def longest_valid_parantheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]
        for i, bracket in enumerate(s):
            if bracket == "(":
                # Push the index to the stack
                stack.append(i)
            else:
                # Pop from the stack and check if the stack becomes empty or not
                stack.pop()
                if len(stack) != 0:
                    # Stack is not empty, so a valid parantheses
                    new_len = i - stack[-1]
                    max_len = max(max_len, new_len)
                else:
                    # Need to push the current index to the stack as we cannot let the stack remain empty
                    # This will act as our starting point all over again to point the beginning of a valid parantheses combination
                    stack.append(i)
        return max_len
