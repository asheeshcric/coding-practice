"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # First remove all non-alphanumeric chars using an RE
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
