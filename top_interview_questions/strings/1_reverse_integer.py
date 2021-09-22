"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


"""


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        int_min = -(2 ** 31)
        int_max = 2 ** 31 - 1

        sign = 1
        s = str(x)
        if s[0] == "-":
            sign = -1
            s = s[1:]

        last = len(s) - 1
        while last >= 0 and s[last] == "0":
            last -= 1

        s = s[: last + 1][::-1]
        num = sign * int(s)
        return num if int_min <= num <= int_max else 0
