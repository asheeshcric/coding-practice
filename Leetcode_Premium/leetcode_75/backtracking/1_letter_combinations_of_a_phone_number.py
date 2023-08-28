"""
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []

        def backtrack(i, curr_str):
            if len(curr_str) == len(digits):
                # Base case: When we complete one combination of strings
                result.append(curr_str)
                return

            for char in digit_to_char[digits[i]]:
                backtrack(i + 1, curr_str + char)

        if digits:
            backtrack(0, "")

        return result
