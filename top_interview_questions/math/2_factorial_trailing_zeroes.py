"""
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
"""


from typing import Counter


class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero_count = 0
        while n > 0:
            n = n // 5
            zero_count += n

        return zero_count
