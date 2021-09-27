"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.


"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        result = []
        for i, digit in enumerate(digits[::-1]):
            if i == 0:
                # So, we need to add 1 to the first digit
                add = digit + 1
            else:
                add = digit + carry

            new_digit = add % 10
            carry = add // 10
            result.append(new_digit)

        if carry != 0:
            result.append(carry)

        return result[::-1]
