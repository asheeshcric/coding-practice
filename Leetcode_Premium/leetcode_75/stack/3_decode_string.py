"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. 
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.
For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

"""


"""
The idea is to process the encoded substring as soon as we find an ending bracket ']'
Then add the decoded substring to the stack and keep decoding the rest of the string
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                # this means we need to now keep popping from the stack until we find the initial bracket and the integer
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring

                # Remove the opening bracket
                stack.pop()
                mul = ""
                while stack and stack[-1].isdigit():
                    mul = stack.pop() + mul

                stack.append(substring * int(mul))
            else:
                stack.append(char)

        print(stack)

        return "".join(stack)


sol = Solution()
print(sol.decodeString("3[a]2[bc]"))
