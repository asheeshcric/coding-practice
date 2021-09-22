"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
"""
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r"[^0-9a-z]", "", s)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
