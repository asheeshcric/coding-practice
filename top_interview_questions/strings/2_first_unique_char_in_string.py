"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

U:
- We need the frequency of each char and find out which one has a count of 1.
- Out of chars with count=1, find the one that occurs the first in the string

M:
- Use a hashMap to keep track of the freq
- Using the count values, see which ones have count=1
- Among those chars, return the one with the least index position

P:
- freq = dict() to keep track of the count of each char in the string
- unique = set() -- add chars that occur only once and removes if a char has count of more than 1
- At the end, we start from the beginning of the string and check which of them is present in the unique set().
- The first one present is the first unique chars.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = dict()
        unique = set()
        for char in s:
            freq[char] = freq.get(char, 0) + 1
            if freq[char] > 1:
                if char in unique:
                    unique.remove(char)
            else:
                unique.add(char)

        for i, char in enumerate(s):
            if char in unique:
                return i

        return -1
