"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars_s = dict()
        chars_t = dict()
        for c_s, c_t in zip(s, t):
            chars_s[c_s] = chars_s.get(c_s, 0) + 1
            chars_t[c_t] = chars_t.get(c_t, 0) + 1

        for char in chars_s:
            if char not in chars_t or chars_s[char] != chars_t[char]:
                return False

        return True
