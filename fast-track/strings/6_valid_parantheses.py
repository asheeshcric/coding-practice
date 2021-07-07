"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


def valid_parantheses(s):
    if len(s) < 2:
        return False

    stack = []
    paran_map = {"(": ")", "{": "}", "[": "]"}
    for paran in s:
        if paran in ["(", "{", "["]:
            stack.append(paran)
        elif len(stack) > 0:
            last_paran = stack.pop()
            if paran_map[last_paran] != paran:
                return False
        else:
            return False

    return True if len(stack) == 0 else False


if __name__ == "__main__":
    s = "{}()[}{}"
    print(valid_parantheses(s))
