"""
It's a simple binary search from 2 to x // 2


If x < 2, return x.

Set the left boundary to 2, and the right boundary to x / 2.

While left <= right:

    Take num = (left + right) / 2 as a guess. Compute num * num and compare it with x:

    If num * num > x, move the right boundary right = pivot -1

    Else, if num * num < x, move the left boundary left = pivot + 1

    Otherwise num * num == x, the integer square root is here, let's return it

Return right


"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 2, x // 2

        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot

        return right
